import streamlit as st

def page_hypothesis_body():
    st.write("### Hypothesis and Validation")
    st.success(
        f"* Using machine learning, we compared differences between images that exhibit noticeable but small variations in shape and color."
        f"* By analyzing the average images of healthy leaves and those affected by powdery mildew,"
        f"we identified key patterns, such as discoloration and subtle shape changes, that distinguish the diseased leaves from healthy ones."
    )
    