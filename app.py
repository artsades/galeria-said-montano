# SECCIÓN 1: CONFIGURACIÓN, RECURSOS Y SEO DINÁMICO
# -----------------------------------------------------------------
import streamlit as st
import pandas as pd
import os
import base64
import requests
from bs4 import BeautifulSoup

# --- FUNCIÓN DE SEO DINÁMICO ---
def obtener_seo_estudio():
    keywords = [
        "Said Montaño", "Oil paintings for sale USA", "Pintura al óleo México", 
        "Acuarelas originales", "Fine art watercolors", "Shipping worldwide Skydropx",
        "Contemporary art Mexico", "Comprar arte original", "Destellos del más allá"
    ]
    try:
        res = requests.get("https://www.saatchiart.com/art/Painting/Realism/", timeout=2)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            tendencias = [tag.text.strip() for tag in soup.find_all('h3')[:3]]
            keywords.extend(tendencias)
    except:
        pass 
    return ", ".join(keywords)

SEO_DINAMICO = obtener_seo_estudio()

st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">', unsafe_allow_html=True)

# --- BÓVEDA SEO ACTUALIZADA ---
PALABRAS_SEO = f"{SEO_DINAMICO}, Said Montaño artista, realismo figurativo, arte oscuro, envíos seguros a USA y México."
t_pestana = st.session_state.get('tec_ref', 'ARCHIVO VISUAL')

# --- CARGA DEL FAVICON ---
def get_favicon_final():
    folder = "static"
    if os.path.exists(folder):
        for archivo in os.listdir(folder):
            if archivo.lower().startswith("fav") and archivo.lower().endswith((".png", ".jpg", ".jpeg", ".ico")):
                path_fav = os.path.join(folder, archivo)
                with open(path_fav, "rb") as f:
                    return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    return "https://saidmontano.art/static/logo_said_montano.png"

fav_icon_data = get_favicon_final()

st.set_page_config(
    page_title=f"Said Montaño | {t_pestana} | Fine Art Shipping USA & MX", 
    page_icon=fav_icon_data, 
    layout="wide", 
    initial_sidebar_state="collapsed"
)
st.markdown(f'<div style="display:none; height:0; width:0; overflow:hidden; visibility:hidden;">{PALABRAS_SEO}</div>', unsafe_allow_html=True)

# --- LÓGICA DE NAVEGACIÓN (SOLUCIÓN BOTÓN ATRÁS) ---
# Si el usuario da "atrás", el query param 'obra' desaparece y el modal se cierra solo.
query_params = st.query_params
obra_en_url = query_params.get("obra")

if "p" in st.query_params:
    st.session_state.pag_ref = int(st.query_params["p"])
elif 'pag_ref' not in st.session_state:
    st.session_state.pag_ref = 0

# PRIORIDAD ACUARELA POR DEFECTO
if "t" in st.query_params:
    st.session_state.tec_ref = st.query_params["t"]
elif 'tec_ref' not in st.session_state:
    st.session_state.tec_ref = "ACUARELA"

