"""Soal: Sistem Rekomendasi Produk Sederhana
Lo diminta membuat sistem rekomendasi produk sederhana berdasarkan kategori yang dipilih pengguna.

Spesifikasi Program:
Buat daftar produk dalam bentuk struktur data yang cocok (bisa list atau dictionary).

Contohnya ada beberapa kategori: Elektronik, Fashion, Buku.
Setiap kategori punya beberapa produk.
Minta input dari user untuk memilih kategori produk yang diinginkan.

Tampilkan rekomendasi produk berdasarkan kategori yang dipilih.

Misalnya kalau user pilih "Elektronik", tampilkan beberapa produk seperti "Laptop", "Smartphone", dll.
(Opsional) Jika user tidak memasukkan kategori yang ada, berikan pesan error yang ramah dan minta input ulang.

(Bonus) Tambahkan fitur random recommendation! Jika user bingung, berikan rekomendasi acak dari semua kategori.

"""


# data product

"""Barang Elektronik"""

daftar_elektronik = [
    {"barang":"leptop Asus", "harga": 2000000},
    {"barang":"Henphone Vivo", "harga": 3000000},
    {"barang":"Tablet Samsung", "harga": 2000000},
    {"barang":"Henphone Xiomi", "harga": 3500000},
    {"barang":"Leptop Acer", "harga": 5000000},
    {"barang":"Leptop Lenovo LOQ", "harga": 12000000}
]

"""Barang Fashion"""

daftar_fashion = [
    {"barang": "Kaos", "harga": 120000},
    {"barang": "Celana Jeans", "harga": 250000},
    {"barang": "Hoodie", "harga": 300000},
    {"barang": "Jaket", "harga": 450000},
    {"barang": "Sepatu Sneakers", "harga": 750000},
    {"barang": "Topi", "harga": 100000},
    {"barang": "Kacamata Hitam", "harga": 200000},
    {"barang": "Jam Tangan", "harga": 500000},
    {"barang": "Tas Ransel", "harga": 350000},
    {"barang": "Sweater", "harga": 280000},
    {"barang": "Celana Pendek", "harga": 180000},
    {"barang": "Sandal", "harga": 220000},
    {"barang": "Gaun", "harga": 400000},
    {"barang": "Rok", "harga": 230000},
    {"barang": "Kaos Kaki", "harga": 50000}
]

"""Barang Buku Literasi"""

daftar_buku = [
    {"barang": "Pemrograman Python untuk Pemula", "harga":  150000},
    {"barang": "Dasar-Dasar Machine Learning", "harga":  200000},
    {"barang": "Algoritma dan Struktur Data", "harga":  175000},
    {"barang": "Belajar AI dengan Python", "harga":  250000},
    {"barang": "Matematika untuk Data Science", "harga":  180000},
    {"barang": "Pemrograman Web Full Stack", "harga":  300000},
    {"barang": "Prinsip-Prinsip Ekonomi", "harga":  100000},
    {"barang": "AI untuk Bisnis", "harga":  225000},
    {"barang": "Teknik Pembelajaran Mendalam", "harga": 350000},
    {"barang": "Pengenalan Internet of Things", "harga": 130000}
]

"""Penyimpan data"""
data_elektronik = []
data_fashion = []
data_buku = []

def sambutan():
    print("====" * 13)
    print("Selamat datang di sistem rekomendasi produk!")
    print("Kategori yang tersedia: Elektronik, Fashion, Buku")
    print("====" * 13)
    print("")

