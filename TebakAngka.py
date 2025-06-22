import random  # Mengimpor modul random untuk menghasilkan angka acak

angka_rahasia = random.randint(1, 10)  # Menghasilkan angka acak antara 1 sampai 10
tebakan = 0  # Nilai awal tebakan diset 0

print("Tebak angka dari 1 sampai 10")  # Menampilkan instruksi ke pemain

# Ulangi selama tebakan belum benar
while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan tebakanmu: "))  # Meminta input angka dari pemain
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")  # Jika tebakan lebih kecil dari angka rahasia
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")  # Jika tebakan lebih besar dari angka rahasia

print("Selamat! Kamu menebak dengan benar.")  # Jika tebakan sama dengan angka rahasia
