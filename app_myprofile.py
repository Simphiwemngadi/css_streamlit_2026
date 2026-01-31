import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(
    page_title="Researcher Profile | Simphiwe Mngadi",
    page_icon="📊",
    layout="wide"
)

# --------------------------------
# Title
# --------------------------------
st.title("Researcher Profile Page with STEM Data")

# --------------------------------
# Profile Information
# --------------------------------
name = "Simphiwe Mngadi"
field = "Mathematical Statistics & Data Science"
institution = "Cape Peninsula University of Technology"

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Researcher Overview")
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

    st.write("""
    I am a final-year Mathematical Sciences student with strong interests in
    statistical modelling, data analysis, and machine learning.
    My work focuses on applying quantitative and data-driven methods
    to real-world STEM and educational problems.
    """)

with col2:
    st.image(
        "PASTE_YOUR_GITHUB_PROFILE_IMAGE_URL_HERE",
        caption="Simphiwe Mngadi | GitHub Profile",
        use_column_width=True
    )

# --------------------------------
# Publications
# --------------------------------
st.header("Publications")

uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications, use_container_width=True)

    keyword = st.text_input("Filter by keyword")
    if keyword:
        filtered = publications[
            publications.apply(
                lambda row: keyword.lower() in row.astype(str).str.lower().values,
                axis=1
            )
        ]
        st.subheader("Filtered Publications")
        st.dataframe(filtered, use_container_width=True)

# --------------------------------
# Publication Trends (Professional Plot)
# --------------------------------
st.header("Publication Trends")

if uploaded_file and "Year" in publications.columns:
    year_counts = (
        publications["Year"]
        .value_counts()
        .reset_index()
        .rename(columns={"index": "Year", "Year": "Count"})
        .sort_values("Year")
    )

    chart = alt.Chart(year_counts).mark_bar().encode(
        x=alt.X("Year:O", title="Publication Year"),
        y=alt.Y("Count:Q", title="Number of Publications"),
        tooltip=["Year", "Count"]
    ).properties(
        width=700,
        height=400,
        title="Publications per Year"
    )

    st.altair_chart(chart, use_container_width=True)

# --------------------------------
# STEM Data Section
# --------------------------------
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

# --------------------------------
# STEM Viewer
# --------------------------------
st.subheader("STEM Data Viewer")

dataset = st.selectbox(
    "Choose a dataset to explore",
    ["Physics Experiments", "Astronomy Observations", "Weather Data"]
)

# ---------- Physics ----------
if dataset == "Physics Experiments":
    energy_range = st.slider("Energy Range (MeV)", 0.0, 10.0, (0.0, 10.0))
    filtered = physics_data[
        physics_data["Energy (MeV)"].between(*energy_range)
    ]

    st.dataframe(filtered, use_container_width=True)

    chart = alt.Chart(filtered).mark_line(point=True).encode(
        x=alt.X("Date:T", title="Date"),
        y=alt.Y("Energy (MeV):Q", title="Energy (MeV)"),
        tooltip=["Experiment", "Energy (MeV)"]
    ).properties(
        width=700,
        height=400,
        title="Physics Experiment Energy Levels Over Time"
    )

    st.altair_chart(chart, use_container_width=True)

# ---------- Astronomy ----------
elif dataset == "Astronomy Observations":
    brightness_range = st.slider(
        "Brightness Range (Magnitude)", -15.0, 5.0, (-15.0, 5.0)
    )

    filtered = astronomy_data[
        astronomy_data["Brightness (Magnitude)"].between(*brightness_range)
    ]

    st.dataframe(filtered, use_container_width=True)

    chart = alt.Chart(filtered).mark_circle(size=120).encode(
        x=alt.X("Observation Date:T", title="Observation Date"),
        y=alt.Y("Brightness (Magnitude):Q", title="Brightness"),
        tooltip=["Celestial Object", "Brightness (Magnitude)"]
    ).properties(
        width=700,
        height=400,
        title="Astronomical Brightness Observations"
    )

    st.altair_chart(chart, use_container_width=True)

# ---------- Weather ----------
elif dataset == "Weather Data":
    temp_range = st.slider("Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_range = st.slider("Humidity (%)", 0, 100, (0, 100))

    filtered = weather_data[
        weather_data["Temperature (°C)"].between(*temp_range) &
        weather_data["Humidity (%)"].between(*humidity_range)
    ]

    st.dataframe(filtered, use_container_width=True)

    chart = alt.Chart(filtered).mark_bar().encode(
        x=alt.X("City:N", title="City"),
        y=alt.Y("Temperature (°C):Q", title="Temperature (°C)"),
        color="Humidity (%):Q",
        tooltip=["City", "Temperature (°C)", "Humidity (%)"]
    ).properties(
        width=700,
        height=400,
        title="Weather Conditions by City"
    )

    st.altair_chart(chart, use_container_width=True)

# --------------------------------
# Contact
# --------------------------------
st.header("Contact Information")

email = st.text_input("Enter your contact email")
if email:
    st.success(f"You can reach {name} at {email}")