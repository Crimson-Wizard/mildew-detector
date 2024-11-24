import streamlit as st
from src.data_management import load_pkl_file


# Function to load a test evaluation object from a specific pickle file
def load_test_evaluation():
    return load_pkl_file('outputs/v4/evaluation.pk1')
