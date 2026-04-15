# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 1: Membuat Node
# ===================================================================

# Class Node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan Nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan

# Membuat Root
root = Node("A") # Membuat node root dengan data "A"

# Menampilkan isi node root
print("Data Root:", root.data) # Output: A
print("Data Child Kiri Root:", root.left) # Output: None
print("Data Child Kanan Root:", root.right) # Output: None

# Pembahasan:
'''
Kode ini adalah cara mendefinisikan sebuah Node atau unit dasar dalam struktur data Tree, di mana setiap Node diibaratkan sebagai sebuah kotak yang memiliki tiga bagian utama: identitas atau nilai yang disimpan (data), serta dua "tangan" (left dan right) untuk terhubung ke kotak lain di bawahnya. 
Karena kode ini baru membuat satu objek bernama root dengan isi "A", maka saat dijalankan, sistem hanya menampilkan data utamanya saja, sementara tangan kiri dan kanannya masih bernilai None atau kosong karena belum ada cabang atau "anak" yang kamu sambungkan ke node utama tersebut.
'''