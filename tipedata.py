# Tipe Data 
"""
Boolean	    True atau False         	  Menyatakan benar (True) yang bernilai 1, atau salah (False) yang bernilai 0
String	    "Ayo belajar Python"	      Menyatakan karakter/kalimat bisa berupa huruf, angka, dll (diapit tanda " atau ')
Integer 	25 atau 1209	              Menyatakan bilangan bulat
Float	    3.14 atau 0.99	              Menyatakan bilangan yang mempunyai koma
Hexadecimal	9a atau 1d3     	          Menyatakan bilangan dalam format heksa (bilangan berbasis 16)
Complex 	1 + 5j	                      Menyatakan pasangan angka real dan imajiner
List	    ['xyz', 786, 2.23]	          Data untaian yang dapat menyimpan berbagai tipe data dan isinya dapat diubah-ubah
Tuple	    ('xyz', 786, 2.23)	          Data untaian yang dapat menyimpan berbagai tipe data tapi isinya tidak bisa diubah
Dictionary	{'nama' : 'adi' , 'id' : 2}	  Data untaian yang menyimpan berbagai tipe data berupa pasangan penunjuk dan nilai (key dan value)

Tipe Text yaitu string
Tipe Numeric yaitu Integer, Float, dan Complex
Tipe Sequence yaitu List, Tuple, Range
Tipe Mapping yaitu Dict
Tipe Set yaitu Set, Frozen Set
Tipe Boolean yaitu Bool
Tipe Binary yaitu bytes, bytesarray, memoryview
"""

# Boolean: Menyatakan benar (True) atau salah (False)
print("Boolean:", True, "atau", False)  # True bernilai 1, False bernilai 0

# String: Teks atau kalimat
print("String:", "Aku Suka Nasgor")

# Integer: Bilangan bulat
print("Integer:", 25)

# Float: Bilangan desimal
print("Float:", 3.14)

# Hexadecimal: Bilangan berbasis 16
print("Hexadecimal dari 154 adalah:", hex(154))  # Output: 0x9a

# Complex: Bilangan kompleks (real + imajiner)
print("Complex:", 1 + 5j)

# List: Kumpulan data yang bisa diubah
print("List campuran:", ['xyz', 786, 2.23])
print("List angka:", [1, 2, 3, 4, 5])
print("List string:", ["apel", "jeruk", "mangga"])

# Tuple: Kumpulan data yang tidak bisa diubah
print("Tuple campuran:", ('xyz', 786, 2.23))
print("Tuple angka:", (1, 2, 3, 4, 5))
print("Tuple string:", ("satu", "dua", "tiga"))

# Dictionary: Data pasangan key dan value
print("Dictionary:", {'nama': 'Adi', 'id': 2})

# Dictionary disimpan dalam variabel
biodata = {"nama": "Andi", "umur": 21}
print("Biodata Dictionary:", biodata)