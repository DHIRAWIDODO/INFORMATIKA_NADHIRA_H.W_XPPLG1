# Operator 
# 1. Operator Aritmatika

print("\n")
print ("Operator Aritmatika")

"""
Penjumlahan +	1 + 3 = 4	Menjumlahkan nilai dari masing-masing operan atau bilangan
Pengurangan -	4 - 1 = 3	Mengurangi nilai operan di sebelah kiri menggunakan operan di sebelah kanan
Perkalian   *	2 * 4 = 8	Mengalikan operan/bilangan
Pembagian   /	10 / 5 = 2	Untuk membagi operan di sebelah kiri menggunakan operan di sebelah kanan
Sisa Bagi   %	11 % 2 = 1	Mendapatkan sisa pembagian dari operan di sebelah kiri operator ketika dibagi oleh operan di sebelah kanan
Pangkat    **	8 ** 2 = 64	Memangkatkan operan disebelah kiri operator dengan operan disebelah kanan operator
Pembagian Bulat //	10 //3 = 3	Sama seperti pembagian, hanya saja angka dibelakang koma dihilangka
"""

# Penjumlahan
pensil = 5
pulpen = 3
jumlah_alat_tulis = pensil + pulpen
print("Jumlah alat tulis: ", jumlah_alat_tulis)

# Pengurangan
uang_saku = 20000
jajan = 8000
sisa_uang = uang_saku - jajan
print("Sisa uang setelah jajan: Rp", sisa_uang)

# Perkalian
nasi_kotak = 4
harga_per_kotak = 12000
total_harga = nasi_kotak * harga_per_kotak
print("Total harga nasi kotak: Rp", total_harga)

# Pembagian
roti = 12
teman = 3
roti_per_teman = roti / teman
print("Setiap teman dapat roti sebanyak:", roti_per_teman)

# Modulus (Sisa Bagi)
kelereng = 17
dibagi_ke_teman = 4
sisa_kelereng = kelereng % dibagi_ke_teman
print("Sisa kelereng yang tidak terbagi: ", sisa_kelereng)

# Pangkat
angka = 3
pangkat = 2
hasil = angka ** pangkat
print("Hasil dari 3 pangkat 2 adalah:", hasil)

# Pembagian Bulat
total_orang = 10
kursi = 3
orang_per_kursi = total_orang // kursi
print("Jumlah orang yang duduk per kursi: ", orang_per_kursi)
print ("\n")



# 2. Opertaor perbandingan

print("\n")
print ("Operator Perbandingan")

"""
Sama dengan       ==	1 == 1	Bernilai True Jika masing-masing operan memiliki nilai yang sama, False jika nilai tidak sama
Tidak sama dengan !=	2 != 2	Bernilai True jika masing-masing operan memiliki nilai yang tidak sama, False jika nilai sama
Lebih besar dari   >	5 > 3	Bernilai True Jika nilai operan kiri lebih besar dari nilai operan kanan, maka kondisi menjadi benar.
Lebih kecil dari   <	5 < 3	Bernilai True Jika nilai operan kiri lebih kecil dari nilai operan kanan, maka kondisi menjadi benar.
Lebih besar atau sama dengan >=	5 >= 3	Bernilai True Jika nilai operan kiri lebih besar dari nilai operan kanan, atau sama, maka kondisi menjadi benar
Lebih kecil atau sama dengan <=	5 >= 3	Bernilai True Jika nilai operan kiri lebih kecil dari nilai operan kanan, atau sama, maka kondisi menjadi benar
"""

# Sama dengan (==)
print("10 == 10 =", 10 == 10)  # True
print("5 == 8 =", 5 == 8)      # False

# Tidak sama dengan (!=)
print("7 != 3 =", 7 != 3)      # True
print("4 != 4 =", 4 != 4)      # False

# Lebih besar dari (>)
print("9 > 6 =", 9 > 6)        # True
print("2 > 5 =", 2 > 5)        # False

