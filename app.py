import streamlit as st
from PIL import Image

st.title("Hola!!! mi Nombre es Danniboy")

st.header("En este espacio comenzare a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open("sergey-kolesov-mermaid-sharpen.jpg")
st.image(image, caption = "interfaces multimodales")


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es: ', texto)

col1, col2 = st.columns(2)

with col1:
  st.subheader('Esta es la primera columna')
  st.write('Las interfaces multimodales mejoran la experiencia de usuario')
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('correcto!')

with col2:
  st.subheader('Esta es la segunda columna')
  modo = st.radio ('Que mmodalidad es la principal en tu interfaz?' , ('Visual', 'Auditiva', 'Tactil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'Auditiva':
    st.write('El audio es fundamental para tu interfaz')
  if modo == 'Tactil':
    st.write('El tacto es fundamental para tu interfaz')

st.subheader('Uso de botones')
if st.button('Presiona el boton'):
  st.write('Gracias por presionar')
else:
  st.write('No has presionado aun')
