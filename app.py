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
st.markdown("### Esta es nuestra primera aplicación y exploraremos los distintos tipos de interacción.")
st.write("Selecciona una de las opciones a continuación para experimentar cómo cambia la interfaz según la modalidad.")

st.markdown("---")

# 4. Radio buttons verticales (se eliminó horizontal=True)
modo = st.radio(
    "Selecciona la modalidad principal:",
    ("Visual", "Auditiva", "Háptica")
)

# 5. Lógica de las modalidades
if modo == "Visual":
    st.info("Modo Visual activado: Esta es la experiencia de usuario estándar.")

elif modo == "Auditiva":
    # CSS dinámico inyectado solo cuando se selecciona "Auditiva"
    auditiva_css = """
    <style>
    /* 1. Aplicar filtro blanco y negro a la imagen del banner */
    .parallax {
        filter: grayscale(100%);
    }
    
    /* 2. Ocultar textos camuflándolos con el color de fondo */
    p, h1, h2, h3, h4, h5, h6, li, .stMarkdown, .stInfo {
        /* Se adapta automáticamente al modo oscuro o claro del usuario */
        color: var(--background-color) !important;
        background-color: transparent !important;
        border-color: transparent !important;
        transition: color 0.3s ease-in-out;
    }
    
    /* El H1 del banner requiere ser transparente para no verse como un bloque sólido sobre la foto */
    .parallax-content h1 {
        color: transparent !important;
    }
    
    /* 3. Revelar el texto al hacer hover */
    p:hover, h1:hover, h2:hover, h3:hover, h4:hover, h5:hover, h6:hover, li:hover, .stInfo:hover {
        /* Vuelve al color nativo de Streamlit (blanco en oscuro, negro en claro) */
        color: var(--text-color) !important;
    }
    .parallax-content h1:hover {
        color: white !important; /* El banner siempre revela texto blanco */
    }
    
    /* 4. EXCEPCIONES: Proteger los elementos que no deben desaparecer */
    
    
    /* El widget de los Radio Buttons */
    .stRadio, .stRadio p, .stRadio label, .stRadio div {
        color: var(--text-color) !important;
    }
    </style>
    """
    st.markdown(auditiva_css, unsafe_allow_html=True)
    
    # Textos de prueba que sí se ocultarán
    st.write("Modo Auditivo activado. Explora la pantalla con el cursor para descubrir el contenido oculto.")
    st.write("*(Nota: El backend de audio se gestionará en un script local)*")

elif modo == "Háptica":
    st.write("Modo Háptico seleccionado (Configuración pendiente para el próximo paso).")
