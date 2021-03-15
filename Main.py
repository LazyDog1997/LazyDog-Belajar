#konversi suhu

celsius = float(input('Masukka Suhu Dalam Celsius : '))
print("Suhu : ",celsius," Celsius")

#KOnversi ke Reamur
print(" ")
print("Suhu Dalam Reamur")
reamur = 4/5*celsius
print("Suhu : ",reamur," Reamur")

#Konversi ke Fahrenheit
print(" ")
print("Suhu Dalam Fahrenheit")
fahrenheit = (9/5)*celsius+32
print("Suhu : ",fahrenheit," Fahrenheit")

#Konversi ke Kelvin
print(" ")
print("Suhu Dalam Kelvin")
kelvin = celsius+273
print("Suhu : ",kelvin," Kelvin")

#Konversi Fahrenheit ke Kelvin
print(" ")
print("Konversi Fahrenheit ke Kelvin")
derajatF = float(input('Masukkan Suhu :'))
print("Suhu : ",derajatF,"Fahrenheit")
konK = (5/9*(derajatF-32))+273
print("Suhu : ",konK,"Kelvin")

#Konversi Kelvin ke Fahrenheit
print(" ")
print("Konversi Kelvin ke Fahrenheit")
derajatK = float(input('Masukkan Suhu dalam Kelvin :'))
print("Suhu : ", derajatK,"Kelvin")
konF = ((derajatK-273)*9/5)+32
print("Suhu : ",konF,"Fahrenheit")