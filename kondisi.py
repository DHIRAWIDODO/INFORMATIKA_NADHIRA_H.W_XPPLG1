# KONDISI / PERCABANGAN DI PYTHON

# Contoh 1: If-Elif-Else
# Mengecek nilai dan mencetak kategori huruf
nilai = 80

if nilai >= 90:
    print("Nilai A")  # Jika nilai 90 ke atas
elif nilai >= 75:
    print("Nilai B")  # Jika nilai 75 sampai 89
else:
    print("Nilai C")  # Jika nilai di bawah 75

print()  # Pemisah output

# Contoh 2: If dengan operator logika AND
umur = 17
ktp = True  # Sudah punya KTP

if umur >= 17 and ktp:
    print("Boleh membuat SIM")  # Kedua kondisi harus terpenuhi
else:
    print("Belum bisa membuat SIM")

print()  # Pemisah output

# Contoh 3: If bersarang (nested if)
angka = 10

if angka > 0:
    if angka % 2 == 0:
        print("Angka positif dan genap")  # Cek genap jika positif
    else:
        print("Angka positif dan ganjil")
else:
    print("Angka nol atau negatif")