while True:
    sambutan()
    
    pilih_kategori = input("Masukkan kategori yang Anda inginkan: ").title().strip()

    """Logika Pemrograman"""
    if pilih_kategori == "Elektronik":
        print("\nBerikut daftar produk untuk kategori Elektronik:\n")
        print("==" * 30)

        # Format rata kanan
        max_len_barang = max(len(item['barang']) for item in daftar_elektronik)
        max_len_harga = max(len(f"Rp {item['harga']:,.0f}") for item in daftar_elektronik)

        for data in daftar_elektronik:
            harga_format = f"Rp. {data['harga']:,}".replace(",", ".")
            print(f"Barang: {data['barang'].ljust(max_len_barang + 1)} Harga: {harga_format.rjust(max_len_harga + 4)}")

        print("==" * 30)
        
        # Menerima jumlah barang yang ingin dipilih
        barang_yang_dipilih = int(input("\nBerapa jumlah barang yang akan Anda pilih? "))

        count = 0
        while count < barang_yang_dipilih:
            nama_barang = input("Masukkan nama barang: ").strip()

            # Cari barang di daftar elektronik
            barang_ditemukan = next((item for item in daftar_elektronik if item["barang"].lower() == nama_barang.lower()), None)

            if barang_ditemukan:
                # Tambahkan barang dengan harga aslinya
                data_elektronik.append({"barang": barang_ditemukan["barang"], "harga": barang_ditemukan["harga"]})
                print(f"✅ {barang_ditemukan['barang']} berhasil ditambahkan dengan harga Rp {barang_ditemukan['harga']:,}.\n")
                count += 1
            else:
                print("⚠️ Barang tidak ditemukan, pastikan penulisan benar!\n")

            print("\nBarang yang Anda pilih telah ditambahkan!")
        print("Daftar barang yang sudah dipilih:")

        total_harga = 0 # menampilkan total harga

        """Menampilkan barang yang di pilih"""
        for item in data_elektronik:
            print(f"- {item['barang']} (Rp {item['harga']:,})")

        total_harga += item['harga']
        print(f"Total Harga: Rp.{total_harga:,}\n") #Menampilkan total harga keseluruhan
        break

    elif pilih_kategori == "Fashion":
        print("\nBerikut daftar produk untuk kategori Fashion:\n")
        print("==" * 28)

        # Format rata kanan
        max_len_barang = max(len(item['barang']) for item in daftar_fashion)
        max_len_harga = max(len(f"Rp {item['harga']:,.0f}") for item in daftar_fashion)

        for data in daftar_fashion:
            data_harga = f'Rp.{data["harga"]:,}'.replace(",",".")
            print(f"Barang: {data['barang'].ljust(max_len_barang + 1)} Harga: {data_harga.rjust(max_len_harga + 1)}")
        print("==" * 28)

        # permintaan untuk jumblah barang 
        barang_yang_dipilih = int(input("Berapa barang yang akan anda piih: "))
        count = 0
        
        while count < barang_yang_dipilih:
            nama_fashion = input("Masukkan nama barang: ").strip()

            # Memilih fashion
            barang_ditemukan = next((item for item in daftar_fashion if item["barang"].lower() == nama_fashion.lower()), None)

            if barang_ditemukan:
                data_fashion.append({"barang":barang_ditemukan["barang"], "harga":barang_ditemukan["harga"]})
                print(f"fashion: {barang_ditemukan['barang']} Berhasil di tambahkan, dengan harga: Rp{barang_ditemukan['harga']:,} ✅ \n")
                count += 1

            else:
                print("⚠ Barang tidak ada silahkan masukan format yang benar")
            print("Barang ditambahkan")
        print("barang yang di pilih")

        """Menampilkan total harga"""
        total_harga = 0

        for item in data_fashion:
            print(f'- Fashion: {item["barang"]} harga: (Rp.{item["harga"]:,})')

        total_harga += item["harga"]
        print(f"Total harga: (Rp.{total_harga:,})\n")
        break

    elif pilih_kategori == "Buku":
        print("Berikut beberapa produk yang tersedia: ")
        print("=="*31)

        """Format rata kanan"""
        max_len_barang = max(len(item["barang"]) for item in daftar_buku)
        max_len_harga = max(len(f'Rp.{item["harga"]:,.0f}') for item in daftar_buku)

        for data in daftar_buku:
            data_format = f'Rp. {data["harga"]:,}'.replace(",",".")
            print(f"Barang: {data['barang'].ljust(max_len_barang + 1)} Harga:{data_format.rjust(max_len_harga + 4)}")
        print("==" * 31)

        # Barang yang dipilih
        barang_dipilih = int(input("Berapa barang yang di pilih: "))
        count = 0

        while count < barang_dipilih:
            pilih_buku = input("Buku apa yang anda pilih: ").strip()

            barang_ditemukan = (next((item for item in daftar_buku if item["barang"].lower() == pilih_buku.lower()), None))

            if barang_ditemukan:
                data_buku.append({"barang": pilih_buku, "harga": barang_ditemukan["harga"]})
                print("buku berhasil di tambahkan")
                print(f"Buku {pilih_buku.lower()} berhasil di tambahkan harga: Rp.{barang_ditemukan['harga']:,}✅\n")
                count += 1

            else:
                print("Barang tidak ada")
        print("Barang yang di pilih ")

        """Menampilkan barang yang di pilih"""
        total_harga = 0

        for index, buku in enumerate(data_buku, start=1):
            print(f'{index}. {buku["barang"]} Harga: Rp.{buku["harga"]:,}')

        total_harga += buku["harga"]
        print(f'Harga total: (Rp.{total_harga:,})\n')
        break
