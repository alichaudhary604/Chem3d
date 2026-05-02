# style_utils.py
import streamlit as st

def apply_theme():
    st.markdown("""
<style>
    /* 1. Style the text and number input boxes */
    div[data-testid="stTextInput"] input, 
    div[data-testid="stNumberInput"] input,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 10px !important;
        backdrop-filter: blur(5px);
    }

    /* 2. Glow effect when you click/focus on an input */
    div[data-testid="stTextInput"] input:focus, 
    div[data-testid="stNumberInput"] input:focus {
        border: 1px solid #00d4ff !important;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.5) !important;
        transition: 0.3s ease-in-out;
    }

    /* 3. Style the dropdown (selectbox) list items */
    div[data-baseweb="popover"] ul {
        background-color: #1a1a3a !important;
        color: white !important;
    }
    
    /* 4. Style the labels (the text above the boxes) */
    label p {
        color: #00d4ff !important;
        font-weight: bold !important;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 0.8rem !important;
    }

    /* 5. Style Sliders */
    div[data-testid="stSlider"] [data-baseweb="slider"] {
        background-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            color: #ffffff;
        }
        [data-testid="stMetricValue"] {
            font-size: 2.2rem !important;
            color: #00d4ff !important;
            text-shadow: 0 0 10px rgba(0, 212, 255, 0.4);
        }
        /* This targets the sidebar and makes it semi-transparent */
        section[data-testid="stSidebar"] {
            background-color: rgba(20, 20, 50, 0.8) !important;
            backdrop-filter: blur(10px);
        }
        /* Makes tables look modern */
        .stTable {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
