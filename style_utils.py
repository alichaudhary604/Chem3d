# style_utils.py
import streamlit as st

def apply_theme():
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
