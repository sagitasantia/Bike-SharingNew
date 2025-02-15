import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Dashboard Penyewaan Sepeda", page_icon="🚴", layout="wide")

# Load dataset terbaru
day_df = pd.read_csv('day_df_analisis.csv')
hour_df = pd.read_csv('hour_df_analisis.csv')


day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Sidebar
st.sidebar.image("logo.png")  
st.sidebar.header("Pilih Rentang Waktu")

min_date = day_df['dteday'].min().date()
max_date = day_df['dteday'].max().date()
start_date, end_date = st.sidebar.date_input(
    "Rentang Tanggal", 
    [min_date, max_date], 
    min_value=min_date, 
    max_value=max_date
)

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

filtered_day_df = day_df[(day_df['dteday'] >= start_date) & (day_df['dteday'] <= end_date)]
filtered_hour_df = hour_df[(hour_df['dteday'] >= start_date) & (hour_df['dteday'] <= end_date)]

# **Clustering Penyewaan Sepeda**
st.subheader("📊  Penyewaan Sepeda ")
st.markdown("Kategori kepadatan penyewaan dibagi menjadi tiga:")
st.markdown("- **Rendah**: Penyewaan di bawah rata-rata")
st.markdown("- **Sedang**: Penyewaan mendekati rata-rata")
st.markdown("- **Tinggi**: Penyewaan jauh di atas rata-rata")

# Visualisasi Clustering dengan seaborn
fig, ax = plt.subplots(figsize=(8, 4))
sns.countplot(data=filtered_day_df, x='Kategori Kepadatan', palette="Blues", order=['Rendah', 'Sedang', 'Tinggi'], ax=ax)
ax.set_title("Distribusi Kategori Kepadatan Penyewaan Harian")
st.pyplot(fig)

# **Analisis Penyewaan Sepeda Berdasarkan Faktor-Faktor Lain**
st.subheader("📈 Analisis Penyewaan Sepeda")

# Pengaruh Musim terhadap Penyewaan
fig, ax = plt.subplots(figsize=(6, 4))
season_labels = ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin']
sns.barplot(data=filtered_day_df, x='season', y='cnt', estimator=np.mean, palette='blue', ax=ax)
ax.set_xticklabels(season_labels)
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Pola Penyewaan Sepeda Berdasarkan Jam
fig, ax = plt.subplots(figsize=(8, 4))
sns.lineplot(data=filtered_hour_df, x='hr', y='cnt', estimator=np.mean, color='blue', ax=ax)
ax.set_title("Pola Penyewaan Sepeda Berdasarkan Jam")
ax.set_xlabel("Jam (0-23)")
st.pyplot(fig)

# Pengaruh Cuaca terhadap Penyewaan
fig, ax = plt.subplots(figsize=(6, 4))
weather_labels = ['Cerah', 'Berawan', 'Hujan', 'Badai']
sns.barplot(data=filtered_day_df, x='weathersit', y='cnt', estimator=np.mean, palette='coolwarm', ax=ax)
ax.set_xticklabels(weather_labels)
ax.set_title("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
st.pyplot(fig)

# Perbandingan Hari Kerja dan Akhir Pekan
fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(data=filtered_day_df, x='workingday', y='cnt', estimator=np.mean, palette='coolwarm', ax=ax)
ax.set_xticklabels(["Akhir Pekan", "Hari Kerja"])
ax.set_title("Perbandingan Penyewaan Sepeda pada Hari Kerja vs. Akhir Pekan")
st.pyplot(fig)

st.caption("© Sagitasantia")
