import streamlit as st
import matplotlib.pyplot as plt

def page_hypothesis_body():
    st.write("### Hypothesis and Validation")
    st.markdown("""
                Using a dataset, I hypothesis we can apply machine
                 learning techniques to analyze images and accurately
                 distinguish between healthy leaves and those affected
                 by powdery mildew.
                """)
    st.success(
        f"Using machine learning, we compared differences between images"
        f" that exhibit noticeable but small variations in shape and color."
        f" By analyzing the average images of healthy"
        f" leaves and those affected by powdery mildew,"
        f" we identified key patterns, such as"
        f" discoloration and subtle shape changes,"
        f" that distinguish the diseased leaves from healthy ones."
    )
