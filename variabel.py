# Variabel
"""
Penamaan Variabel
Nama variabel harus dimulai dengan huruf atau karakter garis bawah
Nama variabel tidak dapat dimulai dengan angka
Nama variabel hanya dapat berisi karakter alfanumerik dan garis bawah (A-z, 0-9, dan _)
Nama variabel peka huruf besar-kecil (usia, Usia dan AGE adalah tiga variabel berbeda)
"""

# Cara memasukkan data ke varibel
nama = "Nadhira"
print (nama)

# Data dan Tipe data variabel dapat diubah
umur = 16           # Nilai awal umur
print (umur)        # Mencetak data umur
print (type(umur))  # Tipe data umur
umur = "Enam Belas" # Nilai baru umur
print (umur)        # mencetak data baru umur
print (type(umur))  # tipe data baru umur

# variabel data menggunakan operator aritmatika dan ditampilkan dalam satu kali perintah
depan = "Nadhira"
akhir = "Rahayu"
nama  = depan + " " + akhir
umur  = 16
hobi  = "Membaca"
print ("Biodata\n", "Nama : ", nama, "\n", "Umur : ", umur, "\n", "Hobi : ", hobi) 

# Menghitung luas persegi panjang
panjang = 15
lebar   = 10
# rumus = panjang x lebar
hasil   = panjang * lebar
print (hasil)