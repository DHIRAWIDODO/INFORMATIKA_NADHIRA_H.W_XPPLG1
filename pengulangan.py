# MATERI: JENIS-JENIS LOOPING DI PYTHON

# 1. WHILE LOOP
# Melakukan perulangan selama kondisi bernilai True
print("While Loop:")
angka = 1
while angka <= 5:
    print("Angka ke-", angka)
    angka += 1  # Naikkan nilai angka
print()  # Pemisah output

# 2. FOR LOOP
# Digunakan untuk mengulang elemen dalam urutan seperti range, list, string
print("For Loop:")
for i in range(1, 6):  # range dari 1 sampai 5
    print("Perulangan ke-", i)
print()  # Pemisah output

# 3. NESTED LOOP
# Perulangan di dalam perulangan (loop bersarang)
print("Nested Loop (Perulangan Bersarang):")
for i in range(1, 4):  # loop luar
    for j in range(1, 4):  # loop dalam
        print(f"i={i}, j={j}")
    print("Selesai satu putaran dalam\n")
