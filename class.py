class mobil:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna

    def tampilkan_info(self):
        print(f'\nmerek mobil: {self.merk}')
        print(f'tahun mobil: {self.tahun}')
        print(f'warna mobil: {self.warna}')

# meminta input
merek_m = str(input("masukkan merek mobil: ")).title()
tahun_m = int(input("Masukkan tahun keluar mobil: "))
warna_m = str(input("masukkan warna mobil: ")).title()

# Memasukkan input ke dalam inisial
gabungan = mobil(merek_m, tahun_m, warna_m)

# menampilkannya 
gabungan.tampilkan_info()