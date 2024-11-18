import streamlit as st
from src.data_management import load_pkl_file


def load_test_evaluation():
    return load_pkl_file('outputs/v1/evaluation.pk1')
