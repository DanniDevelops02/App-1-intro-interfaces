import streamlit as st
from PIL import Image

st.title("Hola!!! mi Nombre es Danniboy")

st.header("En este espacio cmoienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open("sergey-kolesov-mermaid-sharpen.jpg")
st.image(image, caption = "interfaces multimodales")


