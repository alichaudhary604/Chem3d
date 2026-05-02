import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Interactive Periodic Table", layout="wide")
st.title(" Interactive Periodic Table")

# 1. Create the Data (Expanding this list adds more elements)
elements = [
    {"symbol": "H", "name": "Hydrogen", "atomic_number": 1, "group": 1, "period": 1, "mass": 1.008, "type": "Nonmetal"},
    {"symbol": "He", "name": "Helium", "atomic_number": 2, "group": 18, "period": 1, "mass": 4.003, "type": "Noble Gas"},
    {"symbol": "Li", "name": "Lithium", "atomic_number": 3, "group": 1, "period": 2, "mass": 6.941, "type": "Alkali Metal"},
    {"symbol": "Be", "name": "Beryllium", "atomic_number": 4, "group": 2, "period": 2, "mass": 9.012, "type": "Alkaline Earth"},
    {"symbol": "B", "name": "Boron", "atomic_number": 5, "group": 13, "period": 2, "mass": 10.811, "type": "Metalloid"},
    {"symbol": "C", "name": "Carbon", "atomic_number": 6, "group": 14, "period": 2, "mass": 12.011, "type": "Nonmetal"},
    {"symbol": "N", "name": "Nitrogen", "atomic_number": 7, "group": 15, "period": 2, "mass": 14.007, "type": "Nonmetal"},
    {"symbol": "O", "name": "Oxygen", "atomic_number": 8, "group": 16, "period": 2, "mass": 15.999, "type": "Nonmetal"},
    {"symbol": "F", "name": "Fluorine", "atomic_number": 9, "group": 17, "period": 2, "mass": 18.998, "type": "Halogen"},
    {"symbol": "Ne", "name": "Neon", "atomic_number": 10, "group": 18, "period": 2, "mass": 20.180, "type": "Noble Gas"},
    {"symbol": "Na", "name": "Sodium", "atomic_number": 11, "group": 1, "period": 3, "mass": 22.990, "type": "Alkali Metal"},
    {"symbol": "Mg", "name": "Magnesium", "atomic_number": 12, "group": 2, "period": 3, "mass": 24.305, "type": "Alkaline Earth"},
    {"symbol": "Al", "name": "Aluminium", "atomic_number": 13, "group": 13, "period": 3, "mass": 26.982, "type": "Post-transition Metal"},
    {"symbol": "Si", "name": "Silicon", "atomic_number": 14, "group": 14, "period": 3, "mass": 28.085, "type": "Metalloid"},
    {"symbol": "P", "name": "Phosphorus", "atomic_number": 15, "group": 15, "period": 3, "mass": 30.974, "type": "Nonmetal"},
    {"symbol": "S", "name": "Sulfur", "atomic_number": 16, "group": 16, "period": 3, "mass": 32.06, "type": "Nonmetal"},
    {"symbol": "Cl", "name": "Chlorine", "atomic_number": 17, "group": 17, "period": 3, "mass": 35.45, "type": "Halogen"},
    {"symbol": "Ar", "name": "Argon", "atomic_number": 18, "group": 18, "period": 3, "mass": 39.948, "type": "Noble Gas"},
    {"symbol": "K", "name": "Potassium", "atomic_number": 19, "group": 1, "period": 4, "mass": 39.098, "type": "Alkali Metal"},
    {"symbol": "Ca", "name": "Calcium", "atomic_number": 20, "group": 2, "period": 4, "mass": 40.078, "type": "Alkaline Earth"},
]

df = pd.DataFrame(elements)

# 2. Create the Figure
fig = px.scatter(
    df, 
    x="group", 
    y="period", 
    color="type",
    text="symbol",
    hover_name="name",
    hover_data={"group": False, "period": False, "atomic_number": True, "mass": True},
    size_max=60
)

# 3. Styling to make it look like a Table
fig.update_traces(marker=dict(size=40, symbol='square'), textfont=dict(color='white'))
fig.update_xaxes(side="top", dtick=1, range=[0.5, 18.5], title="Group")
fig.update_yaxes(autorange="reversed", dtick=1, range=[7.5, 0.5], title="Period")
fig.update_layout(height=600, margin=dict(l=20, r=20, t=20, b=20))

# 4. Show the Table
st.plotly_chart(fig, use_container_width=True)

# 5. The "Popup" Logic
st.write("---")
st.subheader("Element Details")
selected_element = st.selectbox("Select an element to see more details:", df["name"].unique())

details = df[df["name"] == selected_element].iloc[0]

col1, col2, col3 = st.columns(3)
col1.metric("Atomic Number", details["atomic_number"])
col2.metric("Relative Atomic Mass", details["mass"])
col3.metric("Type", details["type"])
