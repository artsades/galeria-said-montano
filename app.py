# SECCIÓN 1: CONFIGURACIÓN Y RECURSOS
# -----------------------------------------------------------------
import streamlit as st
import pandas as pd
import os
import base64

st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">', unsafe_allow_html=True)

# --- BÓVEDA SEO: PALABRAS INVISIBLES PARA GOOGLE ---
PALABRAS_SEO = "Said Montaño, artista visual mexicano, pintura al óleo CDMX, arte contemporáneo oscuro, realismo figurativo, cuadros al óleo, galería de arte online México, arte simbólico, escultura contemporánea, comprar arte directo artista, estudio de arte Ciudad de México, fine art photography, coleccionismo de arte, arte figurativo oscuro."

# Título dinámico para la pestaña del navegador
t_pestana = st.session_state.get('tec_ref', 'ARCHIVO VISUAL')

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
    return "https://saidmontano.art/static/said_perfil.jpg" # Plan C: Tu logo de la web

fav_icon_data = get_favicon_final()

st.set_page_config(
    page_title=f"Said Montaño | {t_pestana}", 
    page_icon=fav_icon_data, 
    layout="wide", 
    initial_sidebar_state="collapsed"
)
# Inyección SEO (Sin generar espacios ni líneas negras)
st.markdown(f'<div style="display:none; height:0; width:0; overflow:hidden; visibility:hidden;">{PALABRAS_SEO}</div>', unsafe_allow_html=True)

# --- MEMORIA DE NAVEGACIÓN (F5) ---
if "p" in st.query_params:
    st.session_state.pag_ref = int(st.query_params["p"])
elif 'pag_ref' not in st.session_state:
    st.session_state.pag_ref = 0

if "t" in st.query_params:
    st.session_state.tec_ref = st.query_params["t"]
