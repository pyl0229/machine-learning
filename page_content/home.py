import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Yilin Peng</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:pyl100229@gmail.com">pyl100229@gmail.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "PENGYILIN.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        Outstanding learning ability: capable of quickly mastering and applying data analysis tools and market research methodologies, effectively transforming the learned knowledge into strategic planning and decision support in practical work;

        Outstanding planning ability: Through in-depth analysis of sales data of over 600 SKUs across multiple time dimensions, scientifically planned product selection priorities and integrated online and offline marketing plans.

        Outstanding content capabilities: capable of systematically sorting out and analyzing complex information, and constructing a clear logical framework for market and brand development.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R, SQL
        - Communication: Mandarin (Native), Cantonese (Native), English (Fluent), French (Basic)
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 
