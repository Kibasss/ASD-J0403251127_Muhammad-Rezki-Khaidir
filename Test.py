import csv
import random

# --- 1. Inisialisasi Data ---
# List untuk menyimpan data pemain dalam bentuk dictionary [cite: 27, 28]
leaderboard_data = [] 
# Stack untuk menyimpan riwayat (history) aktivitas terakhir [cite: 34, 35]
history_stack = [] 

# --- 2. Fungsi File Handling  ---
def load_data():
    """Membaca data dari file CSV ke dalam List [cite: 67]"""
    try:
        with open('data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Pastikan skor diubah ke integer agar bisa di-sorting [cite: 30]
                row['skor'] = int(row['skor'])
                leaderboard_data.append(row)
    except FileNotFoundError:
        print("File data.csv belum ada, akan dibuat otomatis nanti.")

def save_data():
    """Menyimpan data dari List ke file CSV [cite: 68]"""
    fieldnames = ['nama', 'skor']
    with open('data.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(leaderboard_data)

# --- 3. Fungsi Gameplay [cite: 69] ---
def play_game():
    print("\n--- Game Tebak Angka ---")
    nama = input("Masukkan nama kamu: ")
    angka_rahasia = random.randint(1, 10) # Sistem menentukan angka [cite: 53]
    kesempatan = 3 # Maksimal 3 kesempatan [cite: 22, 54]
    
    while kesempatan > 0:
        tebakan = int(input(f"Tebak angka (1-10) [Sisa {kesempatan}]: "))
        if tebakan == angka_rahasia:
            print(f"Selamat {nama}, tebakanmu benar!")
            skor = kesempatan * 10 # Contoh perhitungan skor sederhana
            leaderboard_data.append({"nama": nama, "skor": skor}) 
            history_stack.append(f"Pemain {nama} baru saja bermain dengan skor {skor}")
            break
        else:
            kesempatan -= 1
            if kesempatan > 0:
                # Memberikan clue sederhana [cite: 22, 55]
                clue = "lebih besar" if angka_rahasia > tebakan else "lebih kecil"
                print(f"Salah! Clue: Angka rahasia {clue} dari {tebakan}.")
            else:
                print(f"Yah, kesempatan habis. Angka rahasianya adalah {angka_rahasia}.") 
    save_data() 

# --- 4. Fungsi Leaderboard & CRUD [cite: 71, 72, 73, 74] ---
def tampilkan_leaderboard():
    # Contoh Algoritma Sorting sederhana (mengurutkan skor tertinggi ke terendah) [cite: 15]
    sorted_data = sorted(leaderboard_data, key=lambda x: x['skor'], reverse=True)
    
    print("\n--- Leaderboard Skor ---")
    for i, p in enumerate(sorted_data, 1):
        print(f"{i}. {p['nama']} - {p['skor']} poin")

def lihat_history():
    """Menampilkan aktivitas terakhir menggunakan konsep Stack (LIFO) [cite: 38, 39]"""
    print("\n--- Riwayat Aktivitas Terakhir (Stack) ---")
    if not history_stack:
        print("Belum ada aktivitas.")
    else:
        # Menampilkan dari yang paling baru ditambahkan 
        for act in reversed(history_stack):
            print(f"- {act}")

# --- 5. Menu Utama [cite: 44, 45] ---
def main_menu():
    load_data()
    while True:
        print("\n=== APLIKASI LEADERBOARD TEBAK ANGKA ===")
        print("1. Main Game")
        print("2. Lihat Leaderboard")
        print("3. Cari Pemain")        # Tambahan baru
        print("4. Update Skor")        # Tambahan baru
        print("5. Hapus Data Pemain")  # Tambahan baru
        print("6. Lihat Riwayat (Stack)")
        print("7. Keluar")
        
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            play_game()
        elif pilihan == '2':
            tampilkan_leaderboard()
        elif pilihan == '3':
            cari_pemain()     # Memanggil fungsi cari
        elif pilihan == '4':
            update_skor()     # Memanggil fungsi update
        elif pilihan == '5':
            hapus_pemain()    # Memanggil fungsi hapus
        elif pilihan == '6':
            lihat_history()
        elif pilihan == '7':
            print("Sampai jumpa!")
            break

# --- Tambahan Fungsi CRUD ---

def cari_pemain():
    """Mencari data pemain berdasarkan nama (Searching)"""
    nama_cari = input("\nMasukkan nama pemain yang dicari: ")
    # Menggunakan Linear Search sederhana
    found = False
    for p in leaderboard_data:
        if p['nama'].lower() == nama_cari.lower():
            print(f"Data ditemukan: {p['nama']} - Skor: {p['skor']}")
            found = True
            break
    if not found:
        print("Pemain tidak ditemukan.")

def update_skor():
    """Mengubah skor pemain (Update)"""
    nama_cari = input("\nMasukkan nama pemain yang skornya ingin diubah: ")
    for p in leaderboard_data:
        if p['nama'].lower() == nama_cari.lower():
            skor_baru = int(input(f"Masukkan skor baru untuk {p['nama']}: "))
            p['skor'] = skor_baru
            history_stack.append(f"Update skor {p['nama']} menjadi {skor_baru}")
            save_data()
            print("Skor berhasil diperbarui!")
            return
    print("Nama pemain tidak ditemukan.")

def hapus_pemain():
    """Menghapus data pemain (Delete)"""
    nama_cari = input("\nMasukkan nama pemain yang ingin dihapus: ")
    for i in range(len(leaderboard_data)):
        if leaderboard_data[i]['nama'].lower() == nama_cari.lower():
            pemain_terhapus = leaderboard_data.pop(i)
            history_stack.append(f"Menghapus pemain: {pemain_terhapus['nama']}")
            save_data()
            print(f"Data {pemain_terhapus['nama']} telah dihapus.")
            return
    print("Nama tidak ditemukan.")

if __name__ == "__main__":
    main_menu()