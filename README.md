

# 🚴 Dashboard Penyewaan Sepeda

Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis data penyewaan sepeda berdasarkan berbagai faktor seperti musim, waktu dalam sehari, kondisi cuaca, dan hari kerja vs akhir pekan.

---
## 🛠 **Struktur Folder**
```
submission
├───dashboard
| └───dashboard.py
├───data
| ├───day.csv
| └───hour.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt

```

## 🛠 **Langkah-langkah Menjalankan Dashboard**

### **1️⃣ Clone Repository (Opsional)**
Jika Anda ingin menjalankan dari repository GitHub, gunakan perintah berikut:
```sh
git clone https://github.com/username/repository.git
cd repository
```

### **2️⃣ Buat Virtual Environment**
Disarankan untuk menggunakan virtual environment agar dependensi terisolasi:

#### **Windows**
```sh
python -m venv venv
venv\Scripts\activate
```

#### **Mac/Linux**
```sh
python3 -m venv venv
source venv/bin/activate
```

---

### **3️⃣ Install Dependensi**
Pastikan semua dependensi sudah diinstal dengan menjalankan perintah berikut:
```sh
pip install -r requirements.txt
```

### **4️⃣ Jalankan Aplikasi Streamlit**
Jalankan perintah berikut untuk menjalankan dashboard:
```sh
streamlit run app.py
```
Setelah dijalankan, Anda akan mendapatkan link seperti ini:
```
Local URL: http://localhost:8501
```
Buka link tersebut di browser untuk mengakses dashboard.

---

## 🎨 **Fitur dalam Dashboard**
✅ **Filter Rentang Waktu** – Pilih rentang waktu untuk analisis
✅ **Analisis Musim** – Lihat pengaruh musim terhadap jumlah penyewaan sepeda
✅ **Tren Waktu Sehari** – Analisis pola penyewaan berdasarkan jam
✅ **Kondisi Cuaca** – Pengaruh cuaca terhadap penyewaan sepeda


![image](https://github.com/user-attachments/assets/e9c01ec0-6b52-4558-aed1-b3cb50aafb17)
![image](https://github.com/user-attachments/assets/692191fb-5925-44e4-b2a7-bd99b98f7018)
![image](https://github.com/user-attachments/assets/924a0e9a-ea80-485a-a0ec-95e44cd46d33)
![image](https://github.com/user-attachments/assets/5fa9ecd1-d4c2-4c25-a679-c81c9fc1177a)
![image](https://github.com/user-attachments/assets/60f7983a-80a7-45ab-a95c-d36cd2746273)



