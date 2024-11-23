import streamlit as st
import numpy as np
import os
import tensorflow as tf
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'Healthy': 0, 'Powdery Mildew': 1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    st.plotly_chart(fig)


def resize_input_image(img):
    try:
        image_shape = load_pkl_file(file_path=f"outputs/v2/image_shape.pk1")
        img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
        img_array = np.array(img_resized) / 255.0  # Normalize to [0, 1]
        return np.expand_dims(img_array, axis=0)  # Add batch dimension
    except Exception as e:
        raise ValueError(f"Error resizing image: {e}")



def load_model_and_predict(my_image,):
    st.write(f"Preprocessed image shape: {my_image.shape}")
    try:
        # Log the model path 
        model_path = "path_to_save/saved_model"
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model directory does not exist: {model_path}")

        required_files = ["saved_model.pb", "variables/variables.index", "variables/variables.data-00000-of-00001"]
        for file in required_files:
            if not os.path.exists(os.path.join(model_path, file)):
                raise FileNotFoundError(f"Missing file in model directory: {file}")
            
        # Load the model
        model = load_model(model_path)
        st.write("Model loaded successfully.")

        # Check the model's input shape
        st.write(f"Model expected input shape: {model.input_shape}")
        st.write(f"Input image shape: {my_image.shape}")

        # Perform prediction
        pred_proba = model.predict(my_image)[0, 0]
        st.write(f"Prediction probability: {pred_proba}")

        # Map prediction to class
        target_map = {v: k for k, v in {'Healthy': 0, 'Powdery Mildew': 1}.items()}
        pred_class = target_map[pred_proba > 0.5]
        if pred_class == 'Healthy':
            pred_proba = 1 - pred_proba

        leaf_condition = 'has powdery mildew' if pred_class.lower() == 'powdery mildew' else 'is healthy'
        st.write(f"The leaf condition is: {leaf_condition}")

        return pred_proba, pred_class

    except Exception as e:
        st.error(f"Error during prediction: {e}")
        raise RuntimeError(f"Error during prediction: {e}")
