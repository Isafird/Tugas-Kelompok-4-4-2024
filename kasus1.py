import math

def bola(jari_jari):
    k = 2 * math.pi * jari_jari
    l = 4 * math.pi * jari_jari ** 2
    v = (4/3) * math.pi * jari_jari ** 3
    return k, l, v

def kubus(sisi):
    k = 12 * sisi
    l = 6 * sisi ** 2
    v = sisi ** 3
    return k, l, v

def balok(panjang, lebar, tinggi):
    k = 4 * (panjang + lebar + tinggi)
    l = 2 * (panjang * lebar) + (lebar * tinggi) + (tinggi * panjang)
    v = panjang * lebar * tinggi
    return k, l, v


print("Pilih opsi:")
print("A. Bola \nB. Kubus \nC. Balok")

opsi = input("Masukkan pilihan (A/B/C): ").upper()

if opsi not in ['A', 'B', 'C']:
    print("Pilihan tidak valid.")
    exit()


print("\nPilih operasi yang diinginkan:")
print("1. Keliling \n2. Luas \n3. Volume")
    
operasi = input("Masukkan pilihan (1/2/3): ")

if operasi not in ['1', '2', '3']:
    print("Pilihan tidak valid.")
    exit()


if opsi == 'A':
        jari_jari = float(input("Masukkan panjang jari-jari bola (cm): "))
        hasil = bola(jari_jari)
elif opsi == 'B':
        sisi = float(input("Masukkan panjang sisi kubus (cm): "))
        hasil = kubus(sisi)
elif opsi == 'C':
        panjang = float(input("Masukkan panjang balok (cm): "))
        lebar = float(input("Masukkan lebar balok (cm): "))
        tinggi = float(input("Masukkan tinggi balok (cm): "))
        hasil = balok(panjang, lebar, tinggi)


if operasi == '1':
    print(f"Keliling: {hasil[0]}")
elif operasi == '2':
    print(f"Luas: {hasil[1]}")
elif operasi == '3':
    print(f"Volume: {hasil[2]}")