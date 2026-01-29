import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Researcher Profile | Simphiwe Mngadi",
    page_icon="📊",
    layout="wide"
)

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Simphiwe Mngadi"
field = "Mathematical Statistics & Data Science"
institution = "Cape Peninsula University of Technology"

# Display basic profile information
st.header("Researcher Overview")

col1, col2 = st.columns([2, 1])

with col1:
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

    st.write("""
    I am a final-year Mathematical Sciences student with strong interests in
    statistical modelling, data analysis, and machine learning.
    My research focuses on applying quantitative methods to real-world STEM
    and educational challenges.
    """)

with col2:
    st.image(
        "https://images.unsplash.com/photo-1531482615713-2afd69097998",
        caption="Data Science & Statistical Research",
        use_column_width=True
    )

# Add a section for publications
st.header("Publications")

uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications, use_container_width=True)

    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(
                lambda row: keyword.lower() in row.astype(str).str.lower().values,
                axis=1
            )
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered, use_container_width=True)

# Add a section for visualizing publication trends
st.header("Publication Trends")

if uploaded_file and "Year" in publications.columns:
    year_counts = publications["Year"].value_counts().sort_index()
    st.bar_chart(year_counts)

# Add STEM Data Section
st.header("Explore STEM Data")

# -------------------------------
# Generate dummy data
# -------------------------------
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# STEM Data Viewer
st.subheader("STEM Data Viewer")

data_option = st.selectbox(
    "Choose a dataset to explore",
    ["Physics Experiments", "Astronomy Observations", "Weather Data"]
)

if data_option == "Physics Experiments":
    energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
    st.dataframe(
        physics_data[physics_data["Energy (MeV)"].between(*energy_filter)],
        use_container_width=True
    )

elif data_option == "Astronomy Observations":
    brightness_filter = st.slider(
        "Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0)
    )
    st.dataframe(
        astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(*brightness_filter)
        ],
        use_container_width=True
    )

elif data_option == "Weather Data":
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    st.dataframe(
        weather_data[
            weather_data["Temperature (°C)"].between(*temp_filter) &
            weather_data["Humidity (%)"].between(*humidity_filter)
        ],
        use_container_width=True
    )

# Add a contact section
st.header("Contact Information")

email = st.text_input("Enter your contact email")
if email:
    st.success(f"You can reach {name} at {email}")

