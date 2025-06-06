import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Corporate Communications and Public Affairs Intern
    **Burson Cohn & Wolfe** | *April 2024 - July 2024*
    
    - Information collection and analysis: Conducted comprehensive industry research for the Lenovo brand across platforms such as TechCrunch and Engadget. Performed comparative data analysis to identify and articulate Lenovo's distinct competitive advantages in technology R&D, product innovation, and customer service. Developed strategic advantage analysis reports to enhance brand visibility and content reach;
    - Risk early warning response: Utilized the risk matrix model to quantitatively evaluate potential risks impacting the Lenovo brand, considering both domestic and international public sentiment and policy shifts. Generated a conclusion with key areas of concern and their potential impact on the company's operations and collaborated with legal affairs team, to develop and implement mitigation strategies for identified risks. Successfully warned 2 intermediate potential risks in advance to support the maintenance of the company's business.
    - Content output promotion: Participated in the daily operation and management of Lenovo corporate public account. Responsible for the compilation of specific content. Fostered relationships with international media outlets to enhance Lenovo's external publicity efforts. Developed and executed content strategies aligned with key publicity objectives, resulting in a 30% increase in overall exposure for the brand.
    """)
    

    
    st.markdown("""
    ### Commodity Operation Intern
    **Banana In** | *August 2022 - November 2022*
    
    - Commodity Selection analysis: Conducted a thorough analysis of over 600 SKUs, examining sales, purchase rate, and profit rate across multiple timeframes, including sequential, year-on-year, last month, last quarter, the same period of last year, and the past year to complete a priority ranking for SKUs.  Anchored new product selections in alignment with current industry trends and performed a comparative analysis of competitive products' bestsellers against our own offerings to identify unique selling points and areas for differentiation. Leveraged our competitive advantages to enhance product differentiation in the market.
    - Explosive product marketing: Conducted in-depth analysis to identify and target key demographics (e.g.healthconscious parents in second-tier cities), for selected explosive products. Analyzed demand pain points including product use scenarios and functions to determine primary selling points (e.g. multi-functional versions and pattern types). Developed an integrated online and offline marketing strategy focusing on key scenarios (e.g. family travel and playground activities), which included social media promotion and offline event planning, effectively increasing exposure.
    - Strategy support: Supported strategic initiatives during peak sales seasons, monitoring market trends and consumer insights to refine product, pricing, and promotion strategies. Achieved a 20% sales boost and a 15% increase in inventory turnover for key products.
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Customer Segmentation Analysis",
            "description": "Used K-means clustering to segment customers based on purchasing behavior.",
            "skills": ["Python", "scikit-learn", "Pandas", "Matplotlib"],
            "outcome": "Identified 5 distinct customer segments that informed targeted marketing campaigns."
        },
        {
            "title": "Predictive Maintenance System",
            "description": "Developed a model to predict equipment failures before they occur.",
            "skills": ["Python", "TensorFlow", "Time Series Analysis", "IoT"],
            "outcome": "Reduced downtime by 23% and maintenance costs by 15%."
        },
        {
            "title": "Natural Language Processing for Customer Support",
            "description": "Created a text classification system to automatically categorize customer support tickets.",
            "skills": ["Python", "NLTK", "spaCy", "BERT"],
            "outcome": "Improved response time by 35% and increased customer satisfaction scores."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # Add the interactive visualization demo
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL, JavaScript
        - **Machine Learning:** scikit-learn, TensorFlow, PyTorch
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        - **Cloud Platforms:** AWS, Azure, Google Cloud
        - **Web Development:** Django, Flask, React
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 
