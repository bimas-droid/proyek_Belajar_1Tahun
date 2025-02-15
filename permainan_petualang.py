# Game Petualangan: Menemukan Harta Karun

# batas permintaan 
maxx = 5
kesempatan = 0

# penyimpan data benar
jawaban_benar = ["Kiri", "Maju", "Kanan"]

# soal
ketentuan = [
    "Kiri",
    "Kanan",
    "Maju"
]
print("\nSeorang petualang terjebak dalam sebuah gua dan")
print("harus menemukan jalan keluar dengan memilih arah yang benar.\n")
print("==Pilih dengan jawaban==")

for ket in ketentuan:
    print(f'- {ket}')

nama_player = input("Masukkan Nama: ")
# while true
while True:
    # mengambil input jawaban dari pengguna
    jalan_awal = str(input('\n1. Jalan pertama mana yang harus saya tempu?: '))[:5].title()
    jalan_kedua = str(input('2. jalan kedua mana yang harus saya tempu?: '))[:5].title()
    jalan_ketiga = str(input('3. jalan ke tiga mana yang harus saya tempu?: '))[:6].title()
    kesempatan += 1

    # Logika Program
    if [jalan_awal, jalan_kedua, jalan_ketiga] == jawaban_benar:
        print('')
        print("==="*17)
        print("petualang menemukan harta karun dan keluar dari gua 🎁")
        print("==="*17)
        print(f"\nSelamat {nama_player}🎉!, kamu memenangkan game dengan {kesempatan}x Kesempatan")
        print("Itu sangat luar biasa ✨😎")
        break
 
    if kesempatan == 3:
        print("==="*15)
        print(f'Petualang Tersesat 😔, Tolong Saya {nama_player}!')
        print("==="*15)
        bantuan = str(input(f"\nApakah anda membutuhkan bantuan, Di karenakan kesempatan Anda tersia {maxx - kesempatan}x lagi: "))[:5].title()
        # jika bantuan ya/tentu/baik/ok/oke
        if bantuan == "Ok" or bantuan == "Ya" or bantuan == "Oke" or bantuan == "Tentu" or bantuan == "Baik":
            print("untuk jalan kedua: biasanya tangan untuk orang makan 😁\n")

        # Jika tidak berarti langsung ulang lagi dari awal pertanyaan
        else:

            print(f"Baik Trimakasih {nama_player}, Semoga beruntung 👋")

    else:
        print("==="*15)
        print(f"petualang tersesat 😔, Tolong Saya {nama_player}!")
        print("==="*15)
        mengulang = str(input('Apakah anda ingin mengulang lagi dari awal sampai benar 🤔 : '))[:5].title()

        # jika pemain menjawab ya/oke/tentu/ok/baik
        if mengulang == "Ya" or mengulang == "Oke" or mengulang == "Tentu" or mengulang == "Ok" or mengulang == "Baik":
            continue
        # jika menjawab tidak
        else:
            print("Petualang tersesat selamanya 😣!\n")
            break

print("terimakasih telah bermain 👌, jangan lupa tersenyum ya 😁\n")