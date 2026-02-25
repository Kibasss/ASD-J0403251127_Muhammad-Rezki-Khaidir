# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# ===================================

# ===================================
# Studi Kasus : Sistem Antrian Layanan Akademik
# Implementasi Queue
# Enqueue : Memindahkan Pointer Rear (Menambahkan Data Baru dari Belakang)
# Dequeue : Memindahkan Pointer Front (Menghapus Data dari Depan)
# Front -> A ->b -> B -> C -> Rear
# ===================================

# 1. Medefenisikan Node (Unit Dasar Linked List)
class node:
    def __init__(self,nim,nama):
        self.nim = nim
        self.nama = nama
        self.next = None

# 2. Mendefenisikan Queue, Terdiri dari Front dan Rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self,nim,nama):
        nodeBaru = node(nim,nama)
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
        else:
            self.rear.next = nodeBaru
            self.rear = nodeBaru

    def dequeue(self):
        if self.is_empty():
            print("Antrian Kosong. Tidak Ada Mahasiswa yang Dilayani")
            return None
        node_dilayani = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return node_dilayani
    
    def tamplikan(self):
        if self.is_empty():
            print("Antrian Kosong.")
            return
        
        print("Daftar Antrian Mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim}-{current.nama}")
            current = current.next
            no += 1
        print("")

def main():
    q = queueAkademik()
    while True:
        print("===== Sistem Antrian Akademik =====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4): ").strip()
        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()
            q.enqueue(nim,nama)
            print("Berhasil Menambahkan Mahasiswa ke dalam Antrian.")

        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani:
                print(f"Mahasiswa dilayani: {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tamplikan()

        elif pilihan == "4":
            print("Terima Kasih, Sampai Jumpa Kembali")
            break
        
        else:
            print("Pilihan Tidak Valid. Silahkan Pilih yang Tersedia.")
                
if  __name__ == "__main__":
    main()