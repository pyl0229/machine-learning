import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "Yilin Peng - resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Yilin Peng - resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Yilin Peng")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** pyl100229@gmail.com
    - **Phone:** +852 64830523 | +86 13410522403
    - **LinkedIn:** [linkedin.com/in/yilin-peng-a44a55282/](https://www.linkedin.com/in/yilin-peng-a44a55282/)
    - **GitHub:** [github.com/pyl0229](https://github.com/pyl0229)
    - **Address:** Fuheng EST, TAIPO, HKSAR
    """)

    st.header("Professional Summary")
    st.markdown("""
    High potential candidate with master degree in Marketing in CUHK. Proven ability to lead teams, manage projects, and improve software performance. Seeking a challenging role to utilize my technical expertise and problem-solving skills.
    """)

    st.header("Intern Experience")
    st.markdown("""
    **Burson Cohn & Wolfe**
    - *April 2024 – July 2024*
    - Information collection and analysis
    - Risk early warning response
    - Content output promotion

    **Banana In**
    - *August 2022 – November 2022*
    - Commodity Selection analysis
    - Explosive product marketing
    - Strategy support
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**
    - Chinese University of Hong Kong
    - *Graduated: October 2025*
    - GPA: 3.7/4.0
    """)
    st.markdown("""
    **Bachelor of Arts in Business English**
    - University of International Business and Economics
    - *Graduated: May 2024*
    - GPA: 3.7/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, JavaScript, Java, C++
    - **Web Technologies:** HTML, CSS, React, Node.js, Django
    - **Databases:** MySQL, PostgreSQL, MongoDB
    - **Tools:** Git, Docker, Jenkins, AWS
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Certifications")
    st.markdown("""
    - AWS Certified Solutions Architect
    - Certified Scrum Master
    """)

    st.header("Projects")
    st.markdown("""
    **E-commerce Website**
    - Developed a full-stack e-commerce application using React and Django.
    - Integrated payment gateways and implemented user authentication.

    **Data Analysis Tool**
    - Created a Python-based tool for analyzing large datasets and visualizing results.
    - Used pandas and matplotlib libraries for data manipulation and plotting.
    """)

    st.header("Languages")
    st.markdown("""
    - **English:** Native
    - **Spanish:** Intermediate
    """)

    st.header("Interests")
    st.markdown("""
    - Open-source contributions
    - Blogging about technology trends
    - Hiking and outdoor activities
    """)

    st.markdown("---") 
