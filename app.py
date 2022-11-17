import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_cleaning import clean_input_image

st.title("Lemon Image Cleaning Helper")

st.write(
        f"* Upload lemon images here for data cleaning and save "
        f"them to your machine to use in the main application."
        )

st.write("---")

images_buffer = st.file_uploader('Upload lemon images. You may select more than one.',
                                        type=['png', 'jpg'],accept_multiple_files=True)
   
if images_buffer is not None:
    df_report = pd.DataFrame([])
    for image in images_buffer:

        img_pil = (Image.open(image)).convert('RGB')
        st.info(f"Lemon Image: **{image.name}**")
        img_array = np.array(img_pil)
        st.image(img_pil, caption=f"Original image - Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")
        cleaned_img = clean_input_image(img=img_pil)
        cleaned_array = np.array(cleaned_img)
        st.image(cleaned_img, caption=f"Cleaned image - Image Size: {cleaned_array.shape[1]}px width x {cleaned_array.shape[0]}px height")

    
app.run()