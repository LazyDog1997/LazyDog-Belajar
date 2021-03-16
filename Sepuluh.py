#Latihan Komparasi dan Logika
print("----Soal 1----")
soal1 = float(input("Masukkan Angka :"))
a1 = soal1 > 0
b1 = soal1 < 5
c1 = soal1 > 8
d1 = soal1 < 11

bagsoal1a = a1 and b1
bagsoal1b = c1 and d1
hasil1 = bagsoal1a or bagsoal1b
print("Nilai Angka Tersebut : ", hasil1)

print("----Soal 2----")
soal2 = float(input("Masukkan Angka :"))
a2 = soal2 < 0
b2 = soal2 > 5
c2 = soal2 < 8
d2 = soal2 > 11

bagsoal2a = a2 or d2
bagsoal2b = b2 and c2
hasil2 = bagsoal2a or bagsoal2b
print("Nilai Angka Tersebut :", hasil2)