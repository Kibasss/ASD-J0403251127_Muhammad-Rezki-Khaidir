#===============================================================
# Praktikum 1 - Konsep ADT dan File Handling
# Latihan Dasar 1: Membaca Seluruh Isi File
#===============================================================

# Membuka file dengan Mode 'r' (read)
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("===Hasil Read===")
print("Tipe Data:", type(isi_file))
print("Jumlah karakter:", len(isi_file))
print("Jumlah Baris:", isi_file.count('\n') + 1) 

# membuka file per Baris
print("===Membaca File per Baris===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print("Isinya :", baris)

#===============================================================
# Praktikum 1 - Konsep ADT dan File Handling
# Latihan Dasar 2: Parsing Baris Menjadi Kolom Data
#===============================================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("NIM :", nim, " | Nama :", nama, "| Nilai :", nilai)

#===============================================================
# Praktikum 1 - Konsep ADT dan File Handling
# Latihan Dasar 3: Membaca File dan Menyimpan ke List
#===============================================================
# List untuk Menampung
data_list = []

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        
        # Simpan Sebagai List [NIM, Nama, Nilai]
        data_list.append([nim, nama, int(nilai)])

print("=== Data Mahasiswa dalam List ===")
print(data_list)

print("=== Jumlah Record dalam List ===")
print("Jumlah Record :", len(data_list))

print("===Menampilkan Data Record Tertentu===")
print("Contoh Record Pertama :", data_list[0])

#===============================================================
# Praktikum 1 - Konsep ADT dan File Handling
# Latihan Dasar 4: Membaca File dan Menyimpan ke Dictionary
#===============================================================

data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        # Simpan Data mahasiswa ke Dictionary dengan Key NIM
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }
print("=== Data Mahasiswa dalam Dictionary ===")
print(data_dict)