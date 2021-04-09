from PIL import Image

import numpy as np
import seam_carving
import streamlit as st

size = (512,512)
og   = Image.open('./img.jpg')
og.thumbnail(size, Image.ANTIALIAS)

src  = np.array(og)
print(src)

st.image(src)
src_h, src_w, _ = src.shape
delta = st.slider('adjust the width', -src_w, 0, 0)
dst = seam_carving.resize(src, (
    src_w + delta,
    src_h
), energy_mode='backward', order='width-first', keep_mask=None)
morphed = Image.fromarray(dst)
st.write("After:")
st.image(morphed)
