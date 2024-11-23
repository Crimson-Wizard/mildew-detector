import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)


def page_mildew_detector_body():
    st.info(
        f"The client is interested in predicting if a cherry"
        f"tree is healthy or contains powdery mildew."
    )

    st.write(
        f"* You can download a set of healthy and"
        f"powdery mildew leaves for live prediction. "
        f"You can download the images from "
        f"[here](https://www.kaggle.com/codeinstitute/cherry-leaves)."
    )

    st.write("---")
    # file uploader for multiple images
    images_buffer = st.file_uploader(
        'Upload cherry leaf samples. You may select more than one.', type=[
            'png', 'jpg', 'jpeg'], accept_multiple_files=True)

    results = []
    for image in images_buffer:
        img_pil = (Image.open(image))
        st.info(f"Cherry Leaf sample **{image.name}**")
        img_array = np.array(img_pil)
        st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

        resized_img = resize_input_image(img=img_pil)
        pred_proba, pred_class = load_model_and_predict(resized_img)
        plot_predictions_probabilities(pred_proba, pred_class)

        results.append({"Name": image.name, "Result": pred_class})

    # Convert results to DataFrame
    df_report = pd.DataFrame(results)