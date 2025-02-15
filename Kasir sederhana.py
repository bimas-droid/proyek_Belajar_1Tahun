data_buah = {
   "Apel": 10000,
    "Jeruk": 8000,
    "Mangga": 12000,
    "Pisang": 5000,
    "Anggur": 25000,
    "Semangka": 15000,
    "Melon": 14000,
}

daftar_belanja = []

while True:
    print("\n==Daftar Nama Buah==")
    for buah in data_buah:
        print(f'-{buah}')

    permintaan = input("pilih buah apa yang ingin anda beli: ").title()

    # jika pembeli mengklik kembali maka akan ke close
    if permintaan == "Keluar" or permintaan == "Close" or permintaan == "Kembali" or permintaan == "Cukup":
        break

    # jika permintaan ada di dalam data buah
    if permintaan in data_buah:
        # menampilkan harga buah
        print(f'harga buah {permintaan} Rp.{data_buah[permintaan]} per Kg')
        beli = input('beli atau tidak: ').title()

        # jika pelanggan klik beli
        if beli == "Beli" or beli == "Ya" or beli == "Oke":
            per_kilo = float(input("Beli berapa Kilo: "))

            # rumus harga jual barang
            harga = (data_buah[permintaan]) * per_kilo
            daftar_belanja.append((permintaan, per_kilo, harga))
            print(f'buah {permintaan} sudah di masukkan dengan berat {per_kilo} dan harga {harga}')

        else:
            print("\n Kembali ke Menu")
    else:
        print(f"Buah {permintaan}, Tidak tersedia")

# menampilkan barang 
if daftar_belanja:
   print(f"\n ==Daftar Belanja==")
   for item in daftar_belanja:
        print(f'{item[0]} sebanyak {item[1]} .Kg dengan harga {item[2]}')