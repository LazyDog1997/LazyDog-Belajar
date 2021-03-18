nilai = 3

#while nilai < 5: (Bila ini dijalankan, tidak akan berhenti)
    #print("Nilainya adalah", nilai)

while nilai < 5:
    print("Nilainya adalah", nilai)
    nilai += nilai

print("Udah Selesai")

#Pencarian
print("----Pencarian----")

start = True
NPM = 0

while start:
    print("Urutan", NPM, "Masih nyari ke 74")
    if NPM is 73:
        start = False
        print("Ditemukan")
    NPM = NPM + 1
else:
    print("NPM", NPM, "Ada di Sini")

#Bila Pake Break
print("----Bila Pake Break----")

start = True
NPM = 0

while start:
    print("Urutan", NPM, "Masih nyari ke 74")
    if NPM is 73:
        start = False
        print("Ditemukan")
        break
    NPM = NPM + 1
else:
    print("NPM", NPM, "Ada di Sini")

#Bila Pake Continue
print("----Bila Pake Continue----")

start = True
NPM = 0

while start:
    print("Urutan", NPM, "Masih nyari ke 74")
    if NPM is 73:
        start = False
        print("Ditemukan")
        continue
    NPM = NPM + 1
else:
    print("NPM", NPM, "Ada di Sini")