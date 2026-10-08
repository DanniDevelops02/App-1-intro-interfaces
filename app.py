import streamlit as st

# 1. Configuración de la página en formato de columna única centrada
st.set_page_config(layout="centered", page_title="Interfaces Multimodales")

# 2. HTML y CSS del Banner Parallax (ahora adaptado a la columna centrada)
banner_html = """
<style>
.block-container {
    padding-top: 2rem !important; /* Añade un poco de aire superior */
}

.parallax {
    /* Reemplaza esta URL por tu imagen */
    background-image: url("https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=2000&auto=format&fit=crop");
    min-height: 300px; 
    
    /* Efecto Parallax */
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    
    display: flex;
    align-items: center;
    justify-content: center;
    
    /* Ajustes para columna centrada */
    margin-bottom: 2rem;
    border-radius: 16px;
    
    /* Transición suave para cuando se active el filtro blanco y negro */
    transition: filter 0.5s ease;
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
    font-size: 2.5rem;
    transition: color 0.3s ease;
}
</style>

<div class="parallax">
    <div class="parallax-content">
        <h1>Introducción a interfaces multimodales</h1>
    </div>
</div>
"""
st.markdown(banner_html, unsafe_allow_html=True)

# 3. Textos de instrucción (Ahora sí se ocultarán en modo auditivo)
st.markdown("### Mi nombre es Daniel Flórez. Esta es nuestra primera aplicación y exploraremos los distintos tipos de interacción.")
st.write("Selecciona una de las opciones a continuación para experimentar cómo cambia la interfaz según la modalidad.")

st.markdown("---")

# 4. Radio buttons verticales (se eliminó horizontal=True)
modo = st.radio(
    "Selecciona la modalidad principal:",
    ("Visual - Modo estandar de interacción", "Auditiva - Explora la pantalla con el cursor para descubrir el contenido oculto.", "Háptica - Modo de interacción con feedback fisico")
)

# 5. Lógica de las modalidades
if modo == "Visual":
    st.info("Modo Visual activado: Esta es la experiencia de usuario estándar.")

elif modo == "Auditiva":
    # CSS dinámico inyectado solo cuando se selecciona "Auditiva"
    auditiva_css = """
    <style>
    /* 1. Filtro blanco y negro para el banner (desaturación visual) */
    .parallax {
        filter: grayscale(100%);
    }
    
    /* Ocultar el recuadro y título del banner hasta hacer hover sobre él */
    .parallax-content {
        background-color: transparent !important;
        transition: background-color 0.4s ease;
    }
    .parallax-content h1 {
        opacity: 0 !important;
        transition: opacity 0.4s ease;
    }
    .parallax:hover .parallax-content {
        background-color: rgba(0, 0, 0, 0.7) !important;
    }
    .parallax:hover .parallax-content h1 {
        opacity: 1 !important;
        color: white !important;
    }
    
    /* 2. Ocultar los textos camuflándolos con el fondo */
    /* Al usar opacity: 0, los textos son 100% invisibles y toman automáticamente el color exacto */
    /* del fondo, funcionando a la perfección tanto en Modo Claro como en Modo Oscuro de Streamlit */
    .block-container p,
    .block-container h1,
    .block-container h2,
    .block-container h3,
    .block-container h4,
    .block-container h5,
    .block-container h6,
    .block-container li {
        opacity: 0 !important;
        transition: opacity 0.3s ease-in-out;
    }
    
    /* Atenuar también las líneas divisorias */
    .block-container hr {
        opacity: 0.1 !important;
        transition: opacity 0.3s ease-in-out;
    }
    .block-container hr:hover {
        opacity: 1 !important;
    }
    
    /* 3. Revelar el texto suavemente al pasar el cursor (hover para exploración auditiva) */
    .block-container p:hover,
    .block-container h1:hover,
    .block-container h2:hover,
    .block-container h3:hover,
    .block-container h4:hover,
    .block-container h5:hover,
    .block-container h6:hover,
    .block-container li:hover {
        opacity: 1 !important;
    }
    
    /* 4. EXCEPCIÓN VITAL: Proteger el widget de selección (Radio buttons) */
    /* Con mayor especificidad garantizamos que las opciones siempre permanezcan visibles y legibles */
    div[data-testid="stRadio"] p,
    div[data-testid="stRadio"] label,
    div[data-testid="stRadio"] span,
    div[data-testid="stRadio"] div,
    .stRadio p,
    .stRadio label,
    .stRadio span,
    .stRadio div {
        opacity: 1 !important;
        visibility: visible !important;
    }
    </style>
    """
    st.markdown(auditiva_css, unsafe_allow_html=True)
    
    # Textos de prueba que sí se ocultarán
    st.write("Modo Auditivo activado. Explora la pantalla con el cursor para descubrir el contenido oculto.")
    st.write("*(Nota: El backend de audio se gestionará en un script local)*")

elif modo == "Háptica":
    st.write("Modo Háptico seleccionado (Configuración pendiente para el próximo paso).")
