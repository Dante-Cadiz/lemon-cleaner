import streamlit as st
import numpy as np
from rembg import remove
from PIL import Image


def clean_input_image(img: np.ndarray) -> np.ndarray:  
    """
    Removes background of image using Rembg, gets bounding box
    of foreground element and crops image to bounding box dimensions.
    Returns image array.
    """
    removed = remove(img)
    imageBox = removed.getbbox()
    cropped = removed.crop(imageBox)
    to_rgb = cropped.convert('RGB')
    my_image = np.expand_dims(to_rgb, axis=0)/255

    return my_image