import base64

import streamlit as st

# ----- Page configs (tab title, favicon) -----
st.set_page_config(
        page_title = "Fallou Fall Portfolio" ,
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2023***")
    st.write("**Author:**[Fallou Fall  ](https://github.com/FallouFall)")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(
        f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Fallou Fall</h1></div>""" ,
        unsafe_allow_html = True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "pp.jpg"  # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Master in Big & Data Analytics at EAE Business School Barcelona"  # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 I am a Student at EAE Business School 

- 🛩️ prev: I am a certified software engineer specializing in Java. Over the past three years, I have worked at a mid-sized startup, marking my first job after graduating from college.
 While I have accumulated valuable experience in coding during this time, I am currently aiming to shift away from coding while retaining a technical focus. 
My current interest lies in becoming a Big Data Analyst, which is why I am pursuing another master's degree at EAE Business School.

- ❤️ I am a technology enthusiast. My love for computers is all-encompassing—I find joy in every aspect of them. 
From coding and debugging for eight to ten hours a day to engaging in discussions about coding practices with fellow programmers, computers are at the center of my professional life. 
Even outside the realm of programming, I extend my passion by teaching about computers at the primary school in my neighborhood .
The thrill of a new Linux kernel release or the availability of a groundbreaking web application for beta testing excites me to no end. 
Witnessing elegant and intelligent code solving complex problems is deeply impressive. 
It's during these moments that I believe we have only scratched the surface of what computers,data can achieve,
 and I'm driven to find simple solutions to the programming challenges I encounter.

- 🤖 Data Visualisation web application  PYTHON                           https://datavisualisation.streamlit.app/
     hospital management    JAVAFX/Springbook/Angular                     https://github.com/FallouFall/Hoggy_Web
     School management      JEE/Springbook/Continuous Integration         https://github.com/FallouFall/GestionScolaire
     School management      JEE/Springbook/Continuous Integration/RMI     https://github.com/FallouFall/ServeurGestionEtudiant
     School management      JEE/Springbook/Continuous Integration/RMI     https://github.com/FallouFall/ClientGestionEtudiants

- 📫 How to reach me: falloufalllive@gmail.com
    https://www.linkedin.com/in/fallou-fall-047675173/

- 🏠 Barcelona: Lloret del Mar Barcelona 
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.
