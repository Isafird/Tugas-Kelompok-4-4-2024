print('KASUS 3')

jumlah_pengulangan = int(input("Masukkan banyak pengulangan: "))

for i in range(jumlah_pengulangan, 0, -1):
    print(f"Baris ke- {i}")


print('\nKASUS 5')

max_data = int(input("Enter max data: "))

for i in range(1, max_data + 1):
    print("# " * i)
