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
        f"The client is interested in predicting if a cherry tree is healthy or contains powdery mildew."
        )

    st.write(
        f"* You can download a set of healthy and powdery mildew leaves for live prediction. "
        f"You can download the images from [here](https://www.kaggle.com/codeinstitute/cherry-leaves)."
        )

    st.write("---")
    # file uploader for multiple images
    images_buffer = st.file_uploader('Upload cherry leaf samples. You may select more than one.',
                                        type=['png', 'jpg', 'jpeg'],accept_multiple_files=True)

    if images_buffer is not None:
        report_data = []
        version = "v1" 
        for image in images_buffer:
            try:
                img_pil = (Image.open(image))
                img_array = np.array(img_pil)
                st.info(f"Cherry leaf smaple: **{image.name}**")
                st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")
                resized_img = resize_input_image(img=img_pil)
                pred_proba, pred_class = load_model_and_predict(resized_img)
                plot_predictions_probabilities(pred_proba, pred_class)
                
                report_data.append({"Name":image.name, 'Result': pred_class })
                
            except Exception as e:
                st.error(f"Error processing {image.name}: {e}")

        #create dataframe from collected data
        df_report = pd.DataFrame(report_data)

        if not df_report.empty:
            #display report
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)