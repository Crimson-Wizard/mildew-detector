import streamlit as st
import matplotlib.pyplot as plt

# function to display project summary
def page_project_summary_body():

    st.header("Project Summary")
    st.markdown("""
        The head of IT and Innovation at an agricultural company
        is tackling a challenge with powdery mildew,
        a fungal disease affecting their cherry plantations—one
        of their key products. Currently,
        employees manually inspect cherry trees, spending around
        30 minutes per tree to check for
        the disease and an additional minute to apply treatment if
        needed. With thousands of trees spread across multiple farms,
        this manual process is time-consuming and inefficient.

        To address this, the IT team proposed a machine learning (ML)
        system that can instantly detect powdery mildew from a tree leaf image,
        streamlining the process significantly. If successful, this
        approach could be expanded to other crops,
        improving efficiency and scalability across the company's operations.
    """)

    st.header("Business Requirements")
    st.markdown("""
        The project has 2 business requirements:
        - The client is interested in conducting a study to visually
        differentiate a cherry leaf that is healthy from one
        that contains powdery mildew.
        - The client is interested in predicting if a
        cherry tree is healthy or contains powdery mildew.
    """)

    st.markdown("""
        For more information about the project and datasets visit
        [mildew detector readme file]
        (https://github.com/Crimson-Wizard/mildew-detector/blob/main/README.md)
        """)
