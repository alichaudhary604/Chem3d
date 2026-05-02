import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="AQA Periodic Table", layout="wide")
st.title("🎨 Interactive Periodic Table (AQA Syllabus)")

# 1. Expanded Element Data
# Note: To finish the table, continue adding elements following this exact dictionary format
elements = [
    {"symbol": "H", "name": "Hydrogen", "atomic_number": 1, "group": 1, "period": 1, "mass": 1, "type": "Non-metal", "shells": "1"},
    {"symbol": "He", "name": "Helium", "atomic_number": 2, "group": 18, "period": 1, "mass": 4, "type": "Noble Gas", "shells": "2"},
    {"symbol": "Li", "name": "Lithium", "atomic_number": 3, "group": 1, "period": 2, "mass": 7, "type": "Alkali Metal", "shells": "2,1"},
    {"symbol": "Be", "name": "Beryllium", "atomic_number": 4, "group": 2, "period": 2, "mass": 9, "type": "Alkaline Earth", "shells": "2,2"},
    {"symbol": "B", "name": "Boron", "atomic_number": 5, "group": 13, "period": 2, "mass": 11, "type": "Metalloid", "shells": "2,3"},
    {"symbol": "C", "name": "Carbon", "atomic_number": 6, "group": 14, "period": 2, "mass": 12, "type": "Non-metal", "shells": "2,4"},
    {"symbol": "N", "name": "Nitrogen", "atomic_number": 7, "group": 15, "period": 2, "mass": 14, "type": "Non-metal", "shells": "2,5"},
    {"symbol": "O", "name": "Oxygen", "atomic_number": 8, "group": 16, "period": 2, "mass": 16, "type": "Non-metal", "shells": "2,6"},
    {"symbol": "F", "name": "Fluorine", "atomic_number": 9, "group": 17, "period": 2, "mass": 19, "type": "Halogen", "shells": "2,7"},
    {"symbol": "Ne", "name": "Neon", "atomic_number": 10, "group": 18, "period": 2, "mass": 20, "type": "Noble Gas", "shells": "2,8"},
    {"symbol": "Na", "name": "Sodium", "atomic_number": 11, "group": 1, "period": 3, "mass": 23, "type": "Alkali Metal", "shells": "2,8,1"},
    {"symbol": "Mg", "name": "Magnesium", "atomic_number": 12, "group": 2, "period": 3, "mass": 24, "type": "Alkaline Earth", "shells": "2,8,2"},
    {"symbol": "Al", "name": "Aluminium", "atomic_number": 13, "group": 13, "period": 3, "mass": 27, "type": "Post-transition Metal", "shells": "2,8,3"},
    {"symbol": "Si", "name": "Silicon", "atomic_number": 14, "group": 14, "period": 3, "mass": 28, "type": "Metalloid", "shells": "2,8,4"},
    {"symbol": "P", "name": "Phosphorus", "atomic_number": 15, "group": 15, "period": 3, "mass": 31, "type": "Non-metal", "shells": "2,8,5"},
    {"symbol": "S", "name": "Sulfur", "atomic_number": 16, "group": 16, "period": 3, "mass": 32, "type": "Non-metal", "shells": "2,8,6"},
    {"symbol": "Cl", "name": "Chlorine", "atomic_number": 17, "group": 17, "period": 3, "mass": 35.5, "type": "Halogen", "shells": "2,8,7"},
    {"symbol": "Ar", "name": "Argon", "atomic_number": 18, "group": 18, "period": 3, "mass": 40, "type": "Noble Gas", "shells": "2,8,8"},
    {"symbol": "K", "name": "Potassium", "atomic_number": 19, "group": 1, "period": 4, "mass": 39, "type": "Alkali Metal", "shells": "2,8,8,1"},
    {"symbol": "Ca", "name": "Calcium", "atomic_number": 20, "group": 2, "period": 4, "mass": 40, "type": "Alkaline Earth", "shells": "2,8,8,2"},
    # Adding Transition Metals (Groups 3-12 are usually period 4)
    {"symbol": "Sc", "name": "Scandium", "atomic_number": 21, "group": 3, "period": 4, "mass": 45, "type": "Transition Metal", "shells": "N/A"},
    {"symbol": "Ti", "name": "Titanium", "atomic_number": 22, "group": 4, "period": 4, "mass": 48, "type": "Transition Metal", "shells": "N/A"},
    {"symbol": "V", "name": "Vanadium", "atomic_number": 23, "group": 5, "period": 4, "mass": 51, "type": "Transition Metal", "shells": "N/A"},
    {"symbol": "Cr", "name": "Chromium", "atomic_number": 24, "group": 6, "period": 4, "mass": 52, "type": "Transition Metal", "shells": "N/A"},
    {"symbol": "Mn", "name": "Manganese", "atomic_number": 25, "group": 7, "period": 4, "mass": 55, "type": "Transition Metal", "shells": "N/A"},
    {"symbol": "Fe", "name": "Iron", "atomic_number": 26, "group": 8, "period": 4, "mass": 56, "type": "Transition Metal", "shells": "N/A"},
    {"symbol": "Co", "name": "Cobalt", "atomic_number": 27, "group": 9, "period": 4, "mass": 59, "type": "Transition Metal", "shells": "N/A"},
    {"symbol": "Ni", "name": "Nickel", "atomic_number": 28, "group": 10, "period": 4, "mass": 59, "type": "Transition Metal", "shells": "N/A"},
    {"symbol": "Cu", "name": "Copper", "atomic_number": 29, "group": 11, "period": 4, "mass": 63.5, "type": "Transition Metal", "shells": "N/A"},
    {"symbol": "Zn", "name": "Zinc", "atomic_number": 30, "group": 12, "period": 4, "mass": 65, "type": "Transition Metal", "shells": "N/A"},
]

df = pd.DataFrame(elements)

# 2. Plotly Periodic Grid
fig = px.scatter(
    df, x="group", y="period", color="type", text="symbol",
    hover_name="name", hover_data={"group":False, "period":False, "atomic_number":True, "mass":True},
    color_discrete_map={
        "Alkali Metal": "#FF6666", "Alkaline Earth": "#FFDEAD", 
        "Transition Metal": "#FFB266", "Non-metal": "#90EE90",
        "Halogen": "#87CEFA", "Noble Gas": "#DDA0DD", "Metalloid": "#CCCCFF"
    }
)

fig.update_traces(marker=dict(size=45, symbol='square'), textfont=dict(color='white', size=14))
fig.update_xaxes(side="top", dtick=1, range=[0.5, 18.5], title="Group")
fig.update_yaxes(autorange="reversed", dtick=1, range=[7.5, 0.5], title="Period")
fig.update_layout(height=600, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')

st.plotly_chart(fig, use_container_width=True)

# 3. Detailed Element Inspector
st.write("---")
st.subheader("🔍 Element Inspector")
selected = st.selectbox("Select an element:", df["name"].sort_values())

data = df[df["name"] == selected].iloc[0]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Atomic Number (Z)", data["atomic_number"])
c2.metric("Atomic Mass (Ar)", data["mass"])
c3.metric("Group", data["group"])
c4.metric("Shells", data["shells"])

st.write(f"**Classification:** {data['type']}")
