import streamlit as st
from pathlib import Path


# Page Configuration
st.set_page_config(
    page_title="Simphiwe Mngadi | Portfolio",
    page_icon="📊",
    layout="wide"
)


# Paths (DEPLOY SAFE)

IMAGE_PATH = Path("assets/profile.jpg")
CV_PATH = Path("assets/SIMPHIWE MNGADI_CV.2026.pdf")


# Custom CSS

st.markdown("""
<style>
    .nav {
        display: flex;
        justify-content: center;
        gap: 40px;
        padding: 12px;
        background-color: #0f172a;
        border-radius: 8px;
    }
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)


# Navigation Bar

menu = st.radio(
    label="",
    options=["Home", "About", "Projects", "Contact"],
    horizontal=True
)


# HOME

if menu == "Home":
    col1, col2 = st.columns([1, 2])

    with col1:
        if IMAGE_PATH.exists():
            st.image(str(IMAGE_PATH), use_column_width=True)
        else:
            st.error("Profile image not found. Check assets/profile.jpg")

    with col2:
        st.title("Simphiwe Mngadi")
        st.subheader("Data Analyst | Data Science Graduate")

        st.write("""
        Detail-oriented Mathematical Sciences graduate with hands-on experience
        in data analysis, machine learning, and business intelligence.
        Passionate about transforming data into actionable insights to support
        evidence-based decision-making.
        """)

        if CV_PATH.exists():
            with open(CV_PATH, "rb") as pdf:
                st.download_button(
                    label="📄 Download My CV",
                    data=pdf,
                    file_name="Simphiwe_Mngadi_CV.pdf",
                    mime="application/pdf"
                )
        else:
            st.error("CV file not found. Check assets/SIMPHIWE_MNGADI_CV.2026.pdf")


# ABOUT
elif menu == "About":
    st.header("About Me")

    st.write("""
    I am a Mathematical Sciences graduate with experience in
    **data analysis, machine learning, and statistical modelling**.
    I enjoy working with real-world data to extract insights that
    support academic and business decision-making.
    """)

    st.subheader("Technical Skills")
    st.write("""
    - Python, SQL, R  
    - Power BI, Excel  
    - SAS  
    - Machine Learning (XGBoost, K-Means)  
    - Data Cleaning & EDA
    """)


# PROJECTS
elif menu == "Projects":
    st.header("Projects")

    st.subheader("Sales Interactive Dashboard | SQL & Power BI")
    st.write("""
    - Identified products with gross margin below 30% using SQL  
    - Built interactive Power BI dashboards for revenue and margin analysis  
    - Provided data-driven pricing recommendations
    """)

    st.subheader("Customer Segmentation | Python")
    st.write("""
    - Performed EDA on demographic and economic data  
    - Applied K-Means clustering with elbow-method optimisation  
    - Visualised customer segments to support targeted marketing strategies
    """)

# CONTACT

elif menu == "Contact":
    st.header("Contact")

    st.write(" **Phone:** 067 976 8625")
    st.write(" **Email:** mngadisimphiwe58@gmail.com")
    st.write(" **Location:** Western Cape, South Africa")

    

    st.markdown("""
    🔗 **Links**
    - [GitHub](https://github.com/Simphiwemngadi)
    - [LinkedIn](https://www.linkedin.com/in/simphiwe-mngadi-745a23266/)
    """)




