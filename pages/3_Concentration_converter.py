import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors

st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("🔄 Concentration Unit Converter")

# 1. Molecule Input
smiles = st.text_input("Enter Molecule (SMILES):", "NaOH")

if smiles:
    try:
        mol = Chem.MolFromSmiles(smiles)
        molar_mass = Descriptors.MolWt(mol)
        formula = Chem.rdMolDescriptors.CalcMolFormula(mol)
        
        st.info(f"**Molecule Identified:** {formula} | **Molar Mass:** {molar_mass:.2f} g/mol")

        # 2. Setup the "Two-Way" Converter
        col1, col2 = st.columns(2)
        
        with col1:
            input_unit = st.selectbox(
                "I have concentration in:",
                ["g/dm³ (Grams per decimetre cubed)", "mol/dm³ (Molarity)"]
            )
            value = st.number_input("Enter value:", value=1.0, step=0.1)

        # 3. Logic for conversion
        if "g/dm³" in input_unit:
            # g/dm3 -> mol/dm3: Divide by Molar Mass
            converted_value = value / molar_mass
            target_unit = "mol/dm³"
            calculation_text = f"{value} / {molar_mass:.2f}"
        else:
            # mol/dm3 -> g/dm3: Multiply by Molar Mass
            converted_value = value * molar_mass
            target_unit = "g/dm³"
            calculation_text = f"{value} × {molar_mass:.2f}"

        # 4. Big Result Display
        with col2:
            st.write("### Converted Value:")
            st.success(f"**{converted_value:.4f} {target_unit}**")
            st.caption(f"Math: {calculation_text}")

        # 5. Pro-tip for Exams
        st.divider()
        st.markdown(f"""
        **Exam Cheat Sheet for {formula}:**
        * To get **mol/dm³**: Take your $g/dm^3$ and **divide** by {molar_mass:.2f}.
        * To get **g/dm³**: Take your $mol/dm^3$ and **multiply** by {molar_mass:.2f}.
        """)

    except Exception as e:
        st.error(f"Please enter a valid SMILES string. Error: {e}")