# Lebih kecil dari (<)
print("3 < 10 =", 3 < 10)      # True
print("8 < 1 =", 8 < 1)        # False

# Lebih besar atau sama dengan (>=)
print("5 >= 5 =", 5 >= 5)      # True
print("4 >= 9 =", 4 >= 9)      # False

# Lebih kecil atau sama dengan (<=)
print("6 <= 6 =", 6 <= 6)      # True
print("10 <= 4 =", 10 <= 4)    # False
print ("\n")



# 3. Operator penugasan

print("\n")
print ("Operator penugasan")

"""
Sama dengan         =	a = 1	Memberikan nilai di kanan ke dalam variabel yang berada disebelah kiri
Tambah sama dengan  +=	a += 2	Memberikan nilai variabel dengan nilai variabel itu sendiri ditambah dengan nilai disebelah kanan
Kurang sama dengan  -=	a -= 2	Memberikan nilai variabel dengan nilai variabel itu sendiri dikurangi dengan nilai disebelah kanan
Kali sama dengan    *=	a *= 2	Memberikan nilai variabel dengan nilai variabel itu sendiri dikali dengan nilai disebelah kanan
Bagi sama dengan    /=	a /= 2	Memberikan nilai variabel dengan nilai variabel itu sendiri dibagi dengan nilai disebelah kanan
Sisa bagi sama dengan        %=	a %= 2	Memberikan nilai variabel dengan nilai variabel itu sendiri dibagi dengan nilai di sebelah kanan. Yang diambil nantinya adalah sisa baginya
Pangkat sama dengan         **=	a **= 2	Memberikan nilai variabel dengan nilai variabel itu sendiri dipangkatkan dengan nilai di sebelah kanan
Pembagian bulat sama dengan //=	a //= 2	Membagi bulat operan sebelah kiri operator dengan operan sebelah kanan operator kemudian hasilnya diisikan ke operan sebelah kiri
"""

# 1. Sama dengan (=)
a = 1
print("a =", a)  # Memberikan nilai 1 ke variabel a

# 2. Tambah sama dengan (+=)
a = 5
a += 2  # Sama dengan: a = a + 2
print("a += 2 →", a)

# 3. Kurang sama dengan (-=)
a = 5
a -= 2  # Sama dengan: a = a - 2
print("a -= 2 →", a)

# 4. Kali sama dengan (*=)
a = 3
a *= 2  # Sama dengan: a = a * 2
print("a *= 2 →", a)

# 5. Bagi sama dengan (/=)
a = 10
a /= 2  # Sama dengan: a = a / 2
print("a /= 2 →", a)


# 6. Sisa bagi sama dengan (%=)
a = 10
a %= 3  # Sama dengan: a = a % 3
print("a %= 3 →", a)

# 7. Pangkat sama dengan (**=)
a = 2
a **= 3  # Sama dengan: a = a ** 3
print("a **= 3 →", a)

# 8. Pembagian bulat sama dengan (//=)
a = 10
a //= 3  # Sama dengan: a = a // 3
print("a //= 3 →", a)



# 4. Operator Logical

print("\n")
print ("Operator Logical")

"""
and	a, b = True, True	Jika kedua operan bernilai True, maka kondisi akan bernilai True. Selain kondisi tadi maka akan bernilai False
or	a, b = True, False	Jika salah satu atau kedua operan bernilai True maka kondisi akan bernilai True. Jika keduanya False maka kondisi akan bernilai False.
not	a, b = True, False	Membalikkan nilai kebeneran pada operan misal jika asalnya True akan menjadi False dan begitupun sebaliknya
"""

# and → harus dua-duanya True
print("2 > 1 and 3 > 2 =", 2 > 1 and 3 > 2)     # True
print("2 > 1 and 3 > 5 =", 2 > 1 and 3 > 5)     # False

# or → cukup salah satu True
print("2 > 1 or 3 > 5 =", 2 > 1 or 5 > 3)       # True
print("1 > 5 or 3 > 2 =", 1 > 5 or 3 > 2)       # True
print("1 > 5 or 2 > 3 =", 1 > 5 or 2 > 3)       # False

