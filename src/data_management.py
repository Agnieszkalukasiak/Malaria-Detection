
import pandas as pd
import streamlit as st
import joblib
import os

def download_dataframe_as_csv(df, filename):
    """
    Convert dataframe to CSV and provide download link
    """
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name=f"{filename}.csv",
        mime="text/csv"
    )

def load_pkl_file(file_path):
    """
    Load a pickled file
    """
    if os.path.exists(file_path):
        return joblib.load(file_path)
    else:
        raise FileNotFoundError(f"File not found: {file_path}")
