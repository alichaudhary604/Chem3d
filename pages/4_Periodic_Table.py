import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Complete AQA Periodic Table", layout="wide")
st.title("🎨 Interactive Periodic Table")

# Full Dataset: Atomic Number, Symbol, Name, Group, Period, Mass, Type
raw_data = [
    [1, "H", "Hydrogen", 1, 1, 1, "Non-metal"], [2, "He", "Helium", 18, 1, 4, "Noble Gas"],
    [3, "Li", "Lithium", 1, 2, 7, "Alkali Metal"], [4, "Be", "Beryllium", 2, 2, 9, "Alkaline Earth"],
    [5, "B", "Boron", 13, 2, 11, "Metalloid"], [6, "C", "Carbon", 14, 2, 12, "Non-metal"],
    [7, "N", "Nitrogen", 15, 2, 14, "Non-metal"], [8, "O", "Oxygen", 16, 2, 16, "Non-metal"],
    [9, "F", "Fluorine", 17, 2, 19, "Halogen"], [10, "Ne", "Neon", 18, 2, 20, "Noble Gas"],
    [11, "Na", "Sodium", 1, 3, 23, "Alkali Metal"], [12, "Mg", "Magnesium", 2, 3, 24, "Alkaline Earth"],
    [13, "Al", "Aluminium", 13, 3, 27, "Post-transition Metal"], [14, "Si", "Silicon", 14, 3, 28, "Metalloid"],
    [15, "P", "Phosphorus", 15, 3, 31, "Non-metal"], [16, "S", "Sulfur", 16, 3, 32, "Non-metal"],
    [17, "Cl", "Chlorine", 17, 3, 35.5, "Halogen"], [18, "Ar", "Argon", 18, 3, 40, "Noble Gas"],
    [19, "K", "Potassium", 1, 4, 39, "Alkali Metal"], [20, "Ca", "Calcium", 2, 4, 40, "Alkaline Earth"],
    [21, "Sc", "Scandium", 3, 4, 45, "Transition Metal"], [22, "Ti", "Titanium", 4, 4, 48, "Transition Metal"],
    [23, "V", "Vanadium", 5, 4, 51, "Transition Metal"], [24, "Cr", "Chromium", 6, 4, 52, "Transition Metal"],
    [25, "Mn", "Manganese", 7, 4, 55, "Transition Metal"], [26, "Fe", "Iron", 8, 4, 56, "Transition Metal"],
    [27, "Co", "Cobalt", 9, 4, 59, "Transition Metal"], [28, "Ni", "Nickel", 10, 4, 59, "Transition Metal"],
    [29, "Cu", "Copper", 11, 4, 63.5, "Transition Metal"], [30, "Zn", "Zinc", 12, 4, 65, "Transition Metal"],
    [31, "Ga", "Gallium", 13, 4, 70, "Post-transition Metal"], [32, "Ge", "Germanium", 14, 4, 73, "Metalloid"],
    [33, "As", "Arsenic", 15, 4, 75, "Metalloid"], [34, "Se", "Selenium", 16, 4, 79, "Non-metal"],
    [35, "Br", "Bromine", 17, 4, 80, "Halogen"], [36, "Kr", "Krypton", 18, 4, 84, "Noble Gas"],
    [37, "Rb", "Rubidium", 1, 5, 85, "Alkali Metal"], [38, "Sr", "Strontium", 2, 5, 88, "Alkaline Earth"],
    [39, "Y", "Yttrium", 3, 5, 89, "Transition Metal"], [40, "Zr", "Zirconium", 4, 5, 91, "Transition Metal"],
    [41, "Nb", "Niobium", 5, 5, 93, "Transition Metal"], [42, "Mo", "Molybdenum", 6, 5, 96, "Transition Metal"],
    [43, "Tc", "Technetium", 7, 5, 98, "Transition Metal"], [44, "Ru", "Ruthenium", 8, 5, 101, "Transition Metal"],
    [45, "Rh", "Rhodium", 9, 5, 103, "Transition Metal"], [46, "Pd", "Palladium", 10, 5, 106, "Transition Metal"],
    [47, "Ag", "Silver", 11, 5, 108, "Transition Metal"], [48, "Cd", "Cadmium", 12, 5, 112, "Transition Metal"],
    [49, "In", "Indium", 13, 5, 115, "Post-transition Metal"], [50, "Sn", "Tin", 14, 5, 119, "Post-transition Metal"],
    [51, "Sb", "Antimony", 15, 5, 122, "Metalloid"], [52, "Te", "Tellurium", 16, 5, 128, "Metalloid"],
    [53, "I", "Iodine", 17, 5, 127, "Halogen"], [54, "Xe", "Xenon", 18, 5, 131, "Noble Gas"],
    [55, "Cs", "Cesium", 1, 6, 133, "Alkali Metal"], [56, "Ba", "Barium", 2, 6, 137, "Alkaline Earth"],
    [72, "Hf", "Hafnium", 4, 6, 178, "Transition Metal"], [73, "Ta", "Tantalum", 5, 6, 181, "Transition Metal"],
    [74, "W", "Tungsten", 6, 6, 184, "Transition Metal"], [75, "Re", "Rhenium", 7, 6, 186, "Transition Metal"],
    [76, "Os", "Osmium", 8, 6, 190, "Transition Metal"], [77, "Ir", "Iridium", 9, 6, 192, "Transition Metal"],
    [78, "Pt", "Platinum", 10, 6, 195, "Transition Metal"], [79, "Au", "Gold", 11, 6, 197, "Transition Metal"],
    [80, "Hg", "Mercury", 12, 6, 201, "Transition Metal"], [81, "Tl", "Thallium", 13, 6, 204, "Post-transition Metal"],
    [82, "Pb", "Lead", 14, 6, 207, "Post-transition Metal"], [83, "Bi", "Bismuth", 15, 6, 209, "Post-transition Metal"],
    [86, "Rn", "Radon", 18, 6, 222, "Noble Gas"], [87, "Fr", "Francium", 1, 7, 223, "Alkali Metal"],
    [88, "Ra", "Radium", 2, 7, 226, "Alkaline Earth"]
]

df = pd.DataFrame(raw_data, columns=["atomic_number", "symbol", "name", "group", "period", "mass", "type"])

# Periodic Layout Plot
fig = px.scatter(
    df, x="group", y="period", color="type", text="symbol",
    hover_name="name", hover_data={"group":False, "period":False, "atomic_number":True, "mass":True},
    color_discrete_map={
        "Alkali Metal": "#FF4B4B", "Alkaline Earth": "#FFA500", "Transition Metal": "#FFD700",
        "Non-metal": "#00FF7F", "Halogen": "#00BFFF", "Noble Gas": "#DA70D6", 
        "Metalloid": "#40E0D0", "Post-transition Metal": "#C0C0C0"
    }
)

fig.update_traces(marker=dict(size=40, symbol='square'), textfont=dict(color='white', size=11))
fig.update_xaxes(side="top", dtick=1, range=[0, 19], title="Group")
fig.update_yaxes(autorange="reversed", dtick=1, range=[8, 0], title="Period")
fig.update_layout(height=500, margin=dict(l=10, r=10, t=10, b=10), showlegend=True)

st.plotly_chart(fig, use_container_width=True)

# Detail View
st.divider()
selected_name = st.selectbox("Search for an element:", df["name"].sort_values())
el = df[df["name"] == selected_name].iloc[0]

c1, c2, c3 = st.columns(3)
c1.metric("Atomic Number", el["atomic_number"])
c2.metric("Relative Atomic Mass", el["mass"])
c3.metric("Type", el["type"])
