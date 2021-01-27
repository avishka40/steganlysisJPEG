
import streamlit as st 
from PIL import Image
from classify import predict


st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = predict(uploaded_file)
    st.write(label)
    st.write(label[:,0])
    #st.write('%s (%.2f%%)' % (label[0], label[0]*100))