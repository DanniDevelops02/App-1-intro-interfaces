import streamlit as st

# 1. Configuración de la página en formato de columna única centrada
st.set_page_config(layout="centered", page_title="Interfaces Multimodales")

# 2. HTML y CSS del Banner Parallax 
banner_html = """
<style>
.block-container {
    padding-top: 2rem !important; 
}
.parallax {
    background-image: url("https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2F04dc6a81d4228b64d99b9f8f8f42ac16db790c75-1920x1080.jpg&w=3840&q=75");
    min-height: 300px; 
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 2rem;
    border-radius: 16px;
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

# ---------------------------------------------------------
# NUEVO: 3. Inyección del sistema de audios y desbloqueo
# ---------------------------------------------------------
audio_system_html = """
<!-- Etiquetas de audio ocultas -->
<audio id="audio_bienvenida" src="bienvenida.mp3" preload="auto"></audio>
<audio id="audio_instruccion" src="instruccion.mp3" preload="auto"></audio>
<audio id="audio_nota" src="nota.mp3" preload="auto"></audio>

<!-- Botón de inicialización y Script de desbloqueo -->
<div id="audio-unlocker" style="text-align: center; margin-bottom: 20px; padding: 20px; background-color: #2e2e38; border-radius: 8px;">
    <p style="margin-bottom: 10px; color: white;">Para habilitar la experiencia auditiva, debes inicializar el sistema.</p>
    <button onclick="unlockAudio()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; background-color: #4F46E5; color: white; border: none; border-radius: 5px;">
        Activar Experiencia Auditiva 🔊
    </button>
</div>

<script>
    // Función que se ejecuta con el primer clic del usuario
    function unlockAudio() {
        // Obtenemos todos los elementos de audio
        var audios = document.getElementsByTagName('audio');
        
        // El truco de desbloqueo: reproducir y pausar inmediatamente cada audio
        // Esto le dice al navegador "el usuario solicitó usar el audio"
        for (var i = 0; i < audios.length; i++) {
            audios[i].play().then(function() {
                // Si la promesa se cumple (se permitió reproducir), lo pausamos al instante
                for (var j = 0; j < audios.length; j++) {
                     audios[j].pause();
                     audios[j].currentTime = 0;
                }
            }).catch(function(error) {
                console.log("Error al desbloquear audio:", error);
            });
        }
        
        // Ocultamos el botón porque ya no es necesario
        document.getElementById('audio-unlocker').style.display = 'none';
    }
</script>
"""
st.markdown(audio_system_html, unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. Textos de instrucción interactivos
# Reemplazamos st.markdown por HTML inyectado para poder 
# agregar el atributo 'onmouseover' de JavaScript
# ---------------------------------------------------------
textos_interactivos_html = """
<div class="contenedor-interactivo">
    <!-- El evento onmouseover busca el ID del audio y le da play -->
    <h3 onmouseover="document.getElementById('audio_bienvenida').play()">
        Mi nombre es Daniel Flórez, esta es nuestra primera aplicación dónde exploraremos los distintos tipos de interacción.
    </h3>
    
    <p onmouseover="document.getElementById('audio_instruccion').play()">
        Selecciona una de las opciones a continuación para experimentar cómo cambia la interfaz según la modalidad.
    </p>
</div>
"""
st.markdown(textos_interactivos_html, unsafe_allow_html=True)

st.markdown("---")

# 5. Radio buttons verticales (se eliminó horizontal=True)
modo = st.radio(
    "Selecciona la modalidad principal:",
    ("Visual", "Auditiva", "Háptica")
)

# 6. Lógica de las modalidades
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
    .block-container p,
    .block-container h1,
    .block-container h2,
    .block-container h3,
    .block-container h4,
    .block-container h5,
    .block-container h6,
    .block-container li,
    .contenedor-interactivo h3,
    .contenedor-interactivo p {
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
    
    /* 3. Revelar el texto suavemente al pasar el cursor */
    .block-container p:hover,
    .block-container h1:hover,
    .block-container h2:hover,
    .block-container h3:hover,
    .block-container h4:hover,
    .block-container h5:hover,
    .block-container h6:hover,
    .block-container li:hover,
    .contenedor-interactivo h3:hover,
    .contenedor-interactivo p:hover {
        opacity: 1 !important;
    }
    
    /* 4. EXCEPCIÓN VITAL: Proteger el widget de selección (Radio buttons) */
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
    
    # ---------------------------------------------------------
    # NUEVO: Aplicamos la misma lógica interactiva a los textos ocultos
    # ---------------------------------------------------------
    textos_ocultos_html = """
    <div>
        <p onmouseover="document.getElementById('audio_nota').play()">
            Modo Auditivo activado. Explora la pantalla con el cursor para descubrir el contenido oculto.
        </p>
    </div>
    """
    st.markdown(textos_ocultos_html, unsafe_allow_html=True)

elif modo == "Háptica":
    st.write("Modo Háptico seleccionado (Configuración pendiente para el próximo paso).")
