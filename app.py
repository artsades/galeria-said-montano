# SECCIÓN 1: CONFIGURACIÓN, RECURSOS Y SEO DINÁMICO
# -----------------------------------------------------------------
import streamlit as st
import pandas as pd
import os
import re
import base64
import requests
from bs4 import BeautifulSoup
import streamlit.components.v1 as components
import textwrap
# --- CONFIGURACIÓN DE CARGA ---
if 'obras_visibles' not in st.session_state:
    st.session_state.obras_visibles = 8

# --- FUNCIÓN DE SEO DINÁMICO (ÓLEO Y ACUARELA) ---
def obtener_seo_estudio():
    # Tus bases sólidas para México y USA
    keywords = [
        "Said Montaño", "Oil paintings for sale USA", "Pintura al óleo México", 
        "Acuarelas originales", "Fine art watercolors", "Shipping worldwide Skydropx",
        "Contemporary art Mexico", "Comprar arte original"
    ]
    try:
        # Intentamos captar tendencias de arte actuales para refrescar el SEO
        res = requests.get("https://www.saatchiart.com/art/Painting/Realism/", timeout=2)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            tendencias = [tag.text.strip() for tag in soup.find_all('h3')[:3]]
            keywords.extend(tendencias)
    except:
        pass 
    return ", ".join(keywords)

# Ejecutamos el motor de SEO
SEO_DINAMICO = obtener_seo_estudio()

st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">', unsafe_allow_html=True)

# --- BÓVEDA SEO ACTUALIZADA ---
PALABRAS_SEO = f"{SEO_DINAMICO}, Said Montaño artista, realismo figurativo, arte oscuro, envíos seguros a USA y México."
# Título dinámico para la pestaña del navegador
t_pestana = st.session_state.get('tec_ref', 'ARCHIVO VISUAL')
# Crear un ancla invisible en la parte superior
st.markdown('<div id="subir"></div>', unsafe_allow_html=True)

# --- CARGA DEL FAVICON (VERSIÓN RASTREADOR) ---
def get_favicon_final():
    # Buscamos en la carpeta static
    folder = "static"
    if os.path.exists(folder):
        for archivo in os.listdir(folder):
            # Si el archivo empieza con 'fav' y es imagen, lo usamos
            if archivo.lower().startswith("fav") and archivo.lower().endswith((".png", ".jpg", ".jpeg", ".ico")):
                path_fav = os.path.join(folder, archivo)
                with open(path_fav, "rb") as f:
                    return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    return "https://saidmontano.art/static/logo_said_montano.png" # Plan C: Tu logo de la web

fav_icon_data = get_favicon_final()

st.set_page_config(
    page_title=f"Said Montaño | {t_pestana} | Fine Art Shipping USA & MX", 
    page_icon=fav_icon_data, 
    layout="wide", 
    initial_sidebar_state="collapsed"
)
# Inyección SEO (Sin generar espacios ni líneas negras)
st.markdown(f'<div style="display:none; height:0; width:0; overflow:hidden; visibility:hidden;">{PALABRAS_SEO}</div>', unsafe_allow_html=True)

# --- MEMORIA DE NAVEGACIÓN (SIMPLE Y LIMPIA) ---
# Leemos directamente si hay una obra seleccionada en la URL
obra_en_url = st.query_params.get("obra")

# Si el usuario cambió de técnica o dio "Ver más", limpiamos la selección
if st.session_state.get('limpiar_fantasma'):
    st.query_params.clear()
    obra_en_url = None
    st.session_state.limpiar_fantasma = False

###=====ESTO SE QUEDA COMO ESTÁ=####
if "p" in st.query_params:
    st.session_state.pag_ref = int(st.query_params["p"])
elif 'pag_ref' not in st.session_state:
    st.session_state.pag_ref = 0

if "t" in st.query_params:
    st.session_state.tec_ref = st.query_params["t"]
elif 'tec_ref' not in st.session_state:
    st.session_state.tec_ref = "ACUARELA" # <--- Aprovechamos para poner Acuarela primero CAMBIA CUANDO QUIERAS
