#Continue & Pass

#Tanpa Keduanya
for angka in range(1,11):
    print("Angka Saat ini", angka)
else:
    print("Udah Selesai")

#Continue
print("----Continue----")
dicari = 8
for angka in range(1,11):
    if angka is dicari:
        print("Ini Angka", dicari)
        continue
    print("Angka Saat ini", angka)
else:
    print("Udah Selesai")

#Pass
print("----Pass----")
dicari = 8
for angka in range(1,11):
    if angka is dicari:
        print("Ini Angka", dicari)
        pass
    print("Angka Saat ini", angka)
else:
    print("Udah Selesai")