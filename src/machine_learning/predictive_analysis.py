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
    """
    Reshape image to average image size
    """
    try:
        image_shape = load_pkl_file(file_path=f"outputs/v2/image_shape.pk1")
        #resize image
        img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
        my_image = np.expand_dims(img_resized, axis=0)/255

        return my_image
    except Exception as e:
        raise ValueError(f"Error resizing image: {e}")


def load_model_and_predict(my_image):
    """
    Load and perform ML prediction over live images
    """
    try:
        #debuging
        #tensoreflow version
        st.write(f"TensorFlow version: {tf.__version__}")
        #do image shapes match 
        st.write(f"Model expected input shape: {model.input_shape}")
        st.write(f"Resized image shape: {my_image.shape}")
        
        model = load_model('path_to_save/saved_model')

        pred_proba = model.predict(my_image)[0, 0]

        target_map = {v: k for k, v in {'Healthy': 0, 'Powdery Mildew': 1}.items()}
        pred_class = target_map[pred_proba > 0.5]
        if pred_class == 'Healthy':
            pred_proba = 1 - pred_proba
            
        leaf_condition = 'has powdery mildew' if pred_class.lower() == 'powdery mildew' else 'is healthy'

        st.write(
            f"The predictive analysis indicates the sample leaf"
            f" **{leaf_condition}**.")

        return pred_proba, pred_class
    except Exception as e:
        raise RuntimeError(f"Error during prediction: {e}")
    