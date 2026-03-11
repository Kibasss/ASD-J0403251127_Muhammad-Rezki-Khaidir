# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Muhammad Rezki Khaidir
# NIM     : J0403251127
# Kelas   : TPL PB/1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1)
def muat_data_buku(nama_file):
    database_buku = {} # Membuat dictionary untuk menyimpan data buku
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() # Menghapus karakter newline dan spasi di awal/akhir
            kode_buku, judul, Harga = baris.split(",") # Memisahkan data berdasarkan koma
            database_buku[kode_buku] = {
                "kode_buku": kode_buku, # Menyimpan kode buku sebagai key utama dalam dictionary
                "judul": judul, # Menyimpan judul buku sebagai string dan value dalam dictionary
                "harga": int(Harga) # Menyimpan harga buku sebagai integer dan value dalam dictionary
            }
    return database_buku # Mengembalikan dictionary yang berisi data buku yang telah dimuat dari file teks

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2)
class Node:
    def __init__(self, judul_buku):
        self.judul = judul_buku # Menyimpan judul buku sebagai atribut dalam node
        self.next = None # Menyimpan referensi ke node berikutnya dalam linked list, diinisialisasi dengan None yang menunjukkan bahwa node ini belum terhubung dengan node lain

class LinkedListPromosi:
    def __init__(self):
         self.head = None

# Metode untuk menambahkan buku ke dalam daftar promosi. Buku baru akan ditambahkan di akhir linked list.
    def tambah_buku_promosi(self, judul_buku):
        buku_promosi = Node(judul_buku)
        if self.head is None:
            self.head = buku_promosi
            return
        buku_terakhir = self.head
        while buku_terakhir.next is not None:
            buku_terakhir = buku_terakhir.next
        buku_terakhir.next = buku_promosi

# Metode untuk menampilkan daftar buku yang sedang dalam promosi. Buku akan ditampilkan dalam urutan penambahan (FIFO).
    def tampilkan_promosi(self):
        buku_sekarang = self.head
        if buku_sekarang is None:   
            print("Tidak ada buku dalam promosi.")
            return
        urutan = 1
        while buku_sekarang is not None:
            print(f"{urutan}. {buku_sekarang.judul}")
            buku_sekarang = buku_sekarang.next
            urutan += 1
        print("================\n")

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3)
class AntreanKasir:
    def __init__(self):
        self.antrean = []

    def is_empty(self):
        return self.front is None

# Metode untuk menambahkan pelanggan ke dalam antrean kasir. Pelanggan baru akan ditambahkan di akhir antrean (FIFO).
    def tambah_antrean(self, nama_pelanggan):
        self.antrean.append(nama_pelanggan)
        print(f"{nama_pelanggan} telah masuk ke antrean.")

# Metode untuk menampilkan daftar pelanggan yang sedang dalam antrean kasir. Pelanggan akan ditampilkan dalam urutan kedatangan (FIFO).
    def tampilkan_antrean(self):
        print("Antrean Kasir Saat Ini:")
        if len(self.antrean) == 0:
            print("Tidak ada pelanggan dalam antrean.")
        else:
            nomor = 1
            for nama in self.antrean:
                print(f"{nomor}.{nama}")
                nomor += 1
        print("================\n")

# Metode untuk melayani pelanggan yang berada di depan antrean kasir. Pelanggan yang dilayani akan dihapus dari antrean (FIFO).
    def layani_pelanggan(self):
        if len(self.antrean) == 0:
            print("Tidak ada pelanggan dalam antrean.")
            return
        pelanggan_dilayani = self.antrean.pop(0)
        print(f"{pelanggan_dilayani} sedang dilayani.")

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4)
# Fungsi untuk mengurutkan daftar harga transaksi menggunakan algoritma Insertion Sort. Daftar harga akan diurutkan dari yang terkecil hingga terbesar.
def urutkan_transaksi(list_harga):
    for i in range(1, len(list_harga)):
        key = list_harga[i]
        j = i - 1
        while j >= 0 and list_harga[j] > key:
            list_harga[j + 1] = list_harga[j]
            j -= 1
        list_harga[j + 1] = key
    return list_harga # Mengembalikan daftar harga yang telah diurutkan menggunakan algoritma Insertion Sort

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "Pertemuan 7 (11 Maret 2026)/Quiz Praktikum/buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    #Menu Antarmuka untuk mengakses berbagai fitur sistem manajemen toko buku.
    #Pengguna dapat memilih opsi untuk melihat katalog buku, mengelola daftar promosi, mengelola antrean kasir, melihat laporan penjualan terurut, atau keluar dari program.
    #Setiap opsi akan memanggil fungsi atau metode yang sesuai untuk menjalankan fitur yang dipilih oleh pengguna.
    #Program akan terus berjalan hingga pengguna memilih untuk keluar (pilihan 5).

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        # Meminta pengguna untuk memilih opsi dari menu utama. Input akan diproses untuk menentukan fitur mana yang akan dijalankan berdasarkan pilihan pengguna.
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\nKatalog Buku:", data_buku)
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            print("1. Tambah Pelanggan ke Antrean") # Menampilkan opsi untuk menambahkan pelanggan ke antrean kasir. Pengguna dapat memasukkan nama pelanggan yang akan ditambahkan ke dalam antrean.
            print("2. Layani Antrian") # Menampilkan opsi untuk melayani pelanggan yang berada di depan antrean kasir. Pengguna dapat memilih untuk melayani pelanggan, yang akan menghapus pelanggan tersebut dari antrean.
            sub_pilihan = input("Pilih opsi (1-2): ")
            if sub_pilihan == '1':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)
                antrean_toko.tampilkan_antrean()
            elif sub_pilihan == '2':
                antrean_toko.layani_pelanggan()
                antrean_toko.tampilkan_antrean()
            # Tambahkan logika untuk melayani jika diperlukan

# Opsi untuk melihat laporan penjualan terurut. Program akan menampilkan daftar harga transaksi sebelum dan sesudah diurutkan menggunakan algoritma Insertion Sort.
        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

# Opsi untuk keluar dari program. Program akan menampilkan pesan terima kasih dan menghentikan eksekusi.
        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

# Program utama akan dijalankan jika file ini dieksekusi secara langsung. Fungsi main() akan dipanggil untuk memulai program dan menampilkan menu antarmuka kepada pengguna.
if __name__ == "__main__":
    main()