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
        raise FileNotFoundError(
            f"{file_path} not found. Ensure the file exists.")

    image_shape = load_pkl_file(file_path=file_path)
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0) / 255

    return my_image


def load_model_and_predict(my_image):
    """
    Load and perform ML prediction over live images
    """
    model_path = os.path.join("outputs", "v1", "trained_model.h5")
    try:
        model = load_model(model_path)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None

    pred_proba = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'Healthy': 0, 'Powdery mildew': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
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
