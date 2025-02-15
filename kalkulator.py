# kalkulator sederhana
print('pilih salah satu oprator untuk melakukan perintah: ')
print('1. penjumblahan +')
print('2. pegurangan -')
print('3. perkalian x')
print('4. pembagian /')

# meinta input 
angka1 = int(input('masukan angka: '))
oprator = str(input('masukan oprator: '))
angka2 = int(input('masukan angka: '))

# logika kalkulator sederhana
# penjumblahan
if oprator == '+':
    print(f'hasil dari {angka1} + {angka2} = {angka1+angka2}')

#pengurangan 
elif oprator == '-':
    print(f'hasil dari {angka1} - {angka2} = {angka1-angka2}')

# perkalian[]
elif oprator == 'x':
    print(f'hasil dari {angka1} x {angka2} = {angka1*angka2}')

# pembagian
else:
    if oprator == "/":
        if angka2 or angka1 == 0:
            print('error')
        else:
            print(f'hasil dari {angka1} / {angka2} = {angka1/angka2}')
            