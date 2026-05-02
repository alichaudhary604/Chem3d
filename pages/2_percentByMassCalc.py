import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors
from collections import Counter

st.set_page_config(page_title="Chem Calculator", layout="wide")
st.title("molar % by mass")

smiles = st.text_input("Enter SMILES (e.g., C6H12O6 for Glucose):", "C6H12O6")

if smiles:
    try:
        mol = Chem.MolFromSmiles(smiles)
       
        mw = Descriptors.MolWt(mol)
        formula = Chem.rdMolDescriptors.CalcMolFormula(mol)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Molecular Weight", f"{mw:.4f} g/mol")
        with col2:
            st.metric("Chemical Formula", formula)

        # 2. Percentage Composition Logic
        st.subheader("Mass Percent Composition")
        
        # Get all atoms in the molecule (including Hydrogens)
        mol_with_hs = Chem.AddHs(mol)
        atoms = [atom.GetSymbol() for atom in mol_with_hs.GetAtoms()]
        atom_counts = Counter(atoms)
        
        # Periodic Table Data (Masses of common elements)
        ptable = Chem.GetPeriodicTable()
        
        comp_data = []
        for symbol, count in atom_counts.items():
            atomic_weight = ptable.GetAtomicWeight(symbol)
            total_element_mass = atomic_weight * count
            percentage = (total_element_mass / mw) * 100
            comp_data.append({
                "Element": symbol,
                "Count": count,
                "Total Mass": round(total_element_mass, 3),
                "Percentage": f"{percentage:.2f}%"
            })
            
        st.table(comp_data)
        
    except Exception as e:
        st.error(f"unknown format error. Error: {e}")