elif 'tec_ref' not in st.session_state:
    st.session_state.tec_ref = "PINTURA AL OLEO"

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
    .block-container {{ padding: 0 50px !important; margin-top: -10px !important; }}

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
        margin-top: 0px !important;
        margin-bottom: 0px !important;
        animation: adn-breathe 2s ease-in-out infinite;
    }}

    /* 2.3 BUSCADOR */
    .stApp div[data-baseweb="input"], 
    .stApp div[data-baseweb="input"] > div {{
        background-color: #F0F0F0 !important;
        border-radius: 0px !important;
        border: none !important;
        border-bottom: 1px solid #757575 !important;
        height: 15px !important;
        min-height: 15px !important;
    }}
    
    .stApp div[data-baseweb="input"] input {{
        background-color: transparent !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        font-family: 'Courier Prime' !important;
        font-size: 0.85rem !important;
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

    /* 2.5 TEXTOS Y RADIO */
    .stRadio div[role="radiogroup"] label p {{ 
        color: #000000 !important;
        font-family: 'Courier Prime' !important;
        font-weight: bold !important;
    }}
    
    div[data-testid="stRadio"] {{
        width: 100% !important;
        margin-top: 2px !important; 
        margin-bottom: 20px !important;
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
        background-color: #D3D3D3 !important; 
        padding: 1px 0px !important;
        border-radius: 0px !important;
    }}

    div[data-testid="stRadio"] label > div:first-of-type {{ display: none !important; }}
    
    div[data-testid="stRadio"] label p {{
        font-family: 'Courier Prime' !important;
        font-size: 0.85rem !important;
        color: #888888 !important; 
        letter-spacing: 5px !important; 
        text-transform: uppercase;
        white-space: nowrap !important;
    }}

    div[data-testid="stRadio"] label:has(input:checked) p {{
        color: #000000 !important;
        text-decoration: underline !important;
        text-underline-offset: 10px !important;
    }}
    </style>
""", unsafe_allow_html=True)

# SECCIÓN 3: CABECERA (LOGO SUPERIOR Y REDES)
# -----------------------------------------------------------------
st.markdown('<div class="banner-envios">ENVÍOS NACIONALES E INTERNACIONALES - TRATO DIRECTO CON EL ARTISTA </div>', unsafe_allow_html=True)

# REDUCIMOS EL ESPACIO ENTRE COLUMNAS (gap)
c1, c2, c3 = st.columns([1.2, 4, 0.8], gap="small") 

with c1:
    if logo_main_b64:
        st.markdown(f'''
            <div style="margin-top: 0px; padding-top: 0px;">
                <img src="data:image/png;base64,{logo_main_b64}" 
                     style="width: 250px; filter: brightness(0); display: block; margin-top: 0px;">
            </div>
        ''', unsafe_allow_html=True)
    
    # --- AJUSTE DE ALINEACIÓN AQUÍ ---
    # CAMBIAMOS EL MARGEN PARA SUBIR O BAJAR EL TEXTO Y QUE CUADRE CON EL BUSCADOR
    st.markdown("<p style='color:#000000; font-family:Courier Prime; font-size:0.6rem; font-weight:bold; margin-top: 0px; letter-spacing:1px;'>ESTUDIO DE ARTE / CDMX / 2026</p>", unsafe_allow_html=True)

with c2:
    # --- AJUSTE DE ALTURA AQUÍ ---
    # Aumenta el número (ej. 30px, 35px) para bajar la barra más
    st.markdown("<div style='margin-top: 60px;'>", unsafe_allow_html=True) 
    
    filtro_busq = st.text_input(
        "", 
        placeholder="ESCRIBE PARA BUSCAR...", 
        key="search", 
        label_visibility="collapsed"
    ).lower()
    
    st.markdown("</div>", unsafe_allow_html=True)

with c3:
    # --- AJUSTE DE ALTURA PARA ICONOS ---
    # Se usa la URL completa para que TikTok e Instagram abran fuera de tu web
    redes_html = f'<div style="display: flex; justify-content: flex-end; gap: 20px; margin-top: 52px; z-index: 9999;">'
    
    # WHATSAPP (Cambia las X por tu número)
   # Mensaje general para el botón de arriba
    msg_gral = "Hola Said, visité tu galería web y me gustaría ponerme en contacto contigo.".replace(" ", "%20")
    redes_html += f'<a href="https://wa.me/5215610810026?text={msg_gral}" target="_blank"><img src="data:image/png;base64,{icon_wa_b64}" style="width:18px; filter:brightness(0);"></a>'
    
    # INSTAGRAM
    redes_html += f'<a href="https://www.instagram.com/saidmontano_/" target="_blank"><img src="data:image/png;base64,{icon_ig_b64}" style="width:18px; filter:brightness(0);"></a>'
    
    # TIKTOK (Protocolo completo https://www para evitar error)
    redes_html += f'<a href="https://www.tiktok.com/@saidmontano_" target="_blank"><img src="data:image/png;base64,{icon_tk_b64}" style="width:18px; filter:brightness(0);"></a>'
    
    st.markdown(redes_html + '</div>', unsafe_allow_html=True)



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



# 3.3 SELECCIÓN DE TÉCNICAS (ELIMINACIÓN DE RESTRICCIONES DE STREAMLIT)
st.markdown('''
    <style>
    /* ATACAMOS EL CONTENEDOR QUE DA EL ESPACIO AUTOMÁTICO */
    [data-testid="stVerticalBlock"] > div:has(div[data-testid="stRadio"]) {
        margin-top: -73px !important; /* <--- AJUSTA ESTO PARA SUBIR O BAJAR */
        margin-bottom: -20px !important;
    }
    
    /* ASEGURAMOS QUE EL RADIO SEA HORIZONTAL */
    div[data-testid="stRadio"] > div {
        flex-direction: row !important;
        flex-wrap: wrap;
    }
    </style>
''', unsafe_allow_html=True)

opciones = ["PINTURA AL OLEO", "ACUARELA", "DIBUJO","ARTE DIGITAL", "ESCULTURA", "ESTUDIO"]
idx_tec = opciones.index(st.session_state.tec_ref) if st.session_state.tec_ref in opciones else 0

tecnica_sel = st.radio("", opciones, index=idx_tec, horizontal=True, label_visibility="collapsed")

# Si cambias de técnica, reseteamos página y guardamos en URL
if tecnica_sel != st.session_state.tec_ref:
    st.session_state.tec_ref = tecnica_sel
    st.session_state.pag_ref = 0
    st.query_params["t"] = tecnica_sel
    st.query_params["p"] = 0
    st.rerun()


# --- 3.4 DESPLEGABLE CON FOTO (ESTRUCTURA RÍGIDA AJUSTABLE) ---
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
    /* 1. BARRA GRIS TOTAL */
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
        background-color: #D3D3D3 !important;
        padding: 25px 0px !important; 
    }

    .tabla-bio {
        background-color: #FFFFFF !important;
        margin: 0 auto !important;
        padding: 45px !important;
        
        /* --- ETIQUETA DE EDICIÓN: ANCHO_RECTANGULO_BLANCO --- */
        /* Sube este % para expandir más el cuadro blanco a los lados */
        width: 100% !important; 
        
        max-width: 1400px !important; /* Límite para pantallas muy grandes */
        border-collapse: separate;
        border-spacing: 30px 0px;
    }
    </style>
''', unsafe_allow_html=True)

with st.expander("SOBRE EL ARTISTA"):
    # Definimos las columnas
    col_foto, col_texto1, col_texto2 = st.columns([1, 2, 2])
    
    with col_foto: # <--- Aquí corregimos el nombre de 'col1' a 'col_foto'
        # Usamos el link que funciona en tu GitHub
        foto_url = "https://raw.githubusercontent.com/artsades/galeria-said-montano/main/said_perfil.jpg"
        st.markdown(f'''
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{foto_url}" style="
                    width: 120px; 
                    height: 120px; 
                    border-radius: 50%; 
                    object-fit: cover; 
                    border: 2px solid #eeeeee; 
                    box-shadow: 0px 4px 6px rgba(0,0,0,0.3);">
            </div>
        ''', unsafe_allow_html=True)
        
    with col_texto1:
        st.markdown("""
        <div style="color: #000000; font-family: 'Courier Prime', monospace; font-size: 15px; text-align: justify; line-height: 1.6;">
            Said Montaño es un artista visual mexicano cuya práctica se centra principalmente en la pintura al óleo sobre lienzo. 
            Su trabajo explora estados emocionales contenidos y tensiones psicológicas que operan de forma silenciosa y persistente.
        </div>
        """, unsafe_allow_html=True)

    with col_texto2:
        st.markdown("""
        <div style="color: #000000; font-family: 'Courier Prime', monospace; font-size: 15px; text-align: justify; line-height: 1.6;">
            Paralelamente, ha desarrollado una línea escultórica que mantiene el mismo lenguaje oscuro y personal. 
            Explora la materialidad del cuerpo y sus restos como símbolos de permanencia, desgaste y memoria.
        </div>
        """, unsafe_allow_html=True)
    
# LÍNEA EXTRA DE SEGURIDAD PARA LA GALERÍA
st.write("")



#===SECCION DE LAS OBRAS=====
# 4.0 LECTURA Y CONTROL DE DATOS [cite: 2026-03-02]
archivos_csv = [f for f in os.listdir('.') if f.endswith('.csv')]

if archivos_csv:
    # PERSISTENCIA DE DATOS [cite: 2026-03-02]
    if 'datos_master' not in st.session_state:
        try:
            st.session_state.datos_master = pd.read_csv(archivos_csv[0], encoding='latin1')
        except:
            st.session_state.datos_master = pd.read_csv(archivos_csv[0], encoding='utf-8')
        st.session_state.datos_master.columns = [c.lower().strip() for c in st.session_state.datos_master.columns]

    # 4.1 FILTRADO INTELIGENTE (Prioridad a Series) [cite: 2026-03-05]
    df_f = st.session_state.datos_master.copy().dropna(subset=['tecnica'])

    # SEPARACIÓN POR SECCIÓN (Said Montaño)
    seccion_actual = "proceso" if "ESTUDIO" in tecnica_sel.upper() else "galeria"
    df_f = df_f[df_f['seccion'] == seccion_actual]

    # 1. FILTRO DE BÚSQUEDA INTEGRAL (Título, Serie, Descripción y Tags)
    if filtro_busq:
        df_f = df_f[df_f.apply(lambda r: 
            filtro_busq in str(r.get('titulo','')).lower() or 
            filtro_busq in str(r.get('descripcion','')).lower() or
            filtro_busq in str(r.get('serie','')).lower() or
            filtro_busq in str(r.get('tags','')).lower(), 
            axis=1)]

    # FILTRADO DIRECTO POR TÉCNICA
    palabra_clave = tecnica_sel.split()[-1].upper()
    if palabra_clave != "OBRAS": 
        df_f = df_f[df_f['tecnica'].str.upper().str.contains(palabra_clave, na=False)]
    if not df_f.empty:
        # --- LÓGICA DE PÁGINAS ESTABLE [cite: 2026-03-02] ---
        OBRAS_POR_PAGINA = 10
        total_paginas = (len(df_f) // OBRAS_POR_PAGINA) + (1 if len(df_f) % OBRAS_POR_PAGINA > 0 else 0)
        
        # Anclamos la página para que no desaparezca al volver a la 1
        if 'pag_ref' not in st.session_state: st.session_state.pag_ref = 0
        if st.session_state.pag_ref >= total_paginas: st.session_state.pag_ref = 0
        
        datos_galeria = df_f.iloc[st.session_state.pag_ref * OBRAS_POR_PAGINA : (st.session_state.pag_ref + 1) * OBRAS_POR_PAGINA]

        # --- FILA DE TÍTULO Y CONTADOR ---
        total_obras_tec = len(df_f)
        inicio_rango = (st.session_state.pag_ref * OBRAS_POR_PAGINA) + 1
        fin_rango = min((st.session_state.pag_ref + 1) * OBRAS_POR_PAGINA, total_obras_tec)

        st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid #eeeeee; padding-bottom: 10px; margin-top: -38px; font-family: 'Courier Prime';">
                <p style="margin: 0; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; color: #000;">{tecnica_sel}</p>
                <p style="margin: 0; font-size: 0.7rem; letter-spacing: 1px; color: #888;">MOSTRANDO {inicio_rango}-{fin_rango} DE {total_obras_tec} OBRAS</p>
            </div>
        """, unsafe_allow_html=True)
            
        # VARIABLES DE DISEÑO ORIGINAL [cite: 2026-02-27]
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        ALTO_OBRA = "500px" 
        T_PRECIO = "1.2rem"
        SIZE_FIRMA_MODAL = "140px" 
        FUENTE_INDUSTRIAL = "'Courier Prime', monospace"
        C_FONDO_MODAL = "#FFFFFF"

        # === COPIAR DESDE AQUÍ: CONFIGURACIÓN 2 COLUMNAS MÓVIL / 5 PC ===
        st.markdown("""
            <style>
            /* Contenedor de las columnas */
            [data-testid="stHorizontalBlock"] {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }
            /* Ajuste para Celulares (2 columnas) */
            @media (max-width: 768px) {
                [data-testid="stHorizontalBlock"] > div {
                    min-width: 45% !important;
                    flex: 1 1 45% !important;
                }
                /* Ajuste de altura de imagen para celular para que no se vea gigante */
                div[class*="st-key-img_btn_"] button {
                    height: 250px !important;
                }
            }
            /* Ajuste para PC (5 columnas) */
            @media (min-width: 769px) {
                [data-testid="stHorizontalBlock"] > div {
                    min-width: 18% !important;
                    flex: 1 1 18% !important;
                }
            }
            </style>
        """, unsafe_allow_html=True)
        # === HASTA AQUÍ ===
        
        # --- FUNCIÓN GLOBAL DEL VISOR ---
        @st.dialog(" ", width="large")
        def visor_galeria(id_ref):
            # Encabezado del visor
            st.markdown(f'<div style="display:flex; justify-content:space-between;"><div style="font-family:Courier Prime; font-size:0.7rem;">ARCHIVO VISUAL</div><img src="data:image/png;base64,{logo_main_b64}" style="width:100px; filter:brightness(0);"></div><hr>', unsafe_allow_html=True)
            
            # IMAGEN PRINCIPAL (Con link directo de GitHub para habilitar zoom)
            url_principal = f"https://raw.githubusercontent.com/artsades/galeria-said-montano/main/assets/{id_ref}.jpg"
            st.markdown(f'<img src="{url_principal}" style="width:100%; margin-bottom: 20px;">', unsafe_allow_html=True)
            
            # IMÁGENES DE DETALLE (Bucle corregido para zoom)
            for d in range(1, 6):
                ruta_detalle = f"assets/{id_ref}_det_{d}.jpg"
                if os.path.exists(ruta_detalle):
                    url_det = f"https://raw.githubusercontent.com/artsades/galeria-said-montano/main/{ruta_detalle}"
                    st.markdown(f'<img src="{url_det}" style="width:100%; margin-bottom: 20px;">', unsafe_allow_html=True)
            
            # BOTÓN DE CIERRE (Para evitar usar el botón 'atrás' del celular)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("✕ CERRAR VISTA", use_container_width=True):
                st.rerun()

                    # --- CASO B: SI ES GALERÍA COMERCIAL ---
                    else:
                        # 1. CONVERSIÓN Y LLAVE
                        img_b64 = image_to_base64(ruta_img)
                        t_key = tecnica_sel.replace(" ", "_")

                        # 2. CSS PARA EL BOTÓN-IMAGEN
                        st.markdown(f"""<style>
                            div.st-key-img_btn_{id_obra}_{t_key} button {{
                                background-image: url("data:image/jpeg;base64,{img_b64}") !important;
                                background-size: cover !important;
                                background-position: center !important;
                                height: {ALTO_OBRA} !important;
                                width: 100% !important;
                                border: 1px solid #eee !important;
                                background-color: transparent !important;
                                border-radius: 0px !important;
                            }}
                        </style>""", unsafe_allow_html=True)

                        # 3. EL BOTÓN-IMAGEN
                        if st.button("", key=f"img_btn_{id_obra}_{t_key}", use_container_width=True):
                            visor_galeria(id_obra)

                        # 4. CÁLCULO DE PRECIO
                        import re
                        val_p = str(row.get('precio', '0'))
                        solo_n = re.sub(r'[^0-9.]', '', val_p)
                        try: precio_f = f"${float(solo_n):,.0f} MXN"
                        except: precio_f = "CONSULTAR PRECIO"

                        # 5. FICHA TÉCNICA
                        st.markdown(f'''
                        <div style="width: 100%; font-family: {FUENTE_INDUSTRIAL}; text-transform: uppercase; text-align: left; border-top: 1px solid #000; padding-top: 10px; margin-top: -15px;">
                            <p style="font-size: 1.0rem; color: #000; font-weight: bold; margin: 0;">{row.get('titulo', 'S/T')}</p>
                            <p style="font-size: 0.7rem; color: #444; margin: 2px 0;">SERIE: {row.get('serie', 'S/S')}</p>
                            <p style="font-size: 0.75rem; color: #444; margin: 0;">{str(row.get('tecnica', '')).upper()} SOBRE {str(row.get('soporte', '')).upper()}</p>
                            <p style="font-size: 0.75rem; color: #444; margin: 0;">{row.get('medidas', '')}</p>
                            <p style="font-size: {T_PRECIO}; color: #000; font-weight: bold; margin-top: 10px;">{precio_f}</p>
                            <p style="font-size: 0.65rem; font-weight: bold; color: #000; margin-bottom: 10px;">[{str(row.get('disponibilidad', 'EN VENTA')).upper()}]</p>
                        </div>''', unsafe_allow_html=True)

                        # 6. BOTÓN DE DETALLES + WHATSAPP (EL QUE YA TENÍAS)
                        # --- Pega aquí el bloque de las columnas (col_det, col_wa) que arreglamos antes ---

                    # --- NUEVO: BOTÓN DE WHATSAPP INTELIGENTE ---
                    txt_obra = f"Hola Said, me interesa la obra '{row.get('titulo', 'S/T')}' de la serie '{row.get('serie', 'S/S')}'. ¿Sigue disponible?".replace(" ", "%20")
                    link_wa_obra = f"https://wa.me/5215610810026?text={txt_obra}"

                
                    # MODAL DETALLES
                    # --- FILA DE ACCIONES (VER DETALLES + ICONO WA) ---
                    # --- REPARACIÓN DEFINITIVA: BOTÓN + ICONO FLOTANTE ---
                    # Creamos un contenedor relativo para que el icono sepa dónde posicionarse
                    st.markdown(f'''
                        <div style="position: relative; width: 100%; margin-top: -15px;">
                            <div style="width: 85%;">
                    ''', unsafe_allow_html=True)

                    # 1. BOTÓN "VER DETALLES"
                    if st.button("VER DETALLES", key=f"btn_{id_obra}_{idx}", use_container_width=True):
                        @st.dialog(" ")
                        def ventana_detalles(r):
                            st.markdown(f"""<style>[data-testid="stDialogHeader"] {{ display: none !important; }} div[data-testid="stDialog"] div[role="dialog"] {{ background-color: #FFF !important; padding-top: 20px !important; }} .stMarkdown p, .stMarkdown h2, .stMarkdown div {{ color: #000000 !important; font-family: {FUENTE_INDUSTRIAL} !important; }}</style><div style="display: flex; justify-content: flex-end; margin-bottom: 20px;"><img src="data:image/png;base64,{logo_main_b64}" style="width: 140px; filter: brightness(0);"></div><hr style="border-top: 1px solid #000; margin-bottom: 20px;">""", unsafe_allow_html=True)
                            st.markdown(f"## {r.get('titulo','').upper()}")
                            st.markdown(f"<div style='text-align: justify;'>{r.get('descripcion','')}</div>", unsafe_allow_html=True)
                        ventana_detalles(row)

                    # 2. ICONO WHATSAPP POSICIONADO A LA IZQUIERDA (CASI PEGADO)
                    txt_obra = f"Hola Said, me interesa la obra '{row.get('titulo', 'S/T')}' de la serie '{row.get('serie', 'S/S')}'. ¿Sigue disponible?".replace(" ", "%20")
                    link_wa_obra = f"https://wa.me/5215610810026?text={txt_obra}"

                    st.markdown(f'''
                            </div>
                            <a href="{link_wa_obra}" target="_blank" 
                               style="position: absolute; left: 150px; top: -45px; text-decoration: none;">
                                <img src="data:image/png;base64,{icon_wa_b64}" 
                                     style="width: 20px; filter: brightness(0); opacity: 0.8;">
                            </a>
                        </div>
                        <div style="height: 20px;"></div>
                    ''', unsafe_allow_html=True)

        # SI SE HIZO CLIC, ABRIMOS EL DIALOG
                    if st.session_state.get('obra_seleccionada') == id_obra:
                        visor_galeria(id_obra)
                        st.session_state.obra_seleccionada = None

        # --- PAGINADOR CON AJUSTE MILIMÉTRICO ---
        if total_paginas > 1:
            # ESPACIADOR AJUSTABLE: Cambia el 'height' para subir o bajar (ej: 40px, 50px, 60px)
            #
            st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True) 
            
            st.markdown("""<style>
                div.st-key-pag_final_v3 {
                    clear: both;
                    display: flex;
                    justify-content: center;
                }
                div.st-key-pag_final_v3 div[role="radiogroup"] { 
                    gap: 30px !important; 
                    background: transparent !important; 
                }
                div.st-key-pag_final_v3 label p { 
                    font-family: 'Courier Prime' !important; 
                    color: #888 !important; 
                }
                div.st-key-pag_final_v3 label:has(input:checked) p { 
                    color: #000 !important; 
                    font-weight: bold !important; 
                    text-decoration: underline !important; 
                }
                div.st-key-pag_final_v3 [data-baseweb="radio"] div::after { display: none !important; }
            </style>""", unsafe_allow_html=True)
            
            opciones_pag = [str(i+1) for i in range(total_paginas)]
            indice_actual = st.session_state.get('pag_ref', 0)
            
            # Usamos 'pag_final_v3' para evitar cualquier error de duplicado previo
            sel_p = st.radio(
                "", 
                opciones_pag, 
                index=indice_actual, 
                horizontal=True, 
                label_visibility="collapsed", 
                key="pag_final_v3"
            )
            
            nuevo_indice = int(sel_p) - 1
            if nuevo_indice != st.session_state.get('pag_ref'):
                st.session_state.pag_ref = nuevo_indice
                # ESCRIBE LA PÁGINA EN LA URL
                st.query_params["p"] = nuevo_indice
                st.rerun()



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
    html_redes += f'<a href="https://www.tiktok.com/@saidmontano_" target="_blank"><img src="data:image/png;base64,{icon_tk_b64}" style="width:18px; filter:brightness(0);"></a>'
    st.markdown(html_redes + '</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:#000000; font-family:Courier Prime; font-size:0.7rem; margin-top:5px;'>art.sades@gmail.com</p>", unsafe_allow_html=True)

with f2: 
    if logo_main_b64:
        # Reducimos un poco el logo para que no empuje el pie de página hacia abajo
        st.markdown(f'<div style="text-align: center; margin-top: -10px;"><img src="data:image/png;base64,{logo_main_b64}" style="width:150px; filter:brightness(0);"></div>', unsafe_allow_html=True)

with f3: 
    st.markdown("<p style='text-align:right; color:#000000; font-family:Courier Prime; font-size:0.7rem; margin-top:5px;'>© 2026 - TODOS LOS DERECHOS RESERVADOS</p>", unsafe_allow_html=True)

# 1. DATOS (TEXTO LIMPIO)
INFO_ESTUDIO_SAID = {
    "ENVÍOS INTERNACIONALES": "Logística global especializada con seguro de cobertura total. Cada pieza se embala bajo estrictos estándares de conservación en cajas de madera, cartón ultraresistente o empaques técnicos de alta resistencia.",
    "TRATO DIRECTO CON EL ARTISTA": "La adquisición de piezas se gestiona directamente con el estudio de Said Montaño. Esto garantiza la autenticidad absoluta de la obra y elimina comisiones de intermediarios.",
    "CÓMO COMPRAR": "1. SELECCIÓN: Elija la pieza de su interés en el catálogo, guarde su nombre y serie si es que pertenece a alguna .<br><br>2. CONSULTA: Verifique disponibilidad y costos de envío (Vía WhatsApp, DM en Instagram, DM Tiktok o correo electrónico: art.sades@gmail.com) .<br><br>3. PAGO: Confirmada la pieza, se emite la factura para pago o se le proporcionan los datos necesarios, segun el tipo de pago.<br><br>4. LOGÍSTICA: Despacho en un lapso de 3 a 5 días hábiles en México. (Si usted requiere el envío fuera de México cunsultelo por via whatsapp, DM instagran, DM tiktok, art.sades@gmail.com).",
    "OBRA PERSONALIZADA": "Se aceptan proyectos por comisión bajo un análisis previo. Pregunta por via WhatsApp, Instagram, tiktok, art.sades@gmail.com (Se requiere anticipo del 60% )",
    "MÉTODOS DE PAGO": "Transferencias bancarias (SPEI) y PAY PAL. Se emite factura fiscal o comercial.",
    "CUIDADOS DE LA OBRA": "• Evite luz solar directa.<br><br>• Humedad controlada.<br><br>• Limpie solo con brocha de pelo suave o microfibra seca.<br><br>• No aplique solventes ni químicos."
}

# 2. FUNCIÓN DEL CUADRO (MODAL) - ESTRUCTURA DE TABLA PARA FIJAR POSICIONES
@st.dialog(" ")
def desplegar_info_servicio(nombre_servicio):
    descripcion = INFO_ESTUDIO_SAID.get(nombre_servicio, "")
    
    st.markdown(f"""
        <style>
            [data-testid="stDialogHeader"] {{ display: none !important; }} 
            div[data-testid="stDialog"] div[role="dialog"] {{ 
                background-color: white !important; 
                padding: 30px !important; 
                border: 1px solid black;
                border-radius: 0px;
                max-width: 500px !important;
            }}
            .tabla-modal {{
                width: 100%;
                border-collapse: collapse;
            }}
            .celda-logo {{
                text-align: right;
                padding-bottom: 20px;
            }}
            .logo-said-img {{
                width: 120px;
                filter: brightness(0);
            }}
            .titulo-servicio {{
                font-family: 'Courier Prime', monospace;
                color: black;
                text-transform: uppercase;
                letter-spacing: 2px;
                font-size: 1.2rem;
                margin: 0;
            }}
            .contenido-servicio {{
                font-family: 'Courier Prime', monospace;
                color: black;
                text-align: justify;
                line-height: 1.6;
                font-size: 0.95rem;
                padding-top: 20px;
            }}
        </style>
        
        <table class="tabla-modal">
            <tr>
                <td class="celda-logo">
                    <img src="data:image/png;base64,{logo_main_b64}" class="logo-said-img">
                </td>
            </tr>
            <tr>
                <td>
                    <h3 class="titulo-servicio">{nombre_servicio}</h3>
                    <hr style="border-top: 1px solid black; margin: 10px 0;">
                </td>
            </tr>
            <tr>
                <td class="contenido-servicio">
                    {descripcion}
                </td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

    if st.button("CERRAR", use_container_width=True):
        st.rerun()

# 3. BARRA GRIS (TU POSICIÓN EXACTA)
st.markdown(f"""
    <style>
        .franja-servicios-final {{
            width: 100vw !important;
            margin-left: -50vw !important;
            left: 50% !important;
            position: relative !important;
            background-color: #D3D3D3 !important;
            margin-top: 20px !important;
            padding: 25px 0 !important;
            display: flex;
            justify-content: center;
        }}
        div[data-testid="stRadio"]:has(label:contains("menu_said_final")) > div {{
            flex-direction: row !important;
            justify-content: center !important;
            gap: 40px !important;
        }}
        div[data-testid="stRadio"]:has(label:contains("menu_said_final")) label {{
            background: none !important;
            border: none !important;
            color: black !important;
            font-family: 'Courier Prime', monospace !important;
            font-size: 0.72rem !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
            cursor: pointer !important;
        }}
        div[data-testid="stRadio"]:has(label:contains("menu_said_final")) input {{ display: none !important; }}
    /* --- REPARACIÓN DE BOTONES BLANCOS (SAID MONTAÑO) --- */
    div.stButton > button:has(p) {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
        border-radius: 0px !important;
        height: 1px !important; 
        width: 135px !important;
        padding: 0px !important;
        margin-top: -20px !important; 
    }}

    div.stButton > button:has(p) p {{
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        font-family: 'Courier Prime', monospace !important;
        font-size: 0.7rem !important;
        font-weight: bold !important;
        letter-spacing: 2px !important;
    }}

    /* PROTECCIÓN DE FOTOS (ALTO INDUSTRIAL) */
    div.stButton > button:not(:has(p)) {{
        background-color: transparent !important;
        height: 500px !important;
        border: 1px solid #eee !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 4. RENDERIZADO
if 'key_srv' not in st.session_state:
    st.session_state.key_srv = 0

st.markdown('<div class="franja-servicios-final">', unsafe_allow_html=True)
opcion = st.radio(
    label="menu_said_final",
    options=list(INFO_ESTUDIO_SAID.keys()),
    index=None,
    horizontal=True,
    label_visibility="collapsed",
    key=f"srv_{st.session_state.key_srv}"
)
st.markdown('</div>', unsafe_allow_html=True)

if opcion:
    st.session_state.key_srv += 1
    desplegar_info_servicio(opcion)


    #===   streamlit run app.py   ===#
















