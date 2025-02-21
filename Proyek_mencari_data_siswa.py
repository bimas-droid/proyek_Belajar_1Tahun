# Program memeriksa data siswa di list

# Kumpulan nama 
data_list = [
    {"nama": "Budi", "id": 573602909341},
    {"nama": "Siti", "id": 290735868422},
    {"nama": "Andi", "id": 427873311756},
    {"nama": "Dewi", "id": 570605172526},
    {"nama": "Rizky", "id": 470446102991},
    {"nama": "Lina", "id": 912134523940},
    {"nama": "Hendra", "id": 169268049643},
    {"nama": "Fajar", "id": 228453947793},
    {"nama": "Nina", "id": 451010987591},
    {"nama": "Yoga", "id": 527150430394},
    {"nama": "Tina", "id": 848615221287},
    {"nama": "Rian", "id": 247415224548},
    {"nama": "Bayu", "id": 293041299393},
    {"nama": "Sari", "id": 686194264577},
    {"nama": "Joko", "id": 782221510809}
]

# memu utama
def menu_utama():
    menu = ["Mengecek nama", "Menampilkan nama", "Menghapus nama", "Menambah nama"]
    for index, nomer in enumerate(menu, start=1):
        print(f"{index}. {nomer}")

def mengecek_nama():
    meminta_nama = (input("masukkan nama: ")).title().strip()
    ditemukan = False

    for data in data_list:
        if meminta_nama == data["nama"]:
            print(f"Nama {meminta_nama} terdaftar di list ✅ id {data["id"]} ")
            ditemukan = True
            break

    if not ditemukan:
            print(f"Nama {meminta_nama} tidak terdaftar di list ❌ ")

# Menampilkan list
def menampilkan_list():
     for index, nama in enumerate(data_list, start=1):
          print(f"{index}. nama: {nama["nama"]} id:{nama["id"]}")

# menghapus nama
def menghapus_nama():
    global data_list
    nama = input("masukkan nama: ").strip().title()

     # mengecek apakah data ada
    found = False # mengecek data

     # masuk kedalam data list
    for data in data_list:
        if data["nama"] == nama:
            data_list.remove(data) # menghapus dictioneri dari data
            print(f'data atas nama {nama} telah di hapus ✅ ')
            found = True
            break

    if not found:
            print(f"Tidak ditemukan data dengan nama {nama} ❌")

# menambah nama
def menambah_nama():
    nama = str(input('masukkan nama: ')).title()
    masukkan_id = input("masukan id min/max 12: ") 
    # menambahkan ke dalam list
    data_list.append({"nama": nama, "id": masukkan_id})
    print("Sukses ✅")

# Wile true
while True:
    menu_utama()
    menu = str(input("Pilih menu: "))

    if menu == "1":
          mengecek_nama()

    if menu == "2":
         menampilkan_list()

    if menu == "3":
        menghapus_nama()

    if menu == "4":
        menambah_nama()