def image_to_base64(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    return ""

logo_main_b64 = image_to_base64("static/logo_said_montano.png")
icon_wa_b64 = image_to_base64("static/logo_whatsapp.png")
icon_ig_b64 = image_to_base64("static/logo_instagram.png")
icon_tk_b64 = image_to_base64("static/logo_tiktok.png")

# SECCIÓN 2: ADN VISUAL (CSS)
# -----------------------------------------------------------------
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap');
    .stAppHeader {{ display: none !important; }}
    .stApp {{ background-color: #ffffff; }}
    .block-container {{ padding: 0 50px !important; margin-top: -10px !important; }}

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
        animation: adn-breathe 2s ease-in-out infinite;
    }}

    /* RADIO BUTTONS (MENÚ) */
    div[data-testid="stRadio"] > div[role="radiogroup"] {{
        background-color: #D3D3D3 !important;
        padding: 5px 0px !important;
    }}
    div[data-testid="stRadio"] label p {{
        font-family: 'Courier Prime' !important;
        font-size: 0.85rem !important;
        letter-spacing: 3px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# SECCIÓN 3: CABECERA
# -----------------------------------------------------------------
st.markdown('<div class="banner-envios">ENVÍOS NACIONALES E INTERNACIONALES - TRATO DIRECTO CON EL ARTISTA </div>', unsafe_allow_html=True)

# BANNER DE OFERTA ESPECIAL (DESTELLOS DEL MÁS ALLÁ)
st.info("✨ **OFERTA DE COLECCIÓN:** Adquiere las 4 acuarelas originales de la serie *'Destellos del más allá'* por solo **$10,000 MXN** (Ahorras $2,000). Envío incluido a todo México.")

c1, c2, c3 = st.columns([1.2, 4, 0.8], gap="small") 

with c1:
    if logo_main_b64:
        st.markdown(f'<img src="data:image/png;base64,{logo_main_b64}" style="width: 250px; filter: brightness(0);">', unsafe_allow_html=True)
    st.markdown("<p style='color:#000; font-family:Courier Prime; font-size:0.6rem; font-weight:bold;'>ESTUDIO DE ARTE / CDMX / 2026</p>", unsafe_allow_html=True)

with c2:
    st.markdown("<div style='margin-top: 60px;'>", unsafe_allow_html=True) 
    filtro_busq = st.text_input("", placeholder="ESCRIBE PARA BUSCAR...", key="search", label_visibility="collapsed").lower()
    st.markdown("</div>", unsafe_allow_html=True)

with c3:
    msg_gral = "Hola Said, visité tu galería web y me gustaría ponerme en contacto contigo.".replace(" ", "%20")
    redes_html = f'''<div style="display: flex; justify-content: flex-end; gap: 20px; margin-top: 52px;">
        <a href="https://wa.me/5215610810026?text={msg_gral}" target="_blank"><img src="data:image/png;base64,{icon_wa_b64}" style="width:18px; filter:brightness(0);"></a>
        <a href="https://www.instagram.com/saidmontano_/" target="_blank"><img src="data:image/png;base64,{icon_ig_b64}" style="width:18px; filter:brightness(0);"></a>
        <a href="https://www.tiktok.com/@saidmontano_" target="_blank"><img src="data:image/png;base64,{icon_tk_b64}" style="width:18px; filter:brightness(0);"></a>
    </div>'''
    st.markdown(redes_html, unsafe_allow_html=True)

# MENÚ DE TÉCNICAS (ACUARELA PRIMERO)
opciones = ["ACUARELA", "PINTURA AL OLEO", "DIBUJO", "ARTE DIGITAL", "ESCULTURA", "ESTUDIO"]
idx_tec = opciones.index(st.session_state.tec_ref) if st.session_state.tec_ref in opciones else 0
tecnica_sel = st.radio("", opciones, index=idx_tec, horizontal=True, label_visibility="collapsed")

if tecnica_sel != st.session_state.tec_ref:
    st.session_state.tec_ref = tecnica_sel
    st.session_state.pag_ref = 0
    st.query_params["t"] = tecnica_sel
    st.query_params["p"] = 0
    st.rerun()

# --- SOBRE EL ARTISTA (EXPANDER) ---
with st.expander("SOBRE EL ARTISTA"):
    col_foto, col_texto = st.columns([1, 3])
    with col_foto:
        foto_url = "https://raw.githubusercontent.com/artsades/galeria-said-montano/main/said_perfil.jpg"
        st.markdown(f'<div style="text-align: center;"><img src="{foto_url}" style="width: 150px; height: 150px; border-radius: 50%; object-fit: cover;"></div>', unsafe_allow_html=True)
    with col_texto:
        st.markdown("<div style='color: #000; font-family: Courier Prime; font-size: 16px;'>Said Montaño es un artista visual mexicano cuya práctica se centra en la pintura al óleo y la acuarela...</div>", unsafe_allow_html=True)

# SECCIÓN 4: GALERÍA DE OBRAS
# -----------------------------------------------------------------
archivos_csv = [f for f in os.listdir('.') if f.endswith('.csv')]
if archivos_csv:
    if 'datos_master' not in st.session_state:
        try: st.session_state.datos_master = pd.read_csv(archivos_csv[0], encoding='latin1')
        except: st.session_state.datos_master = pd.read_csv(archivos_csv[0], encoding='utf-8')
        st.session_state.datos_master.columns = [c.lower().strip() for c in st.session_state.datos_master.columns]

    df_f = st.session_state.datos_master.copy().dropna(subset=['tecnica'])
    seccion_actual = "proceso" if "ESTUDIO" in tecnica_sel.upper() else "galeria"
    df_f = df_f[df_f['seccion'] == seccion_actual]

    if filtro_busq:
        df_f = df_f[df_f.apply(lambda r: filtro_busq in str(r.get('titulo','')).lower() or filtro_busq in str(r.get('serie','')).lower(), axis=1)]

    palabra_clave = tecnica_sel.split()[-1].upper()
    df_f = df_f[df_f['tecnica'].str.upper().str.contains(palabra_clave, na=False)]

    if not df_f.empty:
        OBRAS_POR_PAGINA = 10
        total_paginas = (len(df_f) // OBRAS_POR_PAGINA) + (1 if len(df_f) % OBRAS_POR_PAGINA > 0 else 0)
        datos_galeria = df_f.iloc[st.session_state.pag_ref * OBRAS_POR_PAGINA : (st.session_state.pag_ref + 1) * OBRAS_POR_PAGINA]

        # --- FUNCIÓN VISOR CON SOPORTE PARA BOTÓN ATRÁS ---
        @st.dialog(" ", width="large")
        def visor_galeria(id_ref):
            st.markdown(f'<div style="display:flex; justify-content:space-between;"><div style="font-family:Courier Prime; font-size:0.7rem;">ARCHIVO VISUAL</div><img src="data:image/png;base64,{logo_main_b64}" style="width:100px; filter:brightness(0);"></div><hr>', unsafe_allow_html=True)
            st.image(f"assets/{id_ref}.jpg", use_container_width=True)
            # Botón para cerrar manualmente
            if st.button("VOLVER A LA GALERÍA"):
                st.query_params.clear()
                st.rerun()

        # Si hay una obra en la URL, abrimos el visor automáticamente
        if obra_en_url:
            visor_galeria(obra_en_url)

        cols = st.columns(5, gap="medium")
        for i, (idx, row) in enumerate(datos_galeria.iterrows()):
            with cols[i % 5]:
                id_obra = str(row.get('id_unico')).split('.')[0]
                ruta_img = f"assets/{id_obra}.jpg"
                
                if os.path.exists(ruta_img):
                    img_b64 = image_to_base64(ruta_img)
                    st.markdown(f"""<style>
                        div.st-key-btn_{id_obra} button {{
                            background-image: url("data:image/jpeg;base64,{img_b64}") !important;
                            background-size: cover !important;
                            height: 500px !important;
                            width: 100% !important;
                            border-radius: 0px !important;
                        }}
                    </style>""", unsafe_allow_html=True)

                    # AL HACER CLIC: Cambiamos la URL. Esto permite que el "Atrás" funcione.
                    if st.button("", key=f"btn_{id_obra}", use_container_width=True):
                        st.query_params["obra"] = id_obra
                        st.rerun()

                    # FICHA TÉCNICA
                    import re
                    solo_n = re.sub(r'[^0-9.]', '', str(row.get('precio', '0')))
                    precio_f = f"${float(solo_n):,.0f} MXN" if solo_n else "CONSULTAR"

                    st.markdown(f'''
                        <div style="font-family: 'Courier Prime'; border-top: 1px solid #000; padding-top: 5px;">
                            <p style="font-weight: bold; margin:0;">{row.get('titulo', 'S/T')}</p>
                            <p style="font-size: 0.7rem; margin:0;">SERIE: {row.get('serie', 'S/S')}</p>
                            <p style="font-weight: bold; margin-top: 5px;">{precio_f}</p>
                        </div>''', unsafe_allow_html=True)

        # PAGINACIÓN
        if total_paginas > 1:
            opciones_pag = [str(i+1) for i in range(total_paginas)]
            sel_p = st.radio("Páginas", opciones_pag, index=st.session_state.pag_ref, horizontal=True, key="pag_nav")
            if int(sel_p)-1 != st.session_state.pag_ref:
                st.session_state.pag_ref = int(sel_p)-1
                st.query_params["p"] = st.session_state.pag_ref
                st.rerun()

# PIE DE PÁGINA
st.markdown("<hr>", unsafe_allow_html=True)
f1, f2, f3 = st.columns(3)
with f2:
    if logo_main_b64:
        st.markdown(f'<div style="text-align: center;"><img src="data:image/png;base64,{logo_main_b64}" style="width:150px; filter:brightness(0);"></div>', unsafe_allow_html=True)
with f3:
    st.markdown("<p style='text-align:right; font-family:Courier Prime; font-size:0.7rem;'>© 2026 - SAID MONTAÑO</p>", unsafe_allow_html=True)
