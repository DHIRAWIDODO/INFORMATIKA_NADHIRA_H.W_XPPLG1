# MATERI: MENGUPDATE / MEMANIPULASI STRING

# 1. Mengakses karakter dalam string (indeks dimulai dari 0)
kata = "Python"
print("Huruf pertama:", kata[0])   # Output: P
print("Huruf terakhir:", kata[-1]) # Output: n
print()

# 2. Mengubah string jadi huruf besar dan kecil
kalimat = "Aku Suka Python"
print("Uppercase:", kalimat.upper())   # Semua huruf jadi besar
print("Lowercase:", kalimat.lower())   # Semua huruf jadi kecil
print()

# 3. Mengganti isi string (replace)
kalimat_baru = kalimat.replace("Python", "JavaScript")
print("Hasil Replace:", kalimat_baru)
print()

# 4. Menambahkan (menyambung) string
nama_depan = "Nadhira"
nama_belakang = "Wibowo"
nama_lengkap = nama_depan + " " + nama_belakang
print("Nama Lengkap:", nama_lengkap)
print()

# 5. Mengambil sebagian string (slicing)
teks = "Belajar Pyth
