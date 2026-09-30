> I developed my portfolio website — kutluhanaktar.com — from scratch and decided to migrate all of my codebase to GitHub to provide a simple and straightforward experimentation or replication method for my proof-of-concept projects. Nonetheless, since I focused on demonstrating my thought process and experiment results thoroughly in the written tutorial format, including but not limited to PCB and 3D model designing steps, I could not provide enough information to fully explain my concepts and instructions via GitHub descriptions only. Thus, I highly recommend inspecting the associated project tutorials and videos on my portfolio website or other platforms (maker communities), i.e., Hackster, Hackaday, and Instructables.

# Original Project Publication Date

**October 5, 2026**

# Description

**Inspired to develop this local AI agent after failing to remove a yellowjacket nest with my custom bee vacuum due to my lack of knowledge :)**

If you are familiar with my project tutorials, you may know that I enjoy developing multidisciplinary proof-of-concept research projects that focus on solving real-world problems. Usually, it takes a long time for me to complete a project since I prefer designing custom mechanical parts, PCBs, and firmware from the ground up to be able to control all experiment parameters. Nonetheless, this project was an impromptu idea born out of a failed solution while I was trying to get rid of a pest infestation on my balcony. In this project, I wanted to showcase how a lack of knowledge and experience may lead to a painful and costly mistake, and how employing AI-oriented assistance can help prevent mistakes by providing educated guesses on potential culprits and emphasizing contacting experts for nest removal.

Nearly two months ago, I noticed bee-like pest activity near a small opening outside the wall insulation in my balcony. After some superficial research on species that prefer wall insulation and seeing a bumblebee flying over the flowers on my balcony, I falsely deduced that the pest nest belonged to a bumblebee colony. Thus, I did not give much credence to the increasing colony size and decided to design a custom 3D-printable bee trap, inspired by honey bee vacuums, to safely relocate the nest. As I thought I could create an easily replicable device to help people facing a similar problem, I decided to design my bee trap as an add-on accessory to my Samsung cylinder vacuum cleaner. In this regard, I gradually worked on my bee vacuum and designed it to be attachable between the cleaner hose and the hose connection adapter. I heavily focused on the device's modularity and redirecting the negative pressure and airflow (suction) to safely collect bees.

However, I have made a huge mistake by focusing on the results and ignoring my lack of knowledge about pest species. I realized my mistake as I was searching for bumblebees' airflow resistance to design a safe bee vacuum inner frame. Thanks to a random but lucky article inspection, I came to the conclusion that the flight patterns of the species residing in my balcony do not correspond to those of bees but rather to those of wasps. Considering the wall insulation nest, they were more likely yellowjackets. Once I went out to investigate the nest up close to confirm my new assumption, I could not even get near it; the colony had become too aggressive. The only thing I could do was to squeeze a plastic bag near the opening via a broom to protect myself. Since I utilized this balcony area as storage and only inspected the nest behind a window, I did not notice this aggressiveness and threat.

After realizing this was a pest infestation, I decided to speed up developing my bee vacuum and remove the nest immediately. I even purchased a beekeeping hoodie :) Unfortunately, again due to my lack of knowledge and experience, I made colossally wrong assumptions about the nest population and size. Once I tried to remove the pest nest with my bee vacuum, hundreds of yellowjackets swarmed and stung me three times. Thankfully, I was wearing the hoodie and did not show any allergic symptoms. Thus, my experiment did not cause any serious health issues; the only positive result I got from this experiment was a funny video documenting how yellowjackets successfully repelled me :)

At this point, this infestation stopped being an experiment on a custom bee vacuum and became a dangerous threat to me and my neighbours. Thus, I immediately contacted a professional firm to eliminate the yellowjacket infestation. They applied chemical treatment and needed to break the wall insulation to remove the whole nest. Little did I know, the insulation company left a huge void between the panels, throwing all of my nest size estimations out of the window.

After this painful yet enlightening experience, I still wanted to publish my 3D-printable bee vacuum since it can work perfectly for more docile species such as bumblebees, in the case that the user has the appropriate protection gear and attire. Nevertheless, I also wanted to examine and share how I could employ AI to develop a simple solution to safely investigate potential pest species and their threat levels, leading the user to take action early and contact experts with scrutinizing articles not by chance but by contrivance. After mulling over different AI-oriented solutions, I decided to develop a VLM-enabled AI agent and assign a simple web interface to the agent for user interactions.

The web interface allows the user to upload videos of outside nest activity, select frames from the video, and pass the selected frame to the AI agent. The web interface also lets the user enter assumptions about pest species based on the monitored nest activity. Then, the AI agent utilizes a vision-language model to analyze the nest activity and deduce the pest species shown in the provided frame. After getting the VLM inference result, the agent searches the internet to collect information about the VLM-detected pest species and nest type. If the user provided assumptions, the agent also reviews the viability of these deductions based on its web-scraped research. Finally, the agent generates a PDF report file based on the web-extracted information, including potential pest culprits, species threat levels, colony behaviour, and the importance of contacting experts according to the predicted species.

Since I did not want to develop a complex AI agent pipeline, requiring paid subscriptions or high-end components, I decided to utilize the Dragonwing IQ-9075 EVK to:

- run the AI agent (smolagents),
- run large language models and vision-language models locally via Ollama,
- host the web interface via the Flask lightweight web framework.

After testing the AI agent and asking about my situation, it immediately suggested the infestation might be caused by paper wasps or yellowjackets. After specifying the wall insulation removal, the agent strongly suggested yellowjacket activity and the necessity of contacting professionals :) So the results clearly state that I would probably be able to solve my infestation problem in less than a week instead of enabling it to span nearly two and a half months if I were not ignorant of my inexperience and focused on developing a solution to gain more information, capitalizing on the open-source AI tools.

As discussed, I developed this AI agent to showcase how AI can provide tailored pest infestation reports, combining VLMs and LLMs, to help the user notice dangerous species and emphasize contacting experts instead of DIY solutions to prevent hazardous situations that could pose health risks. Of course, I cannot stress enough that this is a proof-of-concept project and is meant to encourage users to avoid DIY solutions in the case of dangerous pest species. If you notice colony aggressiveness or erratic pest behaviour, please do not trust any information, including but not limited to AI solutions, and directly contact experts for removal. You can develop needle-induced allergies at any time, even if you have been stung before and did not show symptoms. So, please do not be foolish like me, jumping to conclusions about developing a custom nest removal gadget, and conduct extensive research about potential risks with AI agent assistance or not 😊

# Inspect the project tutorial on:

- **[kutluhanaktar.com](https://www.kutluhanaktar.com/projects/A_pest_nest_identification_AI_agent_from_a_failed_bee_vacuum/)**

<img width="1024" height="556" alt="1" src="https://github.com/user-attachments/assets/a0ad68d0-bcb4-4231-a058-2fddc468ab65" />

<img width="1024" height="556" alt="model_design_8" src="https://github.com/user-attachments/assets/ab5f4a7d-3614-442b-84dc-0c9869b873a9" />

<img width="1024" height="556" alt="model_design_13" src="https://github.com/user-attachments/assets/d6a33740-3817-4599-91f2-02c3dd7b6d7b" />

<img width="1024" height="556" alt="model_design_14" src="https://github.com/user-attachments/assets/da158da0-d158-4b50-bdcf-22e2914cd779" />

<img width="1024" height="768" alt="2" src="https://github.com/user-attachments/assets/ee878337-5cbe-4e34-9102-1b33afd1a722" />

<img width="1024" height="768" alt="3" src="https://github.com/user-attachments/assets/d525e479-265d-489c-b4a7-331d1da11167" />

<img width="1024" height="768" alt="4" src="https://github.com/user-attachments/assets/439c2e1e-672b-4c4f-9dba-9d6cbe1077eb" />

<img width="1024" height="768" alt="5" src="https://github.com/user-attachments/assets/910e6e51-3188-443f-9e8a-c192be60d9b8" />

<img width="1024" height="556" alt="6" src="https://github.com/user-attachments/assets/c65ee1de-dfb0-4f67-ab39-b6732887033b" />

<img width="1024" height="556" alt="7" src="https://github.com/user-attachments/assets/00597a14-9216-4162-a992-ddd1b6bd1cf6" />

<img width="1024" height="556" alt="8" src="https://github.com/user-attachments/assets/a200a87a-1bb1-45fc-8717-9bcbf873cbc7" />

<img width="1024" height="556" alt="9" src="https://github.com/user-attachments/assets/5af415a2-59d4-4018-8c1b-38ac741d6a80" />
