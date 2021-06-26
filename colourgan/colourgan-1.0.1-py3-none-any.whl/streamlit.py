'''Interactive Testing Flask app for Model.'''
from colourgan.model import ColourGAN
from colourgan.config import get_cfg
import streamlit as st
from PIL import Image
import numpy as np

def app(weights):
    cfg = get_cfg()
    cfg.initial_weights_generator = weights
    model = ColourGAN(cfg, inference=True)

    st.title('ganapps ')
    st.write('\n')

    st.write("""
    ## ColourGAN Web Application
    """)
    uploaded_file = st.file_uploader("text here", type="png")
    if uploaded_file is not None:
        col1, col2 = st.beta_columns(2)
        image = Image.open(uploaded_file)
        col1.image(image, caption='Uploaded Image.',width = 32, use_column_width=True)
        new_img = model.inference(np.array(image))
        col2.image(new_img, caption='Coloured Image.', use_column_width=True)

    st.write("""
    [GitHub Repository](https://github.com/narenderkumarnain/GAN-Apps)
    """)








