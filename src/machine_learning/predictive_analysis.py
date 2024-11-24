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
        'Probability': [1 - pred_proba, pred_proba] if pred_class == 'Powdery Mildew' else [pred_proba, 1 - pred_proba]
    })

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y='Probability',
        range_y=[0, 1],
        width=600,
        height=300,
        template='seaborn'
    )
    st.plotly_chart(fig)


def resize_input_image(img):
    """
    Resize input image to the expected dimensions for the model.
    """
    try:
        # Load expected image shape
        image_shape = load_pkl_file(file_path="outputs/v4/image_shape.pk1")
        
        # Resize image and normalize
        img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
        img_array = np.array(img_resized) / 255.0  # Normalize to [0, 1]
        return np.expand_dims(img_array, axis=0)  # Add batch dimension
    except FileNotFoundError:
        st.error("Image shape file not found. Please ensure `image_shape.pk1` exists in `outputs/v4`.")
        raise
    except Exception as e:
        st.error(f"Error resizing image: {e}")
        raise

def load_model_and_predict(my_image):
    """
    Load the model and perform predictions on the input image.
    """
    # Path to the model
    model_path = 'outputs/v4/trained_model.h5'

    # Load the model
    try:
        new_model = load_model(model_path)
    except OSError:
        st.error(f"Model file not found at: {model_path}. Please upload the file to `outputs/v4`.")
        raise
    except Exception as e:
        st.error(f"Error loading model: {e}")
        raise

    # Validate input image
    if my_image is None:
        st.error("Invalid input image. Please upload a valid image.")
        return None, None

    # Perform prediction
    try:
        pred_proba = new_model.predict(my_image)[0, 0]
        target_map = {v: k for k, v in {'Healthy': 0, 'Powdery Mildew': 1}.items()}
        pred_class = target_map[pred_proba > 0.5]

        # Adjust probability for 'Healthy' class
        if pred_class == 'Healthy':
            pred_proba = 1 - pred_proba

        # Display results
        leaf_condition = 'has powdery mildew' if pred_class == 'Powdery Mildew' else 'is healthy'
        st.success(f"The leaf condition is {leaf_condition}")

        return pred_proba, pred_class
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        raise
