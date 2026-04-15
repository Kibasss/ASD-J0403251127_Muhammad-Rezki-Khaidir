# ==========================================================
# Nama: Muhammad Rezki Khaidir
# NIM : J0403251127
# Kelas : TPL PB/1
# Latihan 6 : Struktur Organisasi Perusahaan
# ==========================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# Membuat Tree Struktur Organisasi Perusahaan
root = Node("Direktur")

# Child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.left = Node("Staff 3")