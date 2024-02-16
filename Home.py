# Libraries
######################
import streamlit as st
import base64
from PIL import Image
from pathlib import Path
######################

# Page
######################
st.set_page_config(
    page_title="Home"
)
######################

# Paths
######################
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style.css"
resume_file = current_dir / "assets" / "Resume_Shreshth_Rajpal.pdf"
profile_pic = current_dir / "assets" / "dp.png"
file_name = "Resume_Shreshth_Rajpal.pdf"
######################



# CSS, PDF & PROFIL PIC
######################
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
######################



# Header
######################
def download_button(label, data, file_name):
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/pdf;base64,{b64}" download="{file_name}" class="btn btn-outline-primary">{label}</a>'
    st.markdown(href, unsafe_allow_html=True)

col1, col2 = st.columns([1,2])
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.markdown("<h1 style='font-size:40px'>{}</h1>".format('Shreshth Rajpal'), unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px'>{}</p>".format('Data Science | Development'), unsafe_allow_html=True)
    download_button("Download Resume", PDFbyte, file_name)
    st.write("📫", 'shreshthrajpal@gmail.com')
######################



# Custom function for printing text
#####################
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
#####################


# Education
#####################
st.markdown('''## Education''')

txt('**Data Analytics Program**, Durham College, Oshawa',
'2023-2023')
st.markdown('''
- GPA: `3.4` 
- **Relevant Coursework**: `Data Collection,  DBMS,  EDA,  Tableau,  Dashboard, SQL` 
''')

txt('**Applied AI Solutions Program**, George Brown College, Toronto',
'2022-2022')
st.markdown('''
- GPA: `3.6` (Dean's Honour List)
- **Relevant Coursework**: `Machine Learning,  Deep Learning,  NLP,  Python` 
''')
#####################



# Work Experience
#####################
st.markdown('''
## Work Experience
''')
txt('**Data Analyst Intern**, Ernst & Young, India',
'2021-2021')

st.markdown('''
• Developed and implemented key column classification for line item categorization \n
• Segmented the data into GSTR1 Processing, reversed and re-raised entry cases to remove errors \n
• Executed comprehensive data operations to prepare it for DigiGST \n
• Collaborated with the team members to interpret data findings 
''')
#####################
            

# Skills
#####################
st.markdown('''## Skills''')
# Data Science
markdown_text = '> <h5 style="color: #1977F2">Data Science</h5>'
st.markdown(markdown_text, unsafe_allow_html=True)
txt3('Data Collection',  '`DBMS`, `Web Scraping`, `API`')
txt3('Data Preparation', '`Data Cleaning`, `Feature Engineering`')
txt3('Data Analysis and Viz',  '`EDA`, `Tableau`, `Dashboard`')
txt3('Models',  '`Machine Learning`, `NLP`,  `Deep Learning`')
txt3('Statistics',  '`Descriptive`,  `Inferential`')
txt3('Languages', '`Python`, `SQL`')

# Development
markdown_text = '> <h5 style="color: #1977F2">Development</h5>'
st.markdown(markdown_text, unsafe_allow_html=True)
txt3('Front End',  '`HTML`,  `CSS`,   `JavaScript`,  `Web Design`')
txt3('Back End', '`Node`,  `Express`,  `API`')
txt3('Libraries', '`Tailwind CSS`,  `Three.js`,  `React`')
txt3('Programming Languages', '`Python`, `JavaScript`')
txt3('Other',  '`Git`,  `Github`')
#####################


# Links
#####################
st.markdown('''## Links''')
txt2('LinkedIn', 'https://www.linkedin.com/in/shreshthrajpal/')
txt2('GitHub', 'https://github.com/shreshthr')
txt2('Kaggle', 'https://www.kaggle.com/shreshthrajpal')
#####################


