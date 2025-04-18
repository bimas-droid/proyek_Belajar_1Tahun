import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Setup Data"""
# Data nilai siswa
data = {
    "Nama": ['Budi', 'Sari', 'Ani', 'Joko', 'Lina'],
    "Matematika": [80, 90, 70, 85, 75],
    "Bahasa Inggris": [75, 95, 60, 80, 70],
    "IPA": [85, 90, 65, 70, 80],
    "Rangking": [1,2,3,4,5]
}

# Buat data frame
df = pd.DataFrame(data)
print("📄 Data Nilai Siswa:")
print(df)


"""Analisis Data Pakai NumPy"""
# Ambil hanya kolom nilai 
nilai = df[['Matematika', 'Bahasa Inggris', 'IPA']].to_numpy()

# Hitung rata rata, maksimum, minimum, minimum tiap siswa
rata2_siswa = np.mean(nilai, axis=1)
max_siswa = np.max(nilai, axis=1)
min_siswa = np.min(nilai, axis=1)

# Tambahkan ke DataFrame
df['Rata-rata'] = rata2_siswa
df['Tertinggi'] = max_siswa
df['Terendah'] = min_siswa

print("\n📊 Data Setelah Analisis:")
print(df)


"""Visualisasi Data dengan Matplotlib"""
# Grafik Rata-rata per Siswa
plt.figure(figsize=(8,5))
plt.bar(df['Nama'], df['Rata-rata'], color='skyblue')
plt.title("Rata-rata Nilai Siswa")
plt.xlabel("Nama Siswa")
plt.ylabel("Nilai")
plt.ylim(10, 100)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()