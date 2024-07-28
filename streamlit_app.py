import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Aplikasi Input Data dengan Streamlit")

# Membuat form input
st.header("Masukkan Data")

# Input data
luas = st.number_input('Luas (m2)', min_value=0)
jumlah_kamar = st.number_input('Jumlah Kamar', min_value=0)
harga = st.number_input('Harga (Rp)', min_value=0)

# Tombol untuk menambahkan data ke DataFrame
if st.button('Tambahkan Data'):
    # Data baru
    data_baru = {'Luas': [luas], 'Jumlah_Kamar': [jumlah_kamar], 'Harga': [harga]}
    df_baru = pd.DataFrame(data_baru)
    
    # Menyimpan atau menampilkan DataFrame
    if 'dataframe' not in st.session_state:
        st.session_state.dataframe = df_baru
    else:
        st.session_state.dataframe = pd.concat([st.session_state.dataframe, df_baru], ignore_index=True)
    
    st.success("Data berhasil ditambahkan!")

# Menampilkan DataFrame
if 'dataframe' in st.session_state:
    st.header("DataFrame")
    st.dataframe(st.session_state.dataframe)
else:
    st.info("Belum ada data yang dimasukkan.")

# Tombol untuk menghapus data
if st.button('Hapus Semua Data'):
    if 'dataframe' in st.session_state:
        del st.session_state.dataframe
    st.success("Semua data berhasil dihapus.")
