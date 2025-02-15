## Dashboard Analisis Data Bike Sharing

import pandas as pd
import streamlit as st
import altair as alt


st.set_page_config(page_title="Dashboard Penyewaan Sepeda", page_icon="🚴", layout="wide")

# Load dataset terbaru
day_df = pd.read_csv('day_df_analisis.csv')
hour_df = pd.read_csv('hour_df_analisis.csv')

# Pastikan kolom 'dteday' bertipe datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Sidebar
st.sidebar.image("logo.png", use_container_width=True)
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
st.subheader("📊 Clustering Penyewaan Sepeda")
st.markdown("Kategori kepadatan penyewaan dibagi menjadi tiga:")
st.markdown("- **Rendah**: Penyewaan di bawah rata-rata")
st.markdown("- **Sedang**: Penyewaan mendekati rata-rata")
st.markdown("- **Tinggi**: Penyewaan jauh di atas rata-rata")

# Clustering berdasarkan kategori kepadatan harian
chart = alt.Chart(filtered_day_df).mark_bar().encode(
    alt.X('Kategori Kepadatan:N', title='Kategori Kepadatan Penyewaan'),
    alt.Y('count()', title='Jumlah Hari'),
    color='Kategori Kepadatan:N',
    tooltip=['Kategori Kepadatan', 'count()']
).properties(
    title='Distribusi Kategori Kepadatan Penyewaan Harian'
)
st.altair_chart(chart, use_container_width=True)

# Clustering berdasarkan kepadatan penyewaan per jam
chart = alt.Chart(filtered_hour_df).mark_bar().encode(
    alt.X('Kategori Kepadatan:N', title='Kategori Kepadatan Penyewaan per Jam'),
    alt.Y('count()', title='Jumlah Jam'),
    color='Kategori Kepadatan:N',
    tooltip=['Kategori Kepadatan', 'count()']
).properties(
    title='Distribusi Kategori Kepadatan Penyewaan per Jam'
)
st.altair_chart(chart, use_container_width=True)

# **Analisis Penyewaan Sepeda Berdasarkan Faktor-Faktor Lain**
st.subheader("📈 Analisis Penyewaan Sepeda")

# Pengaruh Musim terhadap Penyewaan
st.markdown("Kode Musim:")
st.markdown("- **1**: Musim Semi")
st.markdown("- **2**: Musim Panas")
st.markdown("- **3**: Musim Gugur")
st.markdown("- **4**: Musim Dingin")
chart = alt.Chart(filtered_day_df).mark_bar().encode(
    alt.X('season:N', title='Musim'),
    alt.Y('mean(cnt)', title='Rata-rata Penyewaan'),
    color='season:N',
    tooltip=['season', 'mean(cnt)']
).properties(
    title='Rata-rata Penyewaan Sepeda Berdasarkan Musim'
)
st.altair_chart(chart, use_container_width=True)

# Pola Penyewaan Sepeda Berdasarkan Jam
chart = alt.Chart(filtered_hour_df).mark_line().encode(
    alt.X('hr:O', title='Jam (0-23)'),
    alt.Y('mean(cnt)', title='Rata-rata Penyewaan'),
    tooltip=['hr', 'mean(cnt)'],
    color=alt.value('blue')
).properties(
    title='Pola Penyewaan Sepeda Berdasarkan Jam'
)
st.altair_chart(chart, use_container_width=True)

# Pengaruh Cuaca terhadap Penyewaan
st.markdown("Kode Kondisi Cuaca:")
st.markdown("- **1**: Cerah")
st.markdown("- **2**: Berawan")
st.markdown("- **3**: Hujan")
st.markdown("- **4**: Badai")
chart = alt.Chart(filtered_day_df).mark_bar().encode(
    alt.X('weathersit:N', title='Kondisi Cuaca'),
    alt.Y('mean(cnt)', title='Rata-rata Penyewaan'),
    color='weathersit:N',
    tooltip=['weathersit', 'mean(cnt)']
).properties(
    title='Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda'
)
st.altair_chart(chart, use_container_width=True)

# Perbandingan Hari Kerja dan Akhir Pekan
st.markdown("Kode Hari Kerja:")
st.markdown("- **0**: Akhir Pekan")
st.markdown("- **1**: Hari Kerja")
chart = alt.Chart(filtered_day_df).mark_bar().encode(
    alt.X('workingday:N', title='Hari Kerja (0=Akhir Pekan, 1=Hari Kerja)'),
    alt.Y('mean(cnt)', title='Rata-rata Penyewaan'),
    color='workingday:N',
    tooltip=['workingday', 'mean(cnt)']
).properties(
    title='Perbandingan Penyewaan Sepeda pada Hari Kerja vs. Akhir Pekan'
)
st.altair_chart(chart, use_container_width=True)

st.caption("© Sagitasantia")
