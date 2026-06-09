import streamlit as st
import os
import base64

# Setup dasar halaman supaya responsif di HP
st.set_page_config(page_title="ARM Technology | Link in Bio", page_icon="🔗", layout="centered")

# --- CUSTOM CSS FIX CENTERED & BULAT SEMPURNA ---
st.markdown("""
    <style>
    /* Membatasi lebar konten utama agar pas seperti tampilan HP dan pas di tengah */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 450px;
        margin: 0 auto;
    }
    
    /* Memaksa elemen tombol bawaan Streamlit agar Center & Full Width */
    .stElementContainer, .stButton, div[data-testid="stButton"], div.stLinkButton {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
    }
    
    /* Desain tombol utama biar mirip Linktree */
    div[data-testid="stButton"] button, div.stLinkButton a {
        background-color: #1e63d3 !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        height: 55px !important;
        width: 100% !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1) !important;
        transition: all 0.3s ease !important;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none; /* Hilangkan garis bawah untuk link */
    }
    
    /* Efek hover tombol */
    div[data-testid="stButton"] button:hover, div.stLinkButton a:hover {
        background-color: #154fa6 !important;
        color: white !important;
        transform: translateY(-2px) !important;
    }
    
    /* Memastikan teks teks berada di tengah */
    .centered-text {
        text-align: center;
    }
    
    /* FIX FOTO BULAT SEMPURNA (Meskipun foto aslinya memanjang/persegi panjang) */
    .profile-pic {
        border-radius: 50% !important;
        object-fit: cover !important;
        aspect-ratio: 1 / 1 !important; /* Memaksa rasio kotak 1:1 sebelum dibulatkan */
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. PROFIL & DESKRIPSI ---
nama_file_foto = "CV1.jpg" 

if os.path.exists(nama_file_foto):
    with open(nama_file_foto, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(f'<p class="centered-text"><img class="profile-pic" src="data:image/png;base64,{encoded}" width="140"></p>', unsafe_allow_html=True)
else:
    avatar_url = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    st.markdown(f'<p class="centered-text"><img class="profile-pic" src="{avatar_url}" width="140"></p>', unsafe_allow_html=True)

# Nama ARM Technology
st.markdown('<h1 class="centered-text" style="margin-bottom: 0; font-size: 28px;">ARM Technology</h1>', unsafe_allow_html=True)
st.markdown('<p class="centered-text" style="color: gray; font-size: 15px; margin-top: 5px;">Beyond Just An Idea | We Make Your Idea Alive</p>', unsafe_allow_html=True)

# --- 2. ICON SOSIAL MEDIA ---
st.markdown("""
<p class="centered-text" style="font-size: 26px; word-spacing: 15px; margin-top: 15px; margin-bottom: 25px;">
    <a href="#" target="_blank" style="text-decoration:none;">📸</a>
    <a href="#" target="_blank" style="text-decoration:none;">💼</a>
    <a href="#" target="_blank" style="text-decoration:none;">💻</a>
    <a href="#" target="_blank" style="text-decoration:none;">💬</a>
</p>
""", unsafe_allow_html=True)

# --- 3. MENU UTAMA ---

# Menu 1: About Me (Buka CV)
if "buka_cv" not in st.session_state:
    st.session_state.buka_cv = False

if st.button("🧑‍💻 About Me"):
    st.session_state.buka_cv = not st.session_state.buka_cv

# Tempat munculin Gambar CV lu kalau tombol "About Me" diklik
if st.session_state.buka_cv:
    st.write("")
    nama_file_cv = "profile.jpeg"  
    if os.path.exists(nama_file_cv):
        st.image(nama_file_cv, use_container_width=True)
    else:
        st.warning("Gambar CV belum ditaruh di folder. Pastikan file gambar CV lu namanya sesuai ya!")

st.write("") # Jarak antar tombol

# Menu 2: Link TikTok (Sudah di-fix tampilan sama dengan About Me)
link_tiktok = "https://www.tiktok.com/@arief_mfdhl?is_from_webapp=1&sender_device=pc"

st.link_button("🎵 TikTok", link_tiktok, type="primary") # Gunakan st.link_button asli
