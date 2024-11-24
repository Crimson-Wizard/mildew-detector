import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities,
)


def page_mildew_detector_body():
    """
    Page for detecting mildew in cherry leaf samples.
    This function defines the main interface for the mildew detector.
    """

    st.info(
        "The client is interested in predicting if a cherry "
        "tree is healthy or contains powdery mildew."
    )

    st.write(
        "* You can download a set of healthy and "
        "powdery mildew leaves for live prediction. "
        "You can download the images from "
        "[here](https://www.kaggle.com/codeinstitute/cherry-leaves)."
    )

    st.write("---")

    # File uploader for multiple images
    images_buffer = st.file_uploader(
        'Upload cherry leaf samples. You may select more than one.',
        type=['png', 'jpg', 'jpeg'],
        accept_multiple_files=True,
    )

    # Initialize results as a list
    results = []

    if images_buffer:
        for image in images_buffer:
            try:
                # Load and display the image
                img_pil = Image.open(image)
                st.info(f"Cherry Leaf sample **{image.name}**")
                img_array = np.array(img_pil)
                st.image(
                        img_pil,
                        caption=(
                            f"Image Size: {img_array.shape[1]}px width x "
                            f"{img_array.shape[0]}px height"
                        ),
                    )

                # Process the image and make predictions
                resized_img = resize_input_image(img=img_pil)
                pred_proba, pred_class = load_model_and_predict(resized_img)
                plot_predictions_probabilities(pred_proba, pred_class)

                # Append results to the list
                results.append({"Name": image.name, "Result": pred_class})

            except Exception as e:
                st.error(f"Error processing file {image.name}: {e}")

        # Convert results to a DataFrame and display
        if results:
            df_report = pd.DataFrame(results)
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(
                download_dataframe_as_csv(df_report),
                unsafe_allow_html=True,
            )
