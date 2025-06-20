import random

angka = random.randint(1, 10)
tebakan = 0

print("Tebak angka dari 1 sampai 10!")

while tebakan != angka:
    tebakan = int(input("Tebakanmu: "))
    if tebakan < angka:
        print("Terlalu kecil!")
    elif tebakan > angka:
        print("Terlalu besar!")

print("Benar! 🎉")
