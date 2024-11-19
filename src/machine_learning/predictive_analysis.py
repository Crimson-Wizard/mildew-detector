import os
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """
    prob_per_class = pd.DataFrame({
        'Diagnostic': ['Healthy', 'Powdery Mildew'],
        'Probability': [1 - pred_proba, pred_proba]
    })

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y='Probability',
        range_y=[0, 1],
        width=600, height=300, template='seaborn'
    )
    st.plotly_chart(fig)


def resize_input_image(img):
    """
    Reshape image to average image size
    """
    file_path = os.path.join(os.getcwd(), "outputs", "v1", "image_shape.pk1")
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}. Ensure the file is uploaded")
        return None

    image_shape = load_pkl_file(file_path=file_path)
    if not image_shape:
        st.error("Invalid image shape from file")
        return None
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0) / 255
    
    return my_image


def load_model_and_predict(my_image):
    """
    Load and perform ML prediction over live images
    """
    # Construct the full path to the model
    model_path = os.path.join(os.getcwd(), "outputs", "v1", "trained_model.h5")

    # Debugging: Check the contents of the directory
    st.write(f"Working directory: {os.getcwd()}")
    try:
        st.write(f"Contents of outputs/v1: {os.listdir('outputs/v1')}")
    except FileNotFoundError:
        st.error("The directory 'outputs/v1' does not exist in the live environment.")
        return None, None

    # Check if the model file exists
    if not os.path.exists(model_path):
        st.error(f"Model file not found at: {model_path}. Please upload the model file.")
        return None, None

    # Attempt to load the model
    try:
        model = load_model(model_path)
        st.success("Model loaded successfully.")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None

    # Perform prediction
    # Get probability for class 1 (Powdery mildew)
    try:
        pred_proba = model.predict(my_image)[0, 0]  
        pred_class = "Powdery mildew" if pred_proba > 0.5 else "Healthy"

        if pred_class == "Powdery mildew":
            st.write(
                f"The predictive analysis indicates"
                f" the cherry leaf has **powdery mildew**."
            )
        else:
            st.write(
                f"The predictive analysis indicates"
                f" the cherry leaf is **healthy**."
            )

        return pred_proba, pred_class
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None, None
