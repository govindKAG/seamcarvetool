from PIL import Image

import numpy as np
import seam_carving
import streamlit as st

src = np.array(Image.open('./img2.jpg'))

src_h, src_w, _ = src.shape
delta = st.slider('adjust the width', -src_w, 0, 5)
dst = seam_carving.resize(src, (
    src_w + delta,
    src_h
), energy_mode='backward', order='width-first', keep_mask=None)
morphed = Image.fromarray(dst)
st.image([src,morphed])
