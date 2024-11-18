import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation
import os


def page_ml_performance_body():
    st.write("### Train, Validation and Test Set: Labels Frequencies")
    labels_distribution_path = "outputs/v1/labels_distribution.png"
    if os.path.exists(labels_distribution_path):
        labels_distribution = imread(labels_distribution_path)
        st.image(
            labels_distribution,
            caption='Labels Distribution on Train, Validation and Test Sets')
    else:
        st.error(f"File not found: {labels_distribution_path}")
    st.write("---")

    st.write("### Model History")
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc_path = "outputs/v1/model_training_accuracy.png"
        if os.path.exists(model_acc_path):
            model_acc = imread(model_acc_path)
            st.image(model_acc, caption='Model Training Accuracy')
        else:
            st.error(f"File not found: {model_acc_path}")
    with col2:
        model_loss_path = "outputs/v1/model_training_losses.png"
        if os.path.exists(model_loss_path):
            model_loss = imread(model_loss_path)
            st.image(model_loss, caption='Model Training Losses')
        else:
            st.error(f"File not found: {model_loss_path}")
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    try:
        test_metrics = load_test_evaluation()
        st.dataframe(pd.DataFrame(test_metrics, index=['Loss', 'Accuracy']))
    except Exception as e:
        st.error(f"Error loading test evaluation: {e}")