def image_to_base64(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    return ""

# 1.1 CARGA DE PNGS (LOGO E ICONOS)
logo_main_b64 = image_to_base64("static/logo_said_montano.png")
icon_wa_b64 = image_to_base64("static/logo_whatsapp.png")
icon_ig_b64 = image_to_base64("static/logo_instagram.png")
icon_tk_b64 = image_to_base64("static/logo_tiktok.png")

# SECCIÓN 2: ADN VISUAL (CSS INDUSTRIAL)
# -----------------------------------------------------------------
st.markdown(f"""
    <style>
    /* SEO INDEX: {PALABRAS_SEO} */

    @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap');
    
    /* 2.1 BASE Y FONDO */
    .stAppHeader {{ display: none !important; }}
    .stApp {{ background-color: #ffffff; }}
    .block-container {{ 
    padding: 0 50px !important; 
    padding-top: 0.5rem !important; 
    margin-top: -180px !important; 
}}

    /* 2.1 BARRA ADN VISUAL (CON EFECTO BREATHE) */
    @keyframes adn-breathe {{
        0%   {{ opacity: 1; }}
        50%  {{ opacity: 0.4; }} 
        100% {{ opacity: 1; }}
    }}

    .banner-envios {{
        background-color: #949494; 
        color: #ffffff !important; 
        font-family: 'Courier Prime', monospace;
        font-size: 0.8rem;
        text-align: center;
        padding: 2px 0;
        letter-spacing: 6px;
        width: 100vw;
        margin-left: calc(-50vw + 50%);
        margin-top: 50px !important;  /* SUBE EL BANNER DE ENVIOS */
        margin-bottom: 0px !important;
        animation: adn-breathe 2s ease-in-out infinite;
    }}

    /* 2.3 BUSCADOR */
    .stApp div[data-baseweb="input"], 
    .stApp div[data-baseweb="input"] > div {{
        background-color: #F0F0F0 !important;
        border-radius: 0px !important;
        border: none !important;
        border-bottom: 1px solid #E8E8E8 !important;
        height: 15px !important;
        min-height: 15px !important;
    }}
    
    .stApp div[data-baseweb="input"] input {{
        background-color: transparent !important;
        color: #000000 !important;
        -webkit-text-fill-color: #B3B3B3 !important; /* CAMBIA EL COLOR LETRAS BUSCADOR */
        font-family: 'Courier Prime' !important;
        font-size: 0.8rem !important;
        padding: 0px 10px !important;
        line-height: 32px !important;
    }}

    .stApp div[data-baseweb="input"] > div:focus-within {{
        border: 1px solid #000000 !important;
        box-shadow: none !important;
    }}

    /* 2.4 ICONOS Y LOGOS */
    .logo-firma {{ 
        filter: brightness(0) !important; 
        width: 180px !important;
    }}

    .icono-red-footer {{ 
        filter: brightness(0) !important; 
        width: 18px !important;
    }}

    /* 2.5 TEXTOS Y RADIO SECCION DE LAS TECNICAS BARRA*/
    .stRadio div[role="radiogroup"] label p {{ 
        color: #999999 !important;   /* COLOR DE LAS LETRAS SECCION TECNICAS */
        font-family: 'Courier Prime' !important;
        font-weight: bold !important;
    }}
    
    div[data-testid="stRadio"] {{
        width: 100% !important;
        margin-top: -50px !important; /* SEPARA EL BLOQUE DE LA SECCION DEL LOGO" */
        margin-bottom: 10px !important;  /* SEPARA EL BLOQUE DE LA SECCION DE "SOBRE EL ARTISTA" */
    }}

    div[data-testid="stRadio"] > div[role="radiogroup"] {{
        display: flex !important;
        flex-direction: row !important;
        justify-content: center !important; 
        align-items: center !important;
        gap: 2vw !important; 
        width: 100vw !important;
        max-width: 100vw !important;
        position: relative !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        z-index: 10 !important;
        background-color: #F2F2F2 !important; /* COLOR DE FONDO SECCION TECNICAS */
        padding: 1px 0px !important;
        border-radius: 0px !important;
    }}

    div[data-testid="stRadio"] label > div:first-of-type {{ display: none !important; }}
    
    div[data-testid="stRadio"] label p {{
        font-family: 'Courier Prime' !important;
        font-size: 0.8rem !important;   /* TAMAÑO DE LAS LETRAS SECCION TECNICAS */
        letter-spacing: 1px !important; /* ESPACIO DE LAS LETRAS SECCION TECNICAS */
        text-transform: uppercase;
        white-space: nowrap !important;
    }}

    div[data-testid="stRadio"] label:has(input:checked) p {{
        color: #B50095!important;  /* COLOR DE LAS LETRAS SECCION TECNICAS CUANDO LA SELECCIONAS */
        text-decoration: underline !important;
        text-underline-offset: 5px !important; /* ESPACIO DEL SUBRAYADO DE LAS LETRAS SECCION TECNICAS */
    }}
    /* 1. ANULAR VARIABLES DE MODO OSCURO DE STREAMLIT */
    :root {{
        --text-color: #000000 !important;
    }}

    /* Forzamos que cualquier párrafo dentro de la galería ignore el tema del sistema */
    [data-testid="stMarkdownContainer"] p, 
    [data-testid="stMarkdownContainer"] span {{
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }}

    /* Blindaje para que el navegador no intente invertir colores */
    .stApp {{
        color-scheme: light !important;
    }}
    /* 1. BOTONES ESTILO LIMPIO (SIN CONTORNO) */
    div.stButton > button {{
        background-color: #f0f0f0 !important;
        color: #000000 !important;
        border: none !important; /* <--- AQUÍ QUITAMOS EL CONTORNO */
        border-radius: 0px !important;
        font-family: 'Courier Prime', monospace !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        transition: background-color 0.3s ease !important;
    }}

    /* EFECTO HOVER SUTIL */
    div.stButton > button:hover {{
        background-color: #e0e0e0 !important; /* Un gris un poco más oscuro al pasar el mouse */
        color: #000000 !important;
    }}

    /* 2. FORZAR TEXTO NEGRO INCLUSO EN MODO OSCURO */
    div.stButton > button p {{
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }}

    /* Asegurar que el texto no cambie en hover si no queremos inversión */
    div.stButton > button:hover p {{
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }}
  /* 1. RESET TOTAL: El logo y nombre se quedan anclados donde van */
        .block-container {{
            padding-top: 3.5rem !important; 
        }}

        /* 2. SOLO CELULAR (AQUÍ OCURRE LA MAGIA) */
        @media (max-width: 768px) {{
            /* Quitamos el aire entre columnas solo en móvil */
            [data-testid="stHorizontalBlock"] {{
                gap: 0px !important;
            }}

            /* Succionamos el contenido de la columna hacia la línea técnica */
            [data-testid="stHorizontalBlock"] div[data-testid="column"] {{
                margin-top: -45px !important; 
            }}
            
            /* Mantenemos el aire del encabezado para que el logo no baile */
            [data-testid="stVerticalBlock"] {{
                gap: 1rem !important; 
            }}
        }}
    </style>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------
# INYECCIÓN DE RESPONSIVIDAD (SOLO CELULAR) - MOVIMIENTO FORZADO
# -----------------------------------------------------------------
st.markdown('''
<style>
    @media (max-width: 768px) {
        /* 1. CENTRAR LOGO */
        #contenedor-logo-said img {
            margin: 0 auto !important;
        }

        /* 2. MOVER ESTUDIO DE ARTE (Ajuste fino) */
        #texto-tecnico {
            position: relative !important;
            top: -5px !important;      /* Sube o baja el texto */
            left: -35px !important;    /* MUEVE A LA IZQUIERDA O DERECHA */
            width: 100vw !important;
            margin-left: -15px !important; /* Compensa el padding de Streamlit */
        }

        /* 3. SUBIR REDES SOCIALES (¡Aquí es donde las jalas!) */
        #redes-movil {
            position: relative !important;
            margin-top: -120px !important; /* ESTE VALOR NEGATIVO LAS SUBE */
            align-items: center !important;
            width: 100% !important;
        }
        
        #redes-movil div {
            justify-content: center !important;
        }
        
        #redes-movil .txt-redes {
            text-align: center !important;
            width: 100% !important;
        }
</style>
''', unsafe_allow_html=True)

# SECCIÓN 3: CABECERA (TU CÓDIGO SIGUE IGUAL ABAJO)
# -----------------------------------------------------------------
st.markdown('<div class="banner-envios">ENVÍOS NACIONALES E INTERNACIONALES - TRATO DIRECTO CON EL ARTISTA </div>', unsafe_allow_html=True)
#st.info("✨ **OFERTA DE COLECCIÓN:** Adquiere las 4 acuarelas originales de la serie *'Destellos del más allá'* por solo **$10,000 MXN**. Envío incluido.")

c1, c2, c3 = st.columns([1.2, 4, 1], gap="small") 

with c1:
    if logo_main_b64:
        st.markdown(f'''
            <div id="contenedor-logo-said" style="margin-top: 0px; padding-top: 0px;">
                <img src="data:image/png;base64,{logo_main_b64}" 
                     style="width: 250px; filter: brightness(0); display: block; margin: 0 auto;">
            </div>
        ''', unsafe_allow_html=True)

    # LE PUSIMOS EL ID "texto-tecnico"
    st.markdown("<p id='texto-tecnico' style='color:#000000; font-family:Courier Prime; font-size:0.6rem; font-weight:bold; margin-top: 0px; letter-spacing:1px; text-align:center;'>ESTUDIO DE ARTE / CDMX / 2026</p>", unsafe_allow_html=True)

# --- COLÓCALO ARRIBA DE LA SECCIÓN 4.0 ---
with c2:
    st.markdown("<div id='contenedor-buscador-said' style='margin-top: 55px;'>", unsafe_allow_html=True)
    # Usamos st.session_state para que el valor no se pierda al recargar
    busqueda_input = st.text_input("", placeholder="ESCRIBE PARA BUSCAR...", key="main_search").lower().strip()
    st.markdown("</div>", unsafe_allow_html=True)

with c3:
    msg_gral = "Hola Said, visité tu galería web...".replace(" ", "%20")
    # LE PUSIMOS EL ID "redes-movil"
    redes_html = f'''
    <div id="redes-movil" class="contenedor-redes" style="display: flex; flex-direction: column; align-items: flex-end; gap: 10px; margin-top: 52px;">
        <div style="display: flex; gap: 40px;">
            <a href="https://wa.me/5215610810026?text={msg_gral}" target="_blank"><img src="data:image/png;base64,{icon_wa_b64}" style="width:18px; filter:brightness(0);"></a>
            <a href="https://www.instagram.com/saidmontano_/" target="_blank"><img src="data:image/png;base64,{icon_ig_b64}" style="width:18px; filter:brightness(0);"></a>
            <a href="https://www.tiktok.com/@saidmaokh" target="_blank"><img src="data:image/png;base64,{icon_tk_b64}" style="width:18px; filter:brightness(0);"></a>
        </div>
        <span class="txt-redes" style="color:#000; font-family:Courier Prime; font-size:0.6rem; font-weight:bold; letter-spacing:1px; text-transform:uppercase;">CONTACTO</span>
    </div>
    '''
    st.markdown(redes_html, unsafe_allow_html=True)

# LÍNEA EXTRA DE SEGURIDAD
st.markdown("<br>", unsafe_allow_html=True)

# --- AJUSTES MILIMÉTRICOS (CAMBIA ESTOS VALORES) ---
SUBIR_TEXTO = "-80px"    # Lo subí más para que pegue con el banner [cite: 2026-03-02]
TAMANO_LETRA = "0.75rem" # Tamaño sutil tipo Le Labo [cite: 2026-02-27]
VELOCIDAD = "5s"         # Tiempo de escritura [cite: 2026-03-02]

# --- AJUSTES DE ESTÉTICA INDUSTRIAL (SAID MONTAÑO) ---
SUBIR_TEXTO = "-110px"    # Valor más agresivo para eliminar el hueco blanco [cite: 2026-03-02]
TAMANO_LETRA = "0.72rem"  # Tamaño técnico y minimalista estilo Le Labo [cite: 2026-02-27]
VELOCIDAD = "8s"          # Más lento para que el usuario pueda leer mientras se escribe [cite: 2026-03-02]



# 3.3 NAVEGACIÓN TÉCNICA (LIMPIEZA FINAL)
opciones = ["NUEVAS", "PINTURA AL OLEO", "ACUARELA", "DIBUJO", "ARTE DIGITAL", "ESCULTURA", "ESTUDIO"]
tecnica_actual = st.session_state.get('tec_ref', opciones[0])

botones_html = ""
for opcion in opciones:
    clase = "opcion-activa" if opcion == tecnica_actual else "opcion-inactiva"
    botones_html += f'<div class="{clase} nav-item" onclick="window.parent.postMessage({{type: \'streamlit:setComponentValue\', value: \'{opcion}\', key: \'hidden_nav\'}}, \'*\')">{opcion}</div>'

#:::::::::::::::::::::::::::::::::::::::::::::::::##
# 3.4 RECEPTOR FÍSICO (PERO INVISIBLE)
tecnica_sel = st.radio(
    "receptor_tecnica", # El nombre que busca el JS arriba
    options=opciones,
    key="hidden_nav",
    index=opciones.index(st.session_state.tec_ref) if st.session_state.tec_ref in opciones else 0,
    label_visibility="collapsed"
)

# Sincronización manual inmediata
if tecnica_sel != st.session_state.tec_ref:
    st.session_state.tec_ref = tecnica_sel
    st.session_state.obras_visibles = 8
    st.session_state.limpiar_fantasma = True # <--- AGREGA ESTA LÍNEA 
    st.rerun()
    
#:::::::::::::::::::::::::::::::::::::::::::::::::##

# --- 3.4 DESPLEGABLE CON FOTO (VERSIÓN CELULAR OPTIMIZADA) ---
import base64
import os
from pathlib import Path

def get_image_base64_ultimate():
    base_path = Path(r"C:\Users\SaidEmc\Desktop\ESTUDIO_SAID_ART")
    try:
        for archivo in os.listdir(base_path):
            if archivo.lower().startswith("said_perfil"):
                ruta_final = base_path / archivo
                with open(ruta_final, "rb") as f:
                    return base64.b64encode(f.read()).decode()
    except Exception:
        return None
    return None

foto_b64 = get_image_base64_ultimate()

st.markdown('''
    <style>
    /* 1. BARRA BLANCA TOTAL */
    .stExpander {
        border: none !important;
        background-color: #FFFFFF !important; 
        border-radius: 0px !important;
        margin-top: -45px !important; 
        width: 100vw !important;
        position: relative !important;
        left: 50% !important;
        margin-left: -50vw !important;
    }

    /* 2. TÍTULO CENTRADO */
    .stExpander summary {
        display: flex !important;
        justify-content: center !important;
    }
    .stExpander summary p {
        font-family: 'Courier Prime' !important;
        font-size: 0.6rem !important;
        letter-spacing: 2px;
        color: #000000 !important;
    }

    /* 3. CONTENEDOR DE LA BIO */
    [data-testid="stExpanderDetails"] {
        background-color: #F8F8F8 !important; 
        padding: 40px 0px !important; 
    }

    /* ESTILOS DE ESCRITORIO (PC) */
    .contenedor-foto {
        display: flex;
        justify-content: flex-end;
    }

    .foto-perfil {
        width: 160px;
        height: 160px;
        object-fit: cover;
        border: none;
    }

    .texto-bio-ajustado {
        color: #000000;
        font-family: 'Courier Prime', monospace;
        font-size: 0.8rem;
        text-align: left;
        line-height: 1.7;
        padding-right: 40px;
        padding-left: 0px; /* En PC va pegado a la foto */
    }

    /* --- AJUSTES EXCLUSIVOS PARA CELULAR --- */
    @media (max-width: 768px) {
        .contenedor-foto {
            justify-content: center !important;
            margin-bottom: 30px; /* Más espacio entre foto y texto */
        }
        .foto-perfil {
            width: 150px;
            height: 150px;
        }
        .texto-bio-ajustado {
            padding-left: 25px !important;  /* <--- EL ESPACIO QUE BUSCABAS */
            padding-right: 25px !important; /* Equilibrio en ambos lados */
            font-size: 0.85rem !important;   /* Un pelín más grande para legibilidad en móvil */
        }
    }
    </style>
''', unsafe_allow_html=True)

with st.expander("SOBRE EL ARTISTA"):
    col_foto, col_espacio, col_texto, col_final = st.columns([1.2, 0.1, 4, 1.2])
    
    with col_foto:
        foto_url = "https://raw.githubusercontent.com/artsades/galeria-said-montano/main/said_perfil.jpg"
        st.markdown(f'''
            <div class="contenedor-foto">
                <img src="{foto_url}" class="foto-perfil">
            </div>
        ''', unsafe_allow_html=True)
    
    with col_texto:
        # Usamos la nueva clase texto-bio-ajustado
        st.markdown("""
            <div class="texto-bio-ajustado">
                Said Montaño es un artista visual mexicano cuya práctica se centra principalmente en la pintura al óleo sobre lienzo. Su trabajo explora estados emocionales contenidos y tensiones psicológicas que operan de forma silenciosa y persistentente, construyendo escenas figurativas de alta carga simbólica. A través de una estética oscura, el cuerpo humano aparece fragmentado, intervenido o integrado dentro de estructuras que regulan identidad, control y pertenencia.
                <br><br>
                Paralelamente a su producción pictórica, el artista ha desarrollado una línea escultórica que mantiene el mismo lenguaje oscuro y personal, explorando la materialidad del cuerpo y sus restos como símbolos de permanencia, desgaste y memoria. Su trabajo escultórico ha sido seleccionado de manera consecutiva en cinco ediciones dentro de plataformas nacionales de exhibición, consolidando una identidad visual coherente en contextos de alta visibilidad sin diluir su discurso.
            </div>
        """, unsafe_allow_html=True)


    
# LÍNEA EXTRA DE SEGURIDAD PARA LA GALERÍA
st.write("")



#===SECCION DE LAS OBRAS FILTRADO DE TECNICAS =====
#=== SECCION DE LAS OBRAS FILTRADO DE TECNICAS =====
# 4.0 LECTURA Y CONTROL DE DATOS
archivos_csv = [f for f in os.listdir('.') if f.endswith('.csv')]

if archivos_csv:
    if 'datos_master' not in st.session_state:
        # En la Sección 4.0, asegúrate de que el bloque de error esté así:
        try:
            st.session_state.datos_master = pd.read_csv(archivos_csv[0], encoding='utf-8-sig')
        except:
            # El errors='replace' es el que evita que el celular se confunda
            st.session_state.datos_master = pd.read_csv(archivos_csv[0], encoding='latin-1', errors='replace')
        
        st.session_state.datos_master.columns = [c.lower().strip() for c in st.session_state.datos_master.columns]

    # 1. Copia de trabajo
    df_f = st.session_state.datos_master.copy()
    
    # 2. Definimos seccion_actual siempre
    seccion_actual = "proceso" if "ESTUDIO" in tecnica_sel.upper() else "galeria"
    
    # 3. Limpieza profunda (ESTO ARREGLA LOS ACENTOS EN PANTALLA)
    cols_check = ['titulo', 'tecnica', 'tags', 'descripcion', 'serie']
    for col in cols_check:
        if col in df_f.columns:
            # Forzamos la limpieza de texto para que no salgan símbolos raros
            df_f[col] = df_f[col].fillna('').astype(str).str.strip()
            # Creamos una versión en minúsculas solo para el buscador interno
        else:
            df_f[col] = ""

    # 4. LÓGICA DE BÚSQUEDA (Mantenemos la robusta que ya funcionaba)
    if busqueda_input:
        import re
        patron = r'\b' + re.escape(busqueda_input.lower())
        # Buscamos en minúsculas pero mostramos el texto original con acentos
        super_string = df_f[cols_check].apply(lambda x: ' '.join(x).lower(), axis=1)
        mask = super_string.str.contains(patron, regex=True, na=False)
        df_f = df_f[mask]
        titulo_seccion = f"RESULTADOS: {busqueda_input.upper()}"
    else:
        # Pestañas normales
        titulo_seccion = tecnica_sel
        # ... (aquí sigue tu código de filtrado por seccion_actual y MAPEO_DATOS)

    # 3. Aplicamos la búsqueda global (FLEXIBLE Y ROBUSTA)
    # 3. Aplicamos la búsqueda global (FLEXIBLE Y ROBUSTA)
    if busqueda_input:
        import re
        patron = r'\b' + re.escape(busqueda_input.lower())
        
        # Validamos que df_f no esté vacío antes de procesar
        if not df_f.empty:
            # Unimos las columnas clave
            super_string = df_f[cols_check].astype(str).apply(lambda x: ' '.join(x), axis=1).str.lower()
            
            # PROTECCIÓN: Si por alguna razón super_string no es una serie de strings, 
            # o si el filtro inicial vació el DF, validamos aquí:
            if not super_string.empty:
                mask = super_string.str.contains(patron, regex=True, na=False)
                df_f = df_f[mask]
        
        # Variable crítica para que el encabezado funcione
        titulo_seccion = f"RESULTADOS: {busqueda_input.upper()}"
        # --- MENSAJE DE BÚSQUEDA CON ANCLAJE SEGURO ---
        mensaje_html = ""
        if busqueda_input and df_f.empty:
            mensaje_html = f"""
                <div style="width: 100%; text-align: center; margin-top: 80px; margin-bottom: 80px; font-family: 'Courier Prime', monospace;">
                    <p style="font-size: 0.9rem; color: #000; letter-spacing: 2px; text-transform: uppercase; font-weight: bold;">
                        No se encontraron piezas para: <br>
                        <span style="color: #B50095; font-size: 1.1rem; border-bottom: 1px solid #B50095;">"{busqueda_input.upper()}"</span>
                    </p>
                </div>
            """

        # El secreto: siempre renderizamos un markdown, aunque esté vacío
        # Esto evita que React intente "remover" el componente y truene
        st.markdown(f'<div id="ancla-mensajes">{mensaje_html}</div>', unsafe_allow_html=True)
    else:
        # Pestañas normales
        titulo_seccion = tecnica_sel
        # ... resto de tu else (seccion_actual, MAPEO_DATOS, etc.)
        if 'seccion' in df_f.columns:
            df_f = df_f[df_f['seccion'] == seccion_actual]

        MAPEO_DATOS = {
            "NUEVAS": "OBRAS",
            "PINTURA AL OLEO": "pintura al oleo",
            "ACUARELA": "acuarela",
            "DIBUJO": "dibujo",
            "ARTE DIGITAL": "arte digital",
            "ESCULTURA": "escultura"
        }
        valor_csv = MAPEO_DATOS.get(tecnica_sel, "OBRAS")
        if valor_csv != "OBRAS" and seccion_actual != "proceso":
            df_f = df_f[df_f['tecnica'].str.contains(valor_csv.lower())]

    # ESTA ES LA ASIGNACIÓN FINAL. NO DEBE HABER OTRA DESPUÉS.
    datos_galeria = df_f
    
    if not datos_galeria.empty:
        total_obras_tec = len(datos_galeria)
        obras_reales = min(st.session_state.obras_visibles, total_obras_tec)

        # 1. ENCABEZADO (Línea gris con contador)
        st.markdown(f"""
            <div style="
                display: flex; 
                justify-content: space-between; 
                align-items: flex-end; 
                border-bottom: 1px solid #eeeeee; 
                padding-bottom: 10px; 
                margin-top: -30px;  /* <--- Súbelo a -60px si es necesario */
                position: relative; 
                z-index: 10;
                background: white; 
                font-family: 'Courier Prime';
            ">
                <p style="margin: 0; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; color: #000;">{tecnica_sel}</p>
                <p style="margin: 0; font-size: 0.7rem; letter-spacing: 1px; color: #888;">MOSTRANDO {obras_reales} DE {total_obras_tec} OBRAS</p>
            </div>
        """, unsafe_allow_html=True)

        # 2. DEFINICIÓN DE LA FUNCIÓN (8 espacios de sangría)
        def mostrar_ficha_tecnica(id_ref, sufijo=""):
            # Refuerzo de scroll al inicio de la función
            st.components.v1.html("<script>window.parent.document.querySelector('section.main').scrollTo(0, 0);</script>", height=0)
            import textwrap
            import re
            
            # ESTO SUBE LA PÁGINA AUTOMÁTICAMENTE AL ABRIR
            st.markdown('<script>window.parent.document.querySelector(".main").scrollTo(0,0);</script>', unsafe_allow_html=True)
            
            try:
                r = datos_galeria[datos_galeria['id_unico'].astype(str).str.contains(str(id_ref))].iloc[0]
            except:
                return

            # --- NUEVA FUNCIÓN INTERNA DE LIMPIEZA PARA EL CELULAR ---
            def limpiar_txt(txt):
                t = str(txt)
                # DICCIONARIO PARA CARACTERES Y COMILLAS BASURA
                reemplazos = {
                    'Ã¡': 'á', 'Ã©': 'é', 'Ã­': 'í', 'Ã³': 'ó', 'Ãº': 'ú',
                    'Ã±': 'ñ', 'Ã': 'Á', 'Ã‰': 'É', 'Ã\xcd': 'Í', 'Ã“': 'Ó',
                    'Ãš': 'Ú', 'Ã‘': 'Ñ',
                    # --- ESTO ARREGLA LAS COMILLAS RARAS ---
                    'â€œ': '"', 'â€ ': '"', 'â€"': '-', 'â€¦': '...',
                    'â€': '"', 'â€˜': "'", 'â€™': "'"
                }
                for roto, sano in reemplazos.items():
                    t = t.replace(roto, sano)
                return t

            # --- APLICAMOS LA LIMPIEZA A LOS CAMPOS CRÍTICOS ---
            titulo_obra = limpiar_txt(r.get("titulo", "S/T"))
            descripcion_obra = limpiar_txt(r.get("descripcion", "Sin descripción."))
            tecnica_obra = limpiar_txt(r.get("tecnica", ""))

            # Preparación de links y precios
            val_p = str(r.get('precio', '0'))
            solo_n = re.sub(r'[^0-9.]', '', val_p)
            try: precio_f = f"${float(solo_n):,.0f} MXN"
            except: precio_f = "CONSULTAR PRECIO"
    
            # Nota que aquí ya usamos el titulo_obra que ya fue limpiado arriba
            link_paypal = f"https://www.paypal.me/Saidmc/{solo_n}MXN"
            msj_wa = f"Hola Said, me interesa la obra: {titulo_obra}".replace(" ", "%20")
            link_wa = f"https://wa.me/5215610810026?text={msj_wa}"
            # --- HACK DE SCROLL DEFINITIVO ---
            f_scroll = """
                <img src="x" onerror="
                    setTimeout(function() {
                        var mainContainer = window.parent.document.querySelector('section.main');
                        if (mainContainer) {
                            mainContainer.scrollTo({top: 0, behavior: 'auto'});
                        }
                    }, 50);
                " style="display:none;">
                <div id="top_anchor"></div>
            """
            # 1. BOTONES DE CIERRE (Superiores)
            _, col_cierre_btn = st.columns([0.85, 0.15])
            with col_cierre_btn:
                if st.button("CERRAR ✕", key=f"btn_cerrar_{id_ref}_{sufijo}"):
                    st.query_params.clear()
                    st.rerun()

            # 2. FICHA TÉCNICA Y BOTONES DE COMPRA (Lo primero que se ve)
            ficha_raw = f'''
                <div style="background-color:white; color:black; font-family:'Courier Prime',monospace; padding:20px; border:1px solid #eee; margin-bottom:40px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid black; padding-bottom:10px; margin-bottom:30px;">
                        <span style="font-size:0.7rem; letter-spacing:2px; color:black;">ARCHIVO VISUAL / DETALLES</span>
                        <img src="data:image/png;base64,{logo_main_b64}" style="width:120px; filter:brightness(0);">
                    </div>
                    <div style="display: flex; gap: 15px; margin-bottom: 30px;">
                        <a href="{link_paypal}" target="_blank" style="flex:1; text-align:center; text-decoration:none; font-family:'Courier Prime',monospace; font-weight:bold; border:1px solid #000; text-transform:uppercase; letter-spacing:4px; background-color:#000; color:#fff; font-size:0.8rem; padding:10px 0;">💳COMPRA-PAYPAL</a>
                        <a href="{link_wa}" target="_blank" style="flex:1; text-align:center; text-decoration:none; font-family:'Courier Prime',monospace; font-weight:bold; border:1px solid #000; text-transform:uppercase; letter-spacing:4px; background-color:#000; color:#fff; font-size:0.8rem; padding:10px 0;">💬COMPRA-WHATSAPP</a>
                    </div>
                    <h2 style="font-size:1.8rem; font-weight:bold; margin:0; text-transform:uppercase; color:black;">{titulo_obra}</h2>
                    <p style="font-size:0.9rem; color:#666; margin:5px 0 20px 0; letter-spacing:2px;">SERIE: {str(r.get("serie", "S/S")).upper()}</p>
                    <div style="border-left:2px solid black; padding-left:20px; margin:20px 0;">
                        <p style="font-size:1rem; margin:5px 0; color:black;"><b>TÉCNICA:</b> {str(r.get("tecnica", "")).upper()} SOBRE {str(r.get("soporte", "")).upper()}</p>
                        <p style="font-size:1rem; margin:5px 0; color:black;"><b>MEDIDAS:</b> {r.get("medidas", "")}</p>
                        <p style="font-size:1.1rem; margin:15px 0 5px 0; font-weight:bold; color:black;">{precio_f} <span style="font-size:0.7rem; color:#888;">[{str(r.get("disponibilidad", "EN VENTA")).upper()}]</span></p>
                    </div>
                    <p style="font-size:1rem; line-height:1.6; text-align:justify; margin-top:25px; color:black;">{descripcion_obra}</p>
                </div>
            '''
            st.markdown(textwrap.dedent(ficha_raw), unsafe_allow_html=True)

            # 3. IMÁGENES (Van después de la ficha)
            st.image(f"assets/{id_ref}.jpg", use_container_width=True)
            for d in range(1, 6):
                if os.path.exists(f"assets/{id_ref}_det_{d}.jpg"):
                    st.image(f"assets/{id_ref}_det_{d}.jpg", use_container_width=True)
            
            # Botón de cierre inferior
            if st.button("VOLVER A LA GALERÍA ↑", key=f"btn_volver_{id_ref}_{sufijo}", use_container_width=True):
                st.query_params.clear()
                st.rerun()
                st.rerun()
            st.markdown("---")
            # 3. DISPARADOR (Se activa si hay una obra en la URL)

        # 4. MOTOR DE LA GALERÍA (Prepara las fotos)
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        obras_a_mostrar = datos_galeria.head(st.session_state.obras_visibles)
        
        # Contenedor de la cuadrícula
        st.markdown('<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 0px 80px;">', unsafe_allow_html=True)
        
        # VARIABLES DE DISEÑO (Tus variables actuales + estas nuevas)
        ALTO_OBRA = "500px" 
        T_PRECIO = "1.2rem"
        SIZE_FIRMA_MODAL = "140px" 
        FUENTE_INDUSTRIAL = "'Courier Prime', monospace"
        C_FONDO_MODAL = "#FFFFFF"

        # --- AÑADE ESTAS DOS PARA LA FICHA ---
        T_TITULO = "0.85rem"
        T_DETALLE = "0.65rem"
 ##================nuevo==========================#

        # AQUÍ EMPIEZA TU BUCLE "for i, (idx, row) in enumerate..."
# --- 1. FILTRADO POR BUSCADOR (Hazlo aquí primero) ---

       # --- 2. LÓGICA DE FILTRADO DINÁMICO ---
        id_en_url = st.query_params.get("obra")

        # Si hay una obra seleccionada, el catálogo "desaparece" y solo queda esa obra
        if id_en_url:
            obras_a_renderizar = datos_galeria[datos_galeria['id_unico'].astype(str).str.contains(str(id_en_url))].head(1)
        else:
            # --- AQUÍ ESTÁ EL CAMBIO PARA LIMITAR A 8 ---
            if tecnica_sel.upper() == "NUEVAS":
                obras_a_renderizar = datos_galeria.head(8)
            else:
                obras_a_renderizar = datos_galeria.head(st.session_state.obras_visibles)

        # A partir de aquí, tu bucle 'for i, (idx, row) in enumerate...' sigue EXACTAMENTE IGUAL

        # Iniciamos el bucle solo con lo necesario
        for i, (idx, row) in enumerate(obras_a_renderizar.iterrows()):
            
            id_obra = str(row.get('id_unico')).split('.')[0]
            ruta_img = f"assets/{id_obra}.jpg"

            # --- MODO ENFOQUE (Si hay obra en URL) ---
            if id_en_url:
                # Inyección inmediata: Sin columnas, sin espacios, sin residuos
                st.write("") 
                mostrar_ficha_tecnica(id_obra, sufijo="enfoque_limpio")
                st.markdown("<hr style='border-top: 2px solid #000; margin: 40px 0;'>", unsafe_allow_html=True)
                continue # Finaliza aquí porque solo hay una obra

            # --- MODO GALERÍA NORMAL (Si NO hay obra en URL) ---
            if i % 4 == 0:
                cols = st.columns([0.5, 1, 1, 1, 1, 0.5], gap="large")
            
            col_target = (i % 4) + 1
            # ... (Aquí sigue todo tu código de 'with cols[col_target]' igual que antes)
            
            with cols[col_target]:
                if os.path.exists(ruta_img):
                    if seccion_actual == "proceso":
                        st.image(ruta_img, use_container_width=True)
                    else:
                        img_b64 = image_to_base64(ruta_img)
                        v_count = st.session_state.obras_visibles
                        t_key = f"{tecnica_sel.replace(' ', '_')}_{v_count}"
                        
                        st.markdown(f"""<style>
                            div.st-key-img_btn_{id_obra}_{t_key} button {{
                                background-image: url("data:image/jpeg;base64,{img_b64}") !important;
                                background-size: cover !important;
                                background-position: center !important;
                                aspect-ratio: 3 / 4 !important;
                                width: 100% !important;
                                border: 1px solid #eee !important;
                                border-radius: 0px !important;
                                background-color: transparent !important;
                            }}
                        </style>""", unsafe_allow_html=True)

                        # Busca esta parte en tu bucle for:
                        if st.button("", key=f"img_btn_{id_obra}_{t_key}", use_container_width=True):
                            st.query_params["obra"] = id_obra 
                            # --- ESTA LÍNEA SUBE EL SCROLL ANTES DE RECARGAR ---
                            st.components.v1.html("<script>window.parent.document.querySelector('section.main').scrollTo(0, 0);</script>", height=0)
                            st.rerun()
                        
                        # --- 1. LIMPIEZA DE PRECIO (Lo que ya tenías) ---
                        p_limpio = str(row.get('precio', '0')).replace('$', '').strip()
                        try:
                            precio_formateado = f"{float(p_limpio.replace(',', '')):,.0f}"
                        except:
                            precio_formateado = p_limpio

                        # --- 2. PLANCHADO DE TEXTO ---
                        def limpiar_texto(txt):
                            t = str(txt)
                            if 'Ã' in t:
                                try: return t.encode('latin-1').decode('utf-8')
                                except: return t
                            return t

                        titulo_f = limpiar_texto(row.get('titulo', 'S/T')).upper()
                        tecnica_f = limpiar_texto(row.get('tecnica', '')).lower()
                        medidas_f = limpiar_texto(row.get('medidas', 'N/A')).lower()
                        estatus_f = limpiar_texto(row.get('disponibilidad', 'en venta')).lower()

                        # --- 3. CONSTRUCCIÓN QUIRÚRGICA DEL HTML (SIN F-STRINGS COMPLEJOS) ---
                        # Subimos el margen a -30px para que pegue a la foto
                        html_inicio = f'<div style="width:100%; font-family:{FUENTE_INDUSTRIAL}; border-top:0.5px solid rgba(0,0,0,0.8); padding-top:8px; margin-top:-16px; margin-bottom:10px;">'
                        html_titulo = f'<p style="font-size:0.9rem; font-weight:bold; margin:0; color:#000;">{titulo_f}</p>'
                        html_tec_med = f'<p style="font-size:0.8rem; margin:2px 0; color:#666; line-height:1.2;">{tecnica_f}<br><span style="font-size:0.7rem; opacity:0.8;">{medidas_f}</span></p>'
                        html_precio = f'<p style="font-size:0.85rem; font-weight:bold; margin-top:8px; color:#000;">${precio_formateado} MXN <span style="font-size:0.65rem; font-weight:normal; color:#888;"> [{estatus_f}]</span></p>'
                        html_fin = '</div>'

                        # Unimos todo en una sola variable
                        f_final = html_inicio + html_titulo + html_tec_med + html_precio + html_fin

                        # --- 4. RENDERIZADO ---
                        st.markdown(f_final, unsafe_allow_html=True)
                        
        # --- BOTÓN VER MÁS (Fuera del bucle for) ---
        
        # ### CAMBIO AQUÍ: Solo entra si NO estamos en la sección "NUEVAS" ###
        if tecnica_sel.upper() != "NUEVAS":
            
            if st.session_state.obras_visibles < len(datos_galeria):
                st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
                
                # Centramos el botón
                _, col_btn, _ = st.columns([1.2, 0.6, 1.2]) 
                with col_btn:
                    if st.button("VER MÁS OBRAS ↓", use_container_width=True):
                        # 1. Aumentamos las obras visibles
                        st.session_state.obras_visibles += 8 
                        
                        # 2. ACTIVAMOS EL SEGURO ANTI-FANTASMA
                        st.session_state.limpiar_fantasma = True
                        
                        # 3. LIMPIAMOS LA URL
                        if "obra" in st.query_params:
                            del st.query_params["obra"]
                        
                        # 4. Recargamos limpio
                        st.rerun()
# --- BOTÓN FLOTANTE "VOLVER ARRIBA" (CUADRADO Y COMPACTO) ---
st.markdown("""
    <a href="#subir" class="scroll-top-btn-square">
        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="18 15 12 9 6 15"></polyline>
        </svg>
    </a>

    <style>
    .scroll-top-btn-square {
        position: fixed;
        bottom: 30px;
        right: 50px; /* Alineado con el padding-left: 50px de PC */
        width: 35px;
        height: 35px;
        background-color: rgba(0, 0, 0, 0.05);
        border: none;
        border-radius: 0px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #666;
        text-decoration: none;
        z-index: 9999;
        transition: all 0.3s ease;
    }

    .scroll-top-btn-square:hover {
        background-color: rgba(0, 0, 0, 0.8);
        color: #fff;
    }

    /* AJUSTE PARA MÓVIL (MÁS PEQUEÑO Y AL BORDE) */
    @media (max-width: 768px) {
        .scroll-top-btn-square {
            bottom: 15px;
            right: 15px; /* Alineado con el padding: 0 15px de móvil */
            width: 28px;  /* Tamaño reducido */
            height: 28px;
            background-color: rgba(0, 0, 0, 0.1); /* Un poco más visible en móvil */
        }
        .scroll-top-btn-square svg {
            width: 14px;
            height: 14px;
        }
    }
    </style>
""", unsafe_allow_html=True)
# --- SECCIÓN 5: PIE DE PÁGINA (SUBIDA DE LÍNEA DIVISORIA) ---
# [cite: 2026-03-02]
# Ajustamos margin-top de 100px a -20px para eliminar el hueco blanco
st.markdown("<hr style='border-top: 1px solid #eeeeee; margin-top: -20px; margin-bottom: 20px;'>", unsafe_allow_html=True)

f1, f2, f3 = st.columns([1, 1, 1])

with f1: 
    # REDES SOCIALES (NEGRO)
    html_redes = f'<div style="display: flex; gap: 15px;">'
    # Mensaje general para el botón de arriba
    msg_gral = "Hola Said, visité tu galería web y me gustaría ponerme en contacto contigo.".replace(" ", "%20")
    redes_html += f'<a href="https://wa.me/5215610810026?text={msg_gral}" target="_blank"><img src="data:image/png;base64,{icon_wa_b64}" style="width:18px; filter:brightness(0);"></a>'
    html_redes += f'<a href="https://www.instagram.com/saidmontano_/" target="_blank"><img src="data:image/png;base64,{icon_ig_b64}" style="width:18px; filter:brightness(0);"></a>'
    html_redes += f'<a href="https://www.tiktok.com/@saidmaokh" target="_blank"><img src="data:image/png;base64,{icon_tk_b64}" style="width:18px; filter:brightness(0);"></a>'
    st.markdown(html_redes + '</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:#000000; font-family:Courier Prime; font-size:0.7rem; margin-top:5px;'>art.sades@gmail.com</p>", unsafe_allow_html=True)

with f2: 
    if logo_main_b64:
        # Reducimos un poco el logo para que no empuje el pie de página hacia abajo
        st.markdown(f'<div style="text-align: center; margin-top: -10px;"><img src="data:image/png;base64,{logo_main_b64}" style="width:150px; filter:brightness(0);"></div>', unsafe_allow_html=True)

with f3: 
    st.markdown("<p style='text-align:right; color:#000000; font-family:Courier Prime; font-size:0.7rem; margin-top:5px;'>© 2026 - TODOS LOS DERECHOS RESERVADOS</p>", unsafe_allow_html=True)



# --- ZOOM FORZADO PARA SERVIDORES SEGUROS ---
components.html("""
<script src="https://cdn.jsdelivr.net/npm/medium-zoom@1.0.6/dist/medium-zoom.min.js"></script>
<script>
    window.addEventListener('load', function() {
        setTimeout(function() {
            // Buscamos todas las imágenes de la página, incluso fuera de nuestro cuadro
            const images = Array.from(window.parent.document.querySelectorAll('img'))
                                .filter(img => img.width > 100);
            
            if (images.length > 0) {
                mediumZoom(images, {
                    margin: 0,
                    background: 'rgba(0,0,0,0.95)'
                });
            }
        }, 2000); // Esperamos 2 segundos a que todo cargue
    });
</script>
""", height=0)


    #===   streamlit run app.py   ===#
