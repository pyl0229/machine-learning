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
    - **Programming Languages:** Python, R
    - **Databases:** MySQL, SQL Server
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Certifications")
    st.markdown("""
    - TEM-8
    - TEM-4
    - PSC
    """)

    st.header("Projects")
    st.markdown("""
    **Xiaohongshu Hong Kong User Acquisition Project**
    - Enhance Xiaohongshu's recognition and market share in Hong Kong by conducting user research to gather key insights for market strategies.
    - Content analysis utilized big data to understand user behavior patterns and optimize content direction..

    **Data Analysis Tool**
    - Created a Python-based tool for analyzing large datasets and visualizing results.
    - Used pandas and matplotlib libraries for data manipulation and plotting.
    """)

    st.header("Languages")
    st.markdown("""
    - **Cantonese:** Native
    - **English:** Fluent
    - **French:** Intermediate
    """)

    st.header("Interests")
    st.markdown("""
    - Public Speeking
    - Guzheng & Ukulele
    - Texas Hold 'em Poker
    """)

    st.markdown("---") 
