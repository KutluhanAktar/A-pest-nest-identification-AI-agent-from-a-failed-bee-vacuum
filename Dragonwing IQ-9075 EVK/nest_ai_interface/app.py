import os
import base64
import uuid
from flask import Flask, render_template, request, jsonify, send_file, url_for
import ollama
from smolagents import ToolCallingAgent, LiteLLMModel, DuckDuckGoSearchTool, tool
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# ---------------------------------------------------------
# Flask Configuration
# ---------------------------------------------------------
app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
REPORTS_FOLDER = os.path.join(os.getcwd(), 'reports')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORTS_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['REPORTS_FOLDER'] = REPORTS_FOLDER


# ---------------------------------------------------------
# Tool 1: Analyze an Image using local Ollama Vision
# ---------------------------------------------------------
@tool
def analyze_image(image_path: str, prompt: str) -> str:
    """Analyzes a local image file using a vision model.

    Args:
        image_path: The file path to the local image (e.g. '/path/to/nest.jpg').
        prompt: Question or instruction for what to analyze in the image.

    Returns:
        str: Detailed textual description of what was identified in the image.
    """
    if not os.path.exists(image_path):
        return f"Error: Image path '{image_path}' not found."

    try:
        response = ollama.chat(
            model='llava:7b',
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [image_path]
            }]
        )
        return response['message']['content']
    except Exception as e:
        return f"Image analysis error: {str(e)}"


# ---------------------------------------------------------
# Tool 2: Generate PDF Report using ReportLab
# ---------------------------------------------------------
@tool
def generate_pdf_report(filename: str, title: str, summary: str, details: str, image_path: str = None) -> str:
    """Generates a formatted PDF report on disk.

    Args:
        filename: Target PDF file path (e.g. 'pest_inspection_report.pdf').
        title: Main header title for the report.
        summary: Short executive summary paragraph.
        details: Detailed findings, treatment plan, and professional advisory.
        image_path: (Optional) Local path to an image to include in the PDF report.

    Returns:
        str: Confirmation message with saved PDF location.
    """
    try:
        if not os.path.isabs(filename):
            filename = os.path.join(app.config['REPORTS_FOLDER'], os.path.basename(filename))

        doc = SimpleDocTemplate(
            filename,
            pagesize=letter,
            rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36
        )
        styles = getSampleStyleSheet()
        story = []

        # Header Title
        title_style = ParagraphStyle(
            'ReportTitle',
            parent=styles['Heading1'],
            fontSize=22,
            leading=26,
            textColor=colors.HexColor("#D97706"),  # Amber Accent
            spaceAfter=15
        )
        story.append(Paragraph(title, title_style))
        story.append(Spacer(1, 10))

        # Include Image if present
        if image_path and os.path.exists(image_path):
            img = RLImage(image_path, width=300, height=200)
            story.append(img)
            story.append(Spacer(1, 15))

        # Summary Section
        story.append(Paragraph("<b>Executive Summary & Identification:</b>", styles['Heading2']))
        story.append(Paragraph(summary, styles['BodyText']))
        story.append(Spacer(1, 15))

        # Details & Advisory Section
        story.append(Paragraph("<b>Treatment Guidelines & Professional Thresholds:</b>", styles['Heading2']))

        for paragraph in details.split('\n\n'):
            if paragraph.strip():
                story.append(Paragraph(paragraph.strip(), styles['BodyText']))
                story.append(Spacer(1, 8))

        doc.build(story)
        return f"PDF report successfully created and saved at: {os.path.abspath(filename)}"
    except Exception as e:
        return f"Failed to build PDF: {str(e)}"


# ---------------------------------------------------------
# Agent Setup (ToolCallingAgent)
# ---------------------------------------------------------
model = LiteLLMModel(
    model_id="ollama/qwen2.5:7b",
    api_base="http://localhost:11434"
)

agent = ToolCallingAgent(
    tools=[
        analyze_image,
        generate_pdf_report,
        DuckDuckGoSearchTool()
    ],
    model=model
)


# ---------------------------------------------------------
# Flask Routes
# ---------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Accepts selected frame base64 data, user pest guess, and executes ToolCallingAgent."""
    data = request.get_json(force=True, silent=True)

    if not data or 'image' not in data:
        return jsonify({'error': 'Invalid request: payload must contain image data'}), 400

    try:
        image_data = data['image']
        user_guess = data.get('user_guess', '').strip() or 'Unspecified by user'

        if ',' in image_data:
            image_data = image_data.split(',')[1]

        image_bytes = base64.b64decode(image_data)

        # Save selected frame to disk
        frame_filename = f"selected_frame_{uuid.uuid4().hex[:8]}.jpg"
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], frame_filename)

        with open(image_path, 'wb') as f:
            f.write(image_bytes)

        pdf_name = f"nest_ai_inspection_{uuid.uuid4().hex[:6]}.pdf"

        # Explicit tool calling constraints to avoid python code imports or key missing errors
        agent_prompt = f"""
        CRITICAL TOOL INSTRUCTION:
        - Do NOT output Python code blocks or import any packages.
        - Every tool call MUST strictly follow this exact JSON structure:
          {{"name": "tool_name", "arguments": {{"arg_name": "value"}}}}

        AVAILABLE TOOLS:
        1. analyze_image(image_path: str, prompt: str)
        2. web_search(query: str)
        3. generate_pdf_report(filename: str, title: str, summary: str, details: str, image_path: str)

        TASK PARAMETERS:
        User Pest Hypothesis: "{user_guess}"
        Local Image Path: "{image_path}"

        STEPS TO RUN:
        Step 1: Call `analyze_image` for '{image_path}' to confirm or correct the user hypothesis ("{user_guess}").
        Step 2: Call `web_search` to search for insect dust treatment procedures AND specific criteria for when to call a professional exterminator.
        Step 3: Call `generate_pdf_report` saving to '{pdf_name}'. Summarize visual findings vs user hypothesis, safe insect dust steps, and explicit criteria for when professional extermination is required. Include '{image_path}'.
        """

        # Execute ToolCallingAgent workflow
        agent_response = agent.run(agent_prompt)

        return jsonify({
            'success': True,
            'agent_output': str(agent_response),
            'pdf_url': url_for('download_pdf', filename=pdf_name)
        })

    except Exception as e:
        print(f"Server Processing Error: {str(e)}")
        return jsonify({'error': f"Internal agent execution error: {str(e)}"}), 500


@app.route('/download/<filename>')
def download_pdf(filename):
    file_path = os.path.join(app.config['REPORTS_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "File not found.", 404


# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)