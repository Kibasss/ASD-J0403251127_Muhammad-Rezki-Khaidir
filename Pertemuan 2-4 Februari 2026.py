# ================================================
# Praktikum 2 : Konsep ADT dan FIle Handling (Studi Kasus)
# Latihan Dasar 1 : Membuat Fungsi Load Data
# ================================================

nama_file = 'data_mahasiswa.txt'

def load_data_mahasiswa(nama_file):
    data_mahasiswa = {}
    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(',')

            data_mahasiswa[nim] = {
                'nama': nama,
                'nilai': int(nilai)
            }
    return data_mahasiswa

buka_data = load_data_mahasiswa(nama_file)
# print(load_data_mahasiswa(nama_file))
# print("Jumlah Data Mahasiswa:", len(buka_data))

# ===============================================
# Praktikum 2 : Konsep ADT dan FIle Handling (Studi Kasus)
# Latihan Dasar 2 : Membuat Fungsi Menampilkan Data
# ===============================================

def tampil_data_mahasiswa(data_mahasiswa):
    print("\n=== Data Mahasiswa ===")
    print(f"{'NIM':10} | {'Nama':<12} | {'Nilai':>10}")
    print("-" * 50)

    for nim in sorted(data_mahasiswa.keys()):
        nama = data_mahasiswa[nim]['nama']
        nilai = data_mahasiswa[nim]['nilai']
        print(f"{nim:10} {nama:<12} {nilai:>10}")

# tampil_data_mahasiswa(buka_data)

# ===============================================
# Praktikum 2 : Konsep ADT dan FIle Handling (Studi Kasus)
# Latihan Dasar 3 : Membuat Fungsi Mencari Data
# ===============================================

def cari_data_mahasiswa(data_mahasiswa):
    nim_input = input("Masukkan NIM yang ingin dicari: ").upper().strip()
    if nim_input in data_mahasiswa:
        nama = data_mahasiswa[nim_input]['nama']
        nilai = data_mahasiswa[nim_input]['nilai']
        print("\nData Ditemukan:")
        print(f"NIM  : {nim_input}")
        print(f"Nama :{nama}")
        print(f"Nilai: {nilai}")
    else:
        print("\nData Tidak Ditemukan.")

# cari_data_mahasiswa(buka_data)

# ===============================================
# Praktikum 2 : Konsep ADT dan FIle Handling (Studi Kasus)
# Latihan Dasar 4 : Membuat Fungsi Update Data
# ===============================================

def update_data_mahasiswa(data_mahasiswa):
    nim_input = input("Masukkan NIM yang ingin diupdate: ").upper().strip()
    if nim_input not in data_mahasiswa:
        print("\nData Tidak Ditemukan.")
        return
    try:
        nilai_baru = int(input("Masukkan Nilai Baru (0-100): "))
    except ValueError:
        print("\nNilai harus berupa angka antara 0-100.")
        return
    if nilai_baru < 0 or nilai_baru > 100:
        print("\nNilai harus antara 0-100.")
        return
    
    nilai_lama = data_mahasiswa[nim_input]['nilai']
    data_mahasiswa[nim_input]['nilai'] = nilai_baru
    print("\nData Berhasil Diupdate.")

# update_data_mahasiswa(buka_data)

# ================================================
# Praktikum 2 : Konsep ADT dan FIle Handling (Studi Kasus)
# Latihan Dasar 5 : Membuat Fungsi Simpan Data
# ================================================

def simpan_data_mahasiswa(nama_file, data_mahasiswa):
    with open(nama_file, 'w', encoding='utf-8') as file:
        for nim in sorted(data_mahasiswa.keys()):
            nama = data_mahasiswa[nim]['nama']
            nilai = data_mahasiswa[nim]['nilai']
            baris = f"{nim},{nama},{nilai}\n"
            file.write(baris)
    print("\nData Berhasil Disimpan ke File.")
# simpan_data_mahasiswa(nama_file, buka_data)

# ================================================
# Praktikum 2 : Konsep ADT dan FIle Handling (Studi Kasus)
# Latihan Dasar 6 : Menambahkan Data Mahasiswa
# ================================================

def tambah_data_mahasiswa(data_mahasiswa):
    nim_baru = input("Masukkan NIM Baru: ").upper().strip()
    if nim_baru in data_mahasiswa:
        print("\nNIM sudah ada dalam data.")
        return
    nama_baru = input("Masukkan Nama Mahasiswa: ").strip()
    try:
        nilai_baru = int(input("Masukkan Nilai Mahasiswa (0-100): "))
    except ValueError:
        print("\nNilai harus berupa angka antara 0-100.")
        return
    if nilai_baru < 0 or nilai_baru > 100:
        print("\nNilai harus antara 0-100.")
        return
    
    data_mahasiswa[nim_baru] = {
        'nama': nama_baru,
        'nilai': nilai_baru
    }
    print("\nData Mahasiswa Berhasil Ditambahkan.")
# tambah_data_mahasiswa(buka_data)
# simpan_data_mahasiswa(nama_file, buka_data)

# ================================================
# Praktikum 2 : Konsep ADT dan FIle Handling (Studi Kasus)
# Latihan Dasar 6 : Membuat Fungsi Menu Utama
# ================================================

def menu_utama():
    buka_data = load_data_mahasiswa(nama_file)
    while True:
        print("\n Selamat Datang di Sistem Data Mahasiswa")
        print("\n=== Menu Utama ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Update Data Mahasiswa")
        print("4. Simpan Data Mahasiswa")
        print("5. Tambah Data Mahasiswa")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ").strip()
        
        if pilihan == '1':
            tampil_data_mahasiswa(buka_data)
        elif pilihan == '2':
            cari_data_mahasiswa(buka_data)
        elif pilihan == '3':
            update_data_mahasiswa(buka_data)
        elif pilihan == '4':
            simpan_data_mahasiswa(nama_file, buka_data)
        elif pilihan == '5':
            tambah_data_mahasiswa(buka_data)
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
menu_utama()
