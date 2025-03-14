"""Pertanyaan"""

pilihan = ["ya", "tidak"]


def menu_pilihan():
    for index, string in enumerate(pilihan, start=1):
        print(f"{index}. {string}")


"""Hitung Pajak PBB Sederhana"""
# meminta input
luas_tanah = int(input("Masukkan luas tanah: "))
harga_per_m = int(input("Harga tanah: "))

"""Rumus Perhitungan PBB"""

NJOP = luas_tanah * harga_per_m  # Nilai Jual Objek Pajak
PBB = (NJOP * 0.5) - 15000  # Nilai persekutuan besar


if PBB < 15000:
    print("Tidak perlu membayar PBB")

else:
    print("Anda memiliki 5x kesempatan menebak")

    maximal = 5
    loading = 0
    while loading < maximal:
        tebak_nominal = int(input("Berapa menurut anda: Rp. "))

        if tebak_nominal > PBB:
            print("Nominal terlalu besar")
            loading += 1  # Menambah jumblah

        elif tebak_nominal < PBB:
            print("Nominal terlalu kecil")
            loading += 1  # Menambah jumblah

        elif tebak_nominal == PBB:
            print("selamat kamu benar")
            break

        if loading == 4:
            print("Apakah mau tampilkan: ")
            menu_pilihan()

            pilihan = str(input("Masukkan program: "))

            if pilihan == "1":
                print(f"anda harus membayar Rp.{PBB:,}".replace(",", "."))
                break
            elif pilihan == "2":
                print("Oke selamat berjuang ✅")
                break
            else:
                print("tolong masukkan angka")
                continue
