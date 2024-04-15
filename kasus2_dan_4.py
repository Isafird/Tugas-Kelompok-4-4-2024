angka = int(input("tambahkan max data : "))
for i in range(angka):

  print("number",i)
  
  
angka = int(input("tambahkan max data : "))
for i in range(angka + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")