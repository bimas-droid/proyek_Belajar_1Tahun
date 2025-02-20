# Tugas: Kalkulator Pengelolaan Keuangan Sederhana

# Menyimpan data
data_transaksi = []

# tampilana pilihan menu
def menu_utama():
    print("\n=== Pengelolaan Keuangan Sederhana ===")
    menu = ["Menambahkan transaksi", "menampilkan daftar transaksi", "total saldo saat ini", "Menghapus transaksi tertentu", "Kembali"]
    for index, daftar_menu in enumerate(menu, start=1):
        print(f"{index}. {daftar_menu}")

# Menambahkan transaksi
def Menambahkan_transaksi():
    transaksi = ['Pemasukan', 'Pengeluaran']
    for index, pilihan in enumerate(transaksi, start=1):
        print(f'{index}. {pilihan}')

    # pemilihan
    memilih = str(input("Pilih jenis Transaksi(1/2): "))

    # Jika memilih 1
    if memilih == "1":
        nominal = int(input("\nberapa nominal anda: "))
        keterangan = str(input("Asal Pendapatan: "))
        data_transaksi.append({"jenis": "Pemasukan", "nominal": nominal, "keterangan": keterangan})
        print("data sudah masuk ke list ✅ ")

    elif memilih == "2":
        nominal = int(input("\nberapa nominal anda: "))
        keterangan = str(input("Asal Pengeluaran: "))
        data_transaksi.append({"jenis": "Pengeluaran", "nominal": nominal, "keterangan": keterangan})
        print("data sudah masuk ke list ✅ ")

    else:
        print("==="*10)
        print("\nInput yang anda masukan tidak sesuai dengan menu pemilihan ❌ ")
        print("==="*10)
        return
    
# menampilkan data transaksi
def menampilkan_data():
    for index, data in enumerate(data_transaksi, start=1):
        print(f'{index}. [{data["jenis"]}] {data["nominal"]} - {data["keterangan"]}')

# menampilkan transaksi 
def total_saldo():
    global data_transaksi
    transaksi_pemasukan = 0
    transaksi_pengeluaran = 0

    if not data_transaksi:
        print("saldo tidak ada")

    # logika transaksi 
    for transaksi in data_transaksi:
        if transaksi["jenis"] == "Pemasukan":
            transaksi_pemasukan += transaksi["nominal"] 
        elif transaksi["jenis"] == "Pengeluaran":
            transaksi_pengeluaran += transaksi["nominal"]

    total_saldo = transaksi_pemasukan - transaksi_pengeluaran
    print(f'total saldo anda Rp.{total_saldo:,}'.replace(",","."))

# menghapus data pilihan
def menghapus_transaksi_tertentu():
    global data_transaksi
    if not data_transaksi:
        print("Tidak ada data")
        return

    try:
        pilih = int(input("Berapa data transaksi yang ingin anda hapus: ")) -1 # mengurangi indeks
        if 0 <= pilih < len(data_transaksi):
            del data_transaksi[pilih]
            print("Data berhasil di hapus ❌ ")

        else:
            print("Nomor tidak viled")
    except ValueError:
        print("Harap masukan nomor yang benar")

# while true
while True:
    menu_utama()
    menjalankan = str(input("Pilih Program: "))
    print(" ")

    if menjalankan == "1":
        Menambahkan_transaksi()

    elif menjalankan == "2":
        menampilkan_data()

    elif menjalankan == "3":
        total_saldo()

    elif menjalankan == "4":
        menghapus_transaksi_tertentu()

    elif menjalankan == "5":
        print("trimakasih telah kesistem")
        break

    else:
        print("Perintah tidak ada di daftar tugas coba lagi ❌")
        continue