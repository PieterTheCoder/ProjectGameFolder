def ask_name():
    name = input("What is your name? ")  # Meminta pemain mengetikkan namanya
    if name == "Pieter":                 # Mengecek apakah nama yang diketik "Pieter"
        print("Cool! Your name is the same as a great programmer 😄")  # Puji nama Pieter
    else:
        print("Hello", name)             # Sapa biasa kalau bukan Pieter

ask_name()  # Memanggil fungsi agar dijalankan

