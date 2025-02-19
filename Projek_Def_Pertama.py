"""
Buat program untuk menyimpan data produk di sebuah toko. Program harus bisa:

Menambahkan produk (nama & harga).
Menampilkan semua produk.
Menghapus produk dari daftar.
Keluar dari program.
"""

# Toko sederhana

# data inisialisasi penerimaan barang
data_barang = {}

# menampilkan menu
def menampilkan_menu():
    print("\n=== Menu Utama ===")

    # List menu
    menu = ["Tambah Produk", "Tampilkan Produk", "Hapus Produk", "Kembali"]
    for index, item in enumerate(menu, start=1):
        print("-", index, item )

# Menambah produk
def menambahkan_produk():
    # menambahkan barang
    nama_barang = str(input("Nama Barang: ")).title()
    harga_barang = input("Harga Barang: ")
    data_barang[nama_barang] = harga_barang # Memasukkan barang ke toko
    print("Barang Telah Masuk Ke Toko ✅ ") # menampilkan ceklis barang jika sudah selesai proses

# Menampilkan produk
def Menampilkan_produk():
    if not data_barang:
        print('\nBarang Kosong ❌')
        print("----"*8)

    # Jika Barang ada
    else:
        for nomor, (nama_barang, harga_barang) in enumerate(data_barang.items(), start=1):
            print(" ")
            print("==="*8)
            print(f"{nomor}. {nama_barang} : {harga_barang}")
            print("==="*8)

# menghapus barang dari toko
def menghapus_produk():
    # Jika barang tidak ada 
    if not data_barang:
        print("Barang Kosong")
        print("----"*8)
        return

    nama = input("sebutkan nama barang: ").title()
    del data_barang[nama]

    print(f"\n{nama} berhasil di hapus dari daftar ❌ ")

# keluar secara otomatis
def keluar():
    print('Trimakasih Telah Mengunjungi')

# while true
while True:
    menampilkan_menu()
    masukkan = str(input("Masukkan Pilihan: "))

    if masukkan == "1":
        menambahkan_produk()

    elif masukkan == "2":
        Menampilkan_produk()

    elif masukkan == "3":
        menghapus_produk()
    
    elif masukkan == "4":
        keluar()
        break

    else:
        print("Menu Yang Anda Masukan Tidak Terdaftar Di Sistem ❌")