import streamlit as st

# 1. Configuración de la página en formato ancho
st.set_page_config(layout="wide", page_title="Interfaces Multimodales")

# 2. CSS y HTML para el Banner Parallax
banner_html = """
<style>
/* Forzamos que el contenedor principal no tenga padding superior para que el banner toque el borde */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
}

.parallax {
    /* Reemplaza esta URL por la imagen de fondo que prefieras */
    background-image: url("https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=2000&auto=format&fit=crop");
    
    /* Altura del banner */
    min-height: 400px; 
    
    /* Efecto Parallax */
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    
    /* Centrado del contenido */
    display: flex;
    align-items: center;
    justify-content: center;
    
    /* Márgenes negativos para expandir de lado a lado en Streamlit */
    margin-left: -5rem;
    margin-right: -5rem;
    margin-bottom: 2rem;
}

.parallax-content {
    background-color: rgba(0, 0, 0, 0.6);
    padding: 20px 40px;
    border-radius: 12px;
    text-align: center;
}

.parallax-content h1 {
    color: white !important;
    margin: 0;
    font-size: 3rem;
}
</style>

<div class="parallax">
    <div class="parallax-content">
        <h1>Introducción a interfaces multimodales</h1>
    </div>
</div>
"""
st.markdown(banner_html, unsafe_allow_html=True)

# 3. Descripción de la aplicación
st.markdown("### Esta es nuestra primera aplicación y exploraremos los distintos tipos de interacción.")
st.write("Selecciona una de las opciones a continuación para experimentar cómo cambia la interfaz según la modalidad.")

# 4. Sección de Radio Buttons para las modalidades
st.markdown("---")
modo = st.radio(
    "Selecciona la modalidad principal:",
    ("Visual", "Auditiva", "Háptica"),
    horizontal=True
)

# 5. Lógica de las modalidades
if modo == "Visual":
    st.info("Modo Visual activado: Esta es la experiencia de usuario estándar.")

elif modo == "Auditiva":
    # CSS dinámico para el modo auditivo
    auditiva_css = """
    <style>
    /* Cambiar el color de fondo de toda la aplicación */
    .stApp {
        background-color: #363637 !important;
    }
    
    /* Ocultar el texto camuflándolo con el fondo */
    p, h1, h2, h3, h4, h5, h6, li, label, .stMarkdown {
        color: #363637 !important;
        transition: color 0.3s ease-in-out;
    }
    
    /* Revelar el texto en blanco suave al hacer hover */
    p:hover, h1:hover, h2:hover, h3:hover, h4:hover, h5:hover, h6:hover, li:hover, label:hover {
        color: #cecece !important;
    }
    
    /* Asegurar que los componentes de input mantengan visibilidad básica para poder regresar */
    .stRadio div[role="radiogroup"] {
        background-color: transparent !important;
    }
    </style>
    """
    st.markdown(auditiva_css, unsafe_allow_html=True)
    
    st.write("Modo Auditivo activado. Explora la pantalla con el cursor para descubrir el contenido.")
    st.write("*(Nota: La reproducción de audio al hacer hover se integrará posteriormente)*")

elif modo == "Háptica":
    st.write("Modo Háptico seleccionado (Configuración pendiente para el próximo paso).")
