import streamlit as st
from src.data_management import load_pkl_file

def load_test_evaluation(file_path):
    """
    Load test evaluation results from a pickle file
    """
    try:
        return load_pkl_file(file_path)
    except FileNotFoundError:
        st.error(f"Test evaluation file not found: {file_path}")
        return None
    except Exception as e:
        st.error(f"Error loading test evaluation: {str(e)}")
        return None
