import streamlit as st

st.set_page_config(
    page_title="Dashboard Ekonomi Digital Lampung",
    layout="wide"
)

st.title("Dashboard Ekonomi Digital Lampung")
st.markdown("""
Dashboard ini menyajikan **analisis klaster pasar digital dan pola konsumsi**
kabupaten/kota di Provinsi Lampung menggunakan metode K-Means.

""")

st.info("""
📌 Catatan: \n
Dashboard ini menyajikan hasil klasterisasi dan analisis pasar digital
yang telah diolah sebelumnya sebagai dasar visualisasi dan pengambilan insight.
""")


st.caption("© Proyek Magang Mahasiswa Universitas Negeri Surabaya – Analisis Ekonomi Digital Lampung")
