# Kelas Buku
class Buku:
    def __init__(self, judul, tahun_terbit):
        self.judul = judul.title()
        self.tahun_terbit = tahun_terbit

    def pop_up(self):
        return f'Buku "{self.judul}" ({self.tahun_terbit}) ditambahkan ke daftar ✅'

# Kelas Pembaca
class Pembaca:
    def __init__(self, nama, usia):
        self.nama = nama.title()
        self.usia = usia

# Daftar buku di perpustakaan
list_buku_pengembangan_diri = [
    "Atomic Habits", "The 7 Habits Of Highly Effective People", "The Power Of Now", "Think And Grow Rich",
    "Grit: The Power Of Passion And Perseverance", "The Subtle Art Of Not Giving A F*ck", "How To Win Friends And Influence People",
    "Deep Work", "Ikigai: The Japanese Secret To A Long And Happy Life", "The Psychology Of Money",
    "Mindset: The New Psychology Of Success", "The 5 AM Club", "Make Your Bed", "Can't Hurt Me", "Dare To Lead"
]

# Daftar buku yang sudah dibaca
list_buku_dibaca = []

def tampilkan_menu():
    print("\nSilakan Pilih Menu:")
    print("1. Membaca Buku")
    print("2. Periksa Orang yang Sudah Membaca Buku")
    print("3. Keluar")

def pilih_buku():
    print("\nDaftar Buku yang Tersedia:")
    for index, judul in enumerate(list_buku_pengembangan_diri, start=1):
        print(f"{index}. {judul}")
    
    pilihan = input("Pilih buku berdasarkan nomor atau judul: ")
    
    # Jika input berupa angka (nomor buku)
    if pilihan.isdigit():
        index_buku = int(pilihan) - 1
        if 0 <= index_buku < len(list_buku_pengembangan_diri):
            return list_buku_pengembangan_diri[index_buku]
        else:
            print("Nomor buku tidak valid ❌")
            return None
    else:
        judul_buku = pilihan.title()
        if judul_buku in list_buku_pengembangan_diri:
            return judul_buku
        else:
            print("Buku tidak ditemukan ❌")
            return None

def tampilkan_pembaca():
    if not list_buku_dibaca:
        print("\nBelum ada yang membaca buku")
    else:
        print("\nDaftar Pembaca:")
        for pembaca in list_buku_dibaca:
            print(f"{pembaca['nama']} membaca \"{pembaca['membaca']}\"")

# Program utama
while True:
    nama = input("Masukkan nama Anda: ").strip()
    usia = input("Masukkan usia Anda: ").strip()
    
    if not usia.isdigit():
        print("Usia harus berupa angka ❌")
        continue
    
    usia = int(usia)
    
    if usia <= 10:
        print("Anda belum memenuhi syarat untuk mengakses perpustakaan ❌")
        break
    
    print(f"Selamat {nama}, Anda memenuhi kriteria ✅\n")
    
    pembaca = Pembaca(nama, usia)
    
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan nomor pilihan: ").strip()
        
        if pilihan == "1":
            buku_terpilih = pilih_buku()
            if buku_terpilih:
                list_buku_dibaca.append({"nama": pembaca.nama, "membaca": buku_terpilih})
                print(f"Selamat membaca \"{buku_terpilih}\" ✅")
        elif pilihan == "2":
            tampilkan_pembaca()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan perpustakaan! 👋")
            exit()
        else:
            print("Pilihan tidak valid, silakan coba lagi ❌")
