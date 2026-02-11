import os
import getpass
import stdiomask

nama_file = 'stock_barang.txt'

def load_data_barang(nama_file):
    data_barang = {}
    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()
            kode, nama, harga = baris.split(',')

            data_barang[kode] = {
                'nama': nama,
                'harga': int(harga)
            }
    return data_barang
buka_data = load_data_barang(nama_file)

def tampil_data_barang(data_barang):
    print("\n=== Data Barang ===")
    print(f"{'Kode':7} | {'Nama':<25} | {'Harga':>8}")
    print("-" * 50)

    for kode in sorted(data_barang.keys()):
        nama = data_barang[kode]['nama']
        harga = data_barang[kode]['harga']
        print(f"{kode:7} {nama:<25} {harga:>8}")

def cari_data_barang(data_barang):
    kode_input = input("Masukkan Kode Barang yang ingin dicari: ").upper().strip()
    if kode_input in data_barang:
        nama = data_barang[kode_input]['nama']
        harga = data_barang[kode_input]['harga']
        print("\nData Ditemukan:")
        print(f"Kode : {kode_input}")
        print(f"Nama : {nama}")
        print(f"Harga : {harga}")
    else:
        print("\nData Tidak Ditemukan.")

def update_stok_barang(data_barang):
    kode_input = input("Masukkan Kode Barang yang ingin diupdate stoknya: ").upper().strip()
    if kode_input in data_barang:
        nama = data_barang[kode_input]['nama']
        harga_lama = data_barang[kode_input]['harga']
        print(f"\nData Sebelumnya:")
        print(f"Kode : {kode_input}")
        print(f"Nama : {nama}")
        print(f"Harga : {harga_lama}")
        try:
            harga_baru = float(input("Masukkan Harga Baru: "))
            data_barang[kode_input]['harga'] = harga_baru
            print("\nData Berhasil Diupdate:")
            print(f"Kode : {kode_input}")
            print(f"Nama : {nama}")
            print(f"Harga : {harga_baru}")
        except ValueError:
            print("Input harga harus berupa angka.")
    else:
        print("\nData Tidak Ditemukan.")

def simpan_data_barang(nama_file, data_barang):
    with open(nama_file, 'w', encoding='utf-8') as file:
        for kode in data_barang:
            nama = data_barang[kode]['nama']
            harga = data_barang[kode]['harga']
            file.write(f"{kode},{nama},{harga}\n")
    print("\nData berhasil disimpan ke file.")

def tambah_data_barang(data_barang):
    kode_baru = input("Masukkan Kode Barang Baru: ").upper().strip()
    if kode_baru in data_barang:
        print("\nKode Barang sudah ada. Gunakan kode lain.")
        return
    nama_baru = input("Masukkan Nama Barang: ").strip()
    try:
        harga_baru = float(input("Masukkan Harga Barang: "))
    except ValueError:
        print("Harga harus berupa angka.")
        return

    data_barang[kode_baru] = {
        'nama': nama_baru,
        'harga': harga_baru
    }
    print("\nData Barang Baru Berhasil Ditambahkan.")

def login():
    print("\n=== Login ===")
    username_input = input("Masukkan Username: ")
    password_input = stdiomask.getpass("Masukkan Password: ", mask='*')

    nama_data = 'database_kasir.txt'

    try:
        with open(nama_data, 'r', encoding='utf-8') as kasir:
            found = False
            for baris in kasir:
                if ',' in baris:
                    user_saved, pass_saved = baris.strip().split(',')
                    if username_input == user_saved and password_input == pass_saved:
                        found = True
                        break
            if found:
                print("\nLogin Berhasil.")
            else:
                print("\nUsername atau Password Salah.")
    except FileNotFoundError:
        print("\nDatabase user tidak ditemukan.")


def menu_utama():
    while True:
        print("\n=== Selamat datang, Silahkan Login Terlebih Dahulu ===")
        print("1. Login")
        print("2. Keluar")
        pilihan = input("Pilih menu (1-2): ").strip()
        if pilihan == '1':
            login()
        elif pilihan == '2':
            print("Keluar dari program.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        while True:
            print("\n=== Menu Utama ===")
            print("1. Tampilkan Data Barang")
            print("2. Cari Data Barang")
            print("3. Update Harga Barang")
            print("4. Tambah Data Barang")
            print("5. Simpan Data Barang")
            print("6. Logout")
            pilihan = input("Pilih menu (1-6): ").strip()

            if pilihan == '1':
                tampil_data_barang(buka_data)
            elif pilihan == '2':
                cari_data_barang(buka_data)
            elif pilihan == '3':
                update_stok_barang(buka_data)
            elif pilihan == '4':
                tambah_data_barang(buka_data)
            elif pilihan == '5':
                simpan_data_barang(nama_file, buka_data)
            elif pilihan == '6':
                print("Berhasil Logout.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

menu_utama()

