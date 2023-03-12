import numpy as np
import streamlit as st
from PIL import Image

from MachineLearninginComputerVision import demo

st.set_page_config(layout="wide")
st.title("YOLOv3-nano Demo")
st.write(
    "This web app demonstrates the YOLOv3-nano model "
    "that detects objects and classifies them "
    "to 10 different classes."
)

file_upload = st.file_uploader("Upload the image", type=["jpeg", "jpg", "png"])
col_1, col_2 = st.columns(2)

if file_upload is not None:
    img = Image.open(file_upload)
    col_1.image(img, "Original image")
    array_img = np.array(img)
    result = demo.main(show=False, file_img=array_img)
    col_2.image(result, "Resulted image")
