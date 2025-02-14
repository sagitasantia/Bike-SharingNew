

# 🚴 Dashboard Penyewaan Sepeda

Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis data penyewaan sepeda berdasarkan berbagai faktor seperti musim, waktu dalam sehari, kondisi cuaca, dan hari kerja vs akhir pekan.

---
## 🛠 **Struktur Folder**
```
submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───data_1.csv
| └───data_2.csv
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


![image](https://github.com/user-attachments/assets/00da83a7-a8b8-479b-a259-6c5a519a002e)
![image](https://github.com/user-attachments/assets/545aaedb-f73b-4797-8cc6-955382de7c1d)
![image](https://github.com/user-attachments/assets/2cab6086-21dd-4467-bea4-44caa47e50a6)
![image](https://github.com/user-attachments/assets/f567f1dc-a71a-4811-8b49-29199da50688)


