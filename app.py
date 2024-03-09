import streamlit as st

# Page configuration
st.set_page_config(page_title="Rowan's Personal Web Page", page_icon=":wave:", layout="wide")

# Title of the webpage
st.title("Welcome to Rowan's Web Page!")

# Introduction or Bio
st.header("About Me")
st.write("""
Hi there! I'm Rowan. I'm a tech enthusiast with a passion for learning new things and sharing my knowledge with others. 
In this website, you'll find information about my projects, skills, and how to connect with me.
""")

# Display an image (Adjust the path or URL to your image)
st.image("IMG_3919.JPG", caption="This is me!")

# Skills Section
st.header("Skills")
st.write("""
- **Programming Languages:** Python, JavaScript, Java
- **Frameworks and Tools:** Streamlit, React, Node.js
- **Interests:** Data Science, Web Development, Machine Learning
""")

# Projects Section
st.header("Projects")
st.write("""
1. **Project Name 1:** Description of project 1. The project focuses on ...
2. **Project Name 2:** Description of project 2. This project aims to ...
3. **Project Name 3:** Description of project 3. An interesting project that ...
""")

# Contact or Social Media Section
st.header("Connect with Me")
st.write("""
Feel free to reach out or follow me on social media.
- **LinkedIn:** (https://www.linkedin.com/in/hengjun-zhang-930007116/)
- **GitHub:** (https://github.com/hengjunzhang)
""")

# Footer
st.write("---")
st.write("Thanks for visiting my website. Have a great day!")
