print("Latihan If Elif Else")
print(15*"-")

nilai = float(input("Masukkan Nilai :"))

if nilai >= 80:
    print ("Nilai", nilai, "Adalah A")

elif 68 <= nilai < 80:
    print ("Nilai", nilai, "Adalah B")
elif 55 <= nilai < 68:
    print ("Nilai", nilai, "Adalah C")
elif 40 <= nilai < 55:
    print ("Nilai", nilai, "Adalah D")
else:
    print(nilai, "Anda Harus Mengulang Mata Kuliah Ini")