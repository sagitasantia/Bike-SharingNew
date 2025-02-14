import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from babel.numbers import format_currency
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Penyewaan Sepeda", page_icon="🚴", layout="wide")

# Load dataset
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Pastikan kolom 'dteday' bertipe datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Tambahkan kolom "Hari Kerja" atau "Akhir Pekan"
day_df["day_type"] = day_df["weekday"].apply(lambda x: "Hari Kerja" if x < 5 else "Akhir Pekan")

# Sidebar
st.sidebar.image("logo.png", use_container_width=True)
st.sidebar.header("Pilih Rentang Waktu")

# Rentang Waktu di Sidebar
min_date = day_df['dteday'].min().date()
max_date = day_df['dteday'].max().date()
start_date, end_date = st.sidebar.date_input(
    "Rentang Tanggal", 
    [min_date, max_date], 
    min_value=min_date, 
    max_value=max_date
)

# Konversi start_date dan end_date ke datetime64 agar bisa dibandingkan dengan DataFrame
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data berdasarkan rentang waktu yang dipilih
filtered_day_df = day_df[(day_df['dteday'] >= start_date) & (day_df['dteday'] <= end_date)]
filtered_hour_df = hour_df[(hour_df['dteday'] >= start_date) & (hour_df['dteday'] <= end_date)]

# Rata-rata Recency, Frequency, dan Monetary (day_df)
st.subheader("📊 Rata-rata Recency, Frequency, Monetary, dan Suhu")
col1, col2, col3, col4 = st.columns(4)  # Ubah jadi 4 kolom

with col1:
    avg_recency_day = round((filtered_day_df['dteday'].max() - filtered_day_df['dteday'].min()).days, 1)
    st.metric("Average Recency (days)", value=avg_recency_day)

with col2:
    avg_frequency_day = round(filtered_day_df.groupby("weekday")["cnt"].count().mean(), 2)
    st.metric("Average Frequency", value=avg_frequency_day)

with col3:
    avg_monetary_day = round(filtered_day_df.groupby("weekday")["cnt"].sum().mean(), 2)
    st.metric("Average Monetary", value=avg_monetary_day)

with col4:
    current_temp = filtered_day_df['temp'].mean()  # Ambil suhu rata-rata
    temp_change = filtered_day_df['temp'].diff().mean()  # Perubahan suhu rata-rata antar hari
    st.metric(label="Rata-rata Suhu", value=f"{round(current_temp, 1)} °C", delta=f"{round(temp_change, 1)} °C")


# **Visualisasi Recency, Frequency, dan Monetary per Weekday (day_df)**
st.subheader("📈 Best Customer Based on RFM Parameters (day_df)")
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20, 5))

sns.barplot(y="dteday", x="weekday", data=filtered_day_df.sort_values(by="dteday", ascending=True).head(5), palette="Blues_r", ax=ax[0])
ax[0].set_title("By Recency (days)")

sns.barplot(y="cnt", x="weekday", data=filtered_day_df.sort_values(by="cnt", ascending=False).head(5), palette="Blues_r", ax=ax[1])
ax[1].set_title("By Frequency")

sns.barplot(y="cnt", x="weekday", data=filtered_day_df.sort_values(by="cnt", ascending=False).head(5), palette="Blues_r", ax=ax[2])
ax[2].set_title("By Monetary")

st.pyplot(fig)

# **1️⃣ Bagaimana Pengaruh Musim terhadap jumlah penyewaan sepeda?**
st.subheader("🌤️ Pengaruh Musim terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='season', y='cnt', data=filtered_day_df, estimator='mean', palette='coolwarm', ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
ax.set_xlabel("Musim (1: Semi, 2: Panas, 3: Gugur, 4: Dingin)")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
st.pyplot(fig)

# **2️⃣ Apakah ada pola tertentu dalam jumlah penyewaan sepeda berdasarkan waktu dalam sehari?**
st.subheader("⏰ Pola Penyewaan Sepeda Berdasarkan Waktu dalam Sehari")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="hr", y="cnt", data=filtered_hour_df, estimator="mean", marker="o", color="red")
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
ax.set_xlabel("Jam (0-23)")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
st.pyplot(fig)

# **3️⃣ Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?**
st.subheader("☁️ Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='weathersit', y='cnt', data=filtered_day_df, estimator='mean', palette='viridis', ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
ax.set_xlabel("Kondisi Cuaca (1: Cerah, 2: Berawan, 3: Hujan, 4: Badai)")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
st.pyplot(fig)

# **4️⃣ Apakah ada perbedaan yang signifikan dalam jumlah penyewaan sepeda antara hari kerja dan akhir pekan?**
st.subheader("📆 Perbedaan Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="day_type", y="cnt", data=filtered_day_df, estimator="mean", palette="coolwarm", ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
ax.set_xlabel("Jenis Hari")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
st.pyplot(fig)


