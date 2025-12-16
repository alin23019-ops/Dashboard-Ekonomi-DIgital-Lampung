import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# === LOAD DATA ===
df = pd.read_csv("D:\\projek magang\\hasil_implikasi_pasar.csv", sep=";")
df.columns = df.columns.str.strip()

st.title("📍 Profil Kabupaten/Kota")

# === PILIH KAB/KOTA ===
pilih = st.selectbox(
    "Pilih Kabupaten/Kota:",
    df["Kabupaten/Kota"].unique()
)

d = df[df["Kabupaten/Kota"] == pilih].iloc[0]

# === FUNGSI KONDISI & SARAN PASAR ===
def kondisi_dan_saran(cluster_label):
    if cluster_label == "Starter Digital":
        kondisi = "Kesadaran pasar digital masih rendah, penggunaan internet untuk transaksi belum optimal."
        saran = "Fokus edukasi pasar digital, literasi e-commerce, dan pemasaran produk lokal."
    elif cluster_label == "Potensi Digitalisasi Pasar":
        kondisi = "Pasar digital mulai berkembang, namun belum sepenuhnya mencerminkan pola konsumsi masyarakat."
        saran = "Penguatan pasar produk makanan dan peningkatan kualitas UMKM digital."
    elif cluster_label == "Potensi Pasar(Non Makanan)":
        kondisi = "Konsumsi non-makanan mulai dominan dan variasi produk online meningkat."
        saran = "Perluasan kategori non-makanan seperti fashion, elektronik, dan rumah tangga."
    elif cluster_label == "Pusat E-commerce":
        kondisi = "Pasar digital sudah matang dengan adopsi internet dan aktivitas e-commerce tinggi."
        saran = "Fokus pada branding, inovasi produk, dan ekspansi pasar nasional."
    else:
        kondisi = "-"
        saran = "-"
    return kondisi, saran

kondisi_pasar, saran_pasar = kondisi_dan_saran(d["Cluster_Label"])

# === RINGKASAN ATAS ===
colA, colB, colC = st.columns(3)
colA.metric("Klaster Pasar Digital", d["Cluster_Label"])
colB.metric("Klaster Konsumsi", d["cluster konsumsi"])
colC.metric("Total Toko Shopee", int(d["Total Toko Shopee"]))

st.divider()

# === DETAIL INFORMASI ===
col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 Internet & Aktivitas E-Commerce")
    st.write(f"- Penggunaan internet untuk **penjualan**: **{d['Persentase penggunaan internet sebagai alat Penjualan']}%**")
    st.write(f"- Penggunaan internet untuk **pembelian**: **{d['Persentase penggunaan internet sebagai alat Pembelian']}%**")

with col2:
    st.subheader("📌 Pola Konsumsi & Pasar")
    st.write(f"- Konsumsi Dominan: **{d['Konsumsi_Dominan']}**")
    st.write(f"- Kondisi Pasar Digital: **{kondisi_pasar}**")
    st.write(f"- Saran Pengembangan Pasar: **{saran_pasar}**")