# not → membalik hasil
print("not 3 > 2 =", not 3 > 2)                 # False
print("not 1 > 5 =", not 1 > 5)                 # True



# 5. Operator Bitwise

print("\n")
print ("Operator Bitwise")

"""
&	c = a & b	Operator biner AND, memeriksa apakah operan di sebelah kiri dan operan sebelah kanan mempunyai angka biner 1 di setiap bit. Jika keduanya bernilai 1 maka bit hasil operasi akan bernilai 1
|	c = a | b	Operator biner OR, memeriksa apakah operan di sebelah kiri dan operan sebelah kanan mempunyai angka biner 1 di setiap bit. Jika salah satunya bernilai 1 maka bit hasil operasi akan bernilai 1
"""

# & Operator Biner AND
a = 5   # dalam biner: 0101
b = 3   # dalam biner: 0011
c = a & b  # hanya bit yang sama-sama 1 yang akan bernilai 1
print("a & b =", c)  # Hasil: 0101 & 0011 = 0001 (1 dalam desimal)

# | Operator Biner OR
a = 5   # dalam biner: 0101
b = 3   # dalam biner: 0011
c = a | b  # jika salah satu bit 1, hasilnya 1
print("a | b =", c)  # Hasil: 0101 | 0011 = 0111 (7 dalam desimal)
print("\n")



# 6. Operator Keanggotaan (Membership)

print("\n")
print ("Operator Keanggotaan")

"""
in	sebuah_list     = [1, 2, 3,4 ,5]    print(5 in sebuah_list)	    	Memeriksa apakah nilai yang dicari berada pada list atau struktur data python lainnya. Jika nilai tersebut ada maka kondisi akan bernilai True
not in	sebuah_list = [1, 2, 3,4 ,5]	print(10 not in sebuah_list)	Memeriksa apakah nilai yang dicari tidak ada pada list atau struktur data python lainnya. Jika nilai tersebut tidak ada maka kondisi akan bernilai True
"""

# List untuk contoh
sebuah_list = [1, 2, 3, 4, 5]

# in → Memeriksa apakah nilai ada dalam list
print("5 in sebuah_list =", 5 in sebuah_list)   # True karena 5 ada di dalam list
print("10 in sebuah_list =", 10 in sebuah_list) # False karena 10 tidak ada di dalam list

# not in → Memeriksa apakah nilai tidak ada dalam list
print("3 not in sebuah_list =", 3 not in sebuah_list)  # False karena 3 ada di dalam list
print("7 not in sebuah_list =", 7 not in sebuah_list)  # True karena 7 tidak ada di dalam list
print("\n")



# 7. Operator Identitas

print("\n")
print ("Operator Identitas")

"""
is	    a, b = 10, 10	print(a is b)       Memeriksa apakah nilai di sebelah kiri operan memiliki identitas memori yang sama dengan nilai di sebelah kanan operan. Jika sama maka kondisi bernilai True	
is not	a, b = 10, 10	print(a is not b)	Memeriksa apakah nilai di sebelah kiri operan memiliki identitas memori yang berbeda dengan nilai di sebelah kanan operan. Jika berbeda maka kondisi bernilai True
"""

# Variabel Identitas
a, b, c = 10, 10, 5
print("a =", a)
print("b =", b)
print("c =", c)

# is → Memeriksa apakah objek memiliki identitas memori yang sama
print("a is b =", a is b)  # True karena a dan b memiliki nilai yang sama dan identitas memori yang sama
print("a is c =", a is c)  # False karena a dan c berbeda nilai dan identitas memori

# is not → Memeriksa apakah objek memiliki identitas memori yang berbeda
print("a is not b =", a is not b)  # False karena a dan b identitas memori sama
print("a is not c =", a is not c)  # True karena a dan c memiliki identitas memori berbeda
print("\n")