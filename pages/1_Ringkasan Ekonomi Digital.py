import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv("hasil_implikasi_pasar.csv", sep=";")
df.columns = df.columns.str.strip()

st.title("🔎 Ringkasan Umum")

total_toko = int(df["Total Toko Shopee"].sum())
total_umkm = int(df["umkm 2024"].sum())
rasio_umkm_digital = total_toko / total_umkm

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Jumlah Kabupaten/Kota",
    df["Kabupaten/Kota"].nunique()
)

col2.metric(
    "Internet untuk Penjualan (Rata-rata)",
    f"{df['Persentase penggunaan internet sebagai alat Penjualan'].mean():.2f}%"
)

col3.metric(
    "Internet untuk Pembelian (Rata-rata)",
    f"{df['Persentase penggunaan internet sebagai alat Pembelian'].mean():.2f}%"
)

col4.metric(
    "Total Toko Shopee (Sampel)",
    f"{total_toko:,}"
)

st.divider()

st.info("""
📌 **Catatan Analitis**

Rata-rata penggunaan internet sebagai alat **pembelian** lebih tinggi
dibandingkan penggunaannya sebagai alat **penjualan**.
Kondisi ini menunjukkan bahwa aktivitas ekonomi digital di Lampung
masih cenderung **bersifat konsumtif**, sementara pemanfaatan internet
sebagai sarana produksi dan pemasaran oleh pelaku usaha
belum optimal.
""")

