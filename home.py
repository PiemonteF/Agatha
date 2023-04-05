import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image



image = Image.open('higia.png')
col1, col2, col3 = st.columns(3)

with col2:
    st.image(image, width=200)