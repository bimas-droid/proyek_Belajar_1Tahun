"""
Program Mengelola Menu Restoran (Looping & List)

Deskripsi:
Buatlah program Python untuk mengelola daftar menu restoran. Program harus memiliki fitur sebagai berikut:

Menampilkan daftar menu makanan
Menampilkan daftar menu minum
Menambahkan menu baru ke daftar.
Menghapus menu dari daftar berdasarkan nama menu.
Menampilkan menu pesanan.
"""

menu_makanan = [
    {"makanan": "Nasi Goreng", "harga": 10000},
    {"makanan": "Ayam Goreng", "harga": 15000},
    {"makanan": "Ayam Bakar", "harga": 25000}
]

menu_minuman = [
    {"minuman": "Es Teh", "harga": 5000},
    {"minuman": "Es Jeruk", "harga": 5000},
    {"minuman": "Es Buah", "harga": 15000}
]

keranjang_pesanan = []

# Memilih menampilkan menu makanan atau minuman
def memilih_menu():
    print("\n=== Selamat Datang Di Restoran Kami ===")
    menu = ["makanan", "minuman", "Menambahkan menu baru ke daftar", "Menghapus menu dari daftar ", "Menampilkan Pesanan" ]
    for index, pilih in enumerate(menu, start=1):
        print(f"{index}. {pilih}")

# menampilkan daftar menu yang tersedia
def menampilkan_daftar_makanan():

    print("==="*7)
    print("=== Menu Makanan ===")
    print("==="*7)
    # Menambahkan angka urutan di dalam daftar list makanan
    for index,nama in enumerate(menu_makanan, start=1):
        print(f"{index}. {nama['makanan']} Rp.{nama['harga']}")

def menampilkan_daftar_minuman():

    print("==="*7)
    print("=== Menu Minuman ===")
    print("==="*7)

    # Menambahkan angka urut di dalam daftar list minuman
    for index, nama in enumerate(menu_minuman, start=1):
        print(f"{index}. {nama['minuman']} Rp.{nama['harga']}")

# menambah menu baru ke daftar 
def menambah_menu_baru():

    pilihan = ["Makanan", "Minuman"]
    # membuat susun kebawah dan juga menambahkan angka urut
    for nomer, menu in enumerate(pilihan, start=1):
        print(f"{nomer}. {menu}")

    memilih_menu = str(input("Menu mana yang ingin anda tambahkan: "))
    
        # pelihan
    if memilih_menu == "1":

        # meminta memasukkan menu baru
        masukkan_menu = str(input("Menu apa yang ingin anda tambahkan tuan 🤔: ")).title()
        harga = int(input("berapa harganya: ")) # Meminta memberi harga yang akan di pasarkan

        # Menambahkan menu yang di minta ke daftar list
        menu_makanan.append({"makanan": masukkan_menu, "harga" : harga})
         # apresasi
        print("Menu sudah masuk ke daftar list ✅ ")

    elif memilih_menu == "2":
        # meminta memasukkan menu baru
        masukkan_menu = str(input("Menu apa yang ingin anda tambahkan tuan 🤔: ")).title()
        harga = int(input("berapa harganya: ")) # Meminta memberi harga yang akan di pasarkan

        # Menambahkan menu yang di minta ke daftar list
        menu_minuman.append({"minuman": masukkan_menu, "harga": harga})
        # apresasi
        print("Menu sudah masuk ke daftar list ✅ ")

# Menghapus menu dari daftar menu
def menghapus_menu():
    menu_clear = str(input("menu apa yang ingin anda hapus: "))
    # mencari data
    mencari = False

    for menu in keranjang_pesanan:
        if menu_clear == menu["minuman"] or menu_clear == menu["makanan"]:
            keranjang_pesanan.remove(menu_clear)
            print(f"pesanan {menu_clear} telah di batalkan ✅")
            # di saat ketemu yang di cari
            mencari = True

            # Memberi pertanyaan ulang
            pertanyaan = str(input("apakah masih ada lagi yang ingin anda hapus? ")).title()

            if pertanyaan == "Ya" or pertanyaan == "Iya":
                continue

            else:
                ("trimakasih atas pemesanannya, pesanan anda akan kami kirim, silahkan menunggu ✅")
                break


        if not mencari:
            print("Pesanan yang anda masukkan memang tidak anda pesan ")
            

# menapilkan menu setelah berubah
def menampilkan_pesanan():
    global keranjang_pesanan
    print("\n===== Pesanan anda =====")

    total_harga = 0 #Menghitung total

    for index, pesanan in enumerate(keranjang_pesanan, start=1):
        nama_barang = pesanan.get("makanan", pesanan.get("minuman", "tidak di ketahui"))
        harga = pesanan["harga"]

        print(f'{index}. {nama_barang} Rp {harga:,}'.replace(",","."))
        # Menambahkan harga
        total_harga += harga

    print("==="*9)
    print(f"Total harga: Rp {total_harga:,}".replace(",","."))



# While True
while True:
    memilih_menu()
    pilih_menu = str(input("Pilih menu yang anda ingin pesan: "))

    try:
        #Logika pemilihan menu
        if pilih_menu == "1":
            # memanggil fungsi
            menampilkan_daftar_makanan()
            pilih_makanan = str(input("Makanan apa yang ingin anda pesan: ")) # Memilih menu makanan yang ada

            # Jika pesanan no 1
            if pilih_makanan == "1":
                print("Pesanan sukses ✅\n")
                keranjang_pesanan.append({"makanan": "Nasi goreng", "harga": 10000})
            
            # Jika pesanan no 2
            elif pilih_makanan == "2":
                print("Pesanan sukses ✅\n")
                keranjang_pesanan.append({"makanan": "Ayam Goreng", "harga": 15000})
            
            # Jika pesanan no 3
            elif pilih_makanan == "3":
                print("Pesanan sukses ✅\n")
                keranjang_pesanan.append({"makanan": "Ayam Bakar", "harga": 25000})

            else:
                print("sintak yang anda masukkan tidak ada di menu")
    

        elif pilih_menu == "2":
            menampilkan_daftar_minuman()

            pilih_minuman = str(input("Minumas apa yang ingin anda pesan: ")) # Memilih menu minuman yang ada

            # Jika pesanan no 1
            if pilih_minuman == "1":
                print("Pesanan sukses ✅\n")
                keranjang_pesanan.append({"minuman": "Es Teh", "harga": 5000})

            # Jika pesanan no 2
            elif pilih_minuman == "2":
                print("Pesanan sukses ✅\n")
                keranjang_pesanan.append({"minuman": "Es Jeruk", "harga": 5000})
            # Jika pesanan no 1
            elif pilih_minuman == "3":
                print("Pesanan sukses ✅\n")
                keranjang_pesanan.append({"minuman": "Es Campur", "harga": 10000})

            # Jika pilihan tidak sama dengan menu 
            else:
                print("pilihan yang anda masukkan tidak ada di menu")
        else:
            print("")

    except NameError as e:
        print(f"Terjadi kesalahan: Variabel belum didefinisikan! ({e})")

    except ValueError as e:
        print(f"Input tidak valid! Masukkan angka yang benar. ({e})")

    except Exception as e:
        print(f"Terjadi error yang tidak terduga: {e}")


    if pilih_menu == "3":
        menambah_menu_baru()

    elif pilih_menu == "4":
        menghapus_menu()

    elif pilih_menu == "5":
        menampilkan_pesanan()
