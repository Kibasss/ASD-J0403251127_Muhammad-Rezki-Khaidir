# ==========================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 6: Struktur Organisasi Perusahaan
# ==========================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

def preorder(node):
    if node is not None:
        print(node.data, end=" ") # Menampilkan data pada node
        preorder(node.left) # Traversal ke child kiri
        preorder(node.right) # Traversal ke child kanan

# Membuat Tree Struktur Organisasi Perusahaan
root = Node("Direktur")

# Child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.left = Node("Staff 3")

# Menjalankan transversal preorder
print("Struktur Organisasi (preorder): ")
preorder(root)

# Pembahasan:
'''
Pada latihan keenam ini, kode ini mengaplikasikan konsep Tree ke dalam studi kasus nyata yaitu Struktur Organisasi, di mana setiap jabatan direpresentasikan sebagai sebuah node yang memiliki hubungan atasan-bawahan. 
Dengan menggunakan fungsi preorder, program akan membaca struktur ini berdasarkan garis komando yang dimulai dari jabatan tertinggi yaitu Direktur, lalu turun menelusuri seluruh departemen di bawah Manajer A (dari Staff 1 ke Staff 2), baru kemudian berpindah ke departemen Manajer B dan stafnya. 
Hasil urutan cetaknya mencerminkan cara kerja organisasi yang hierarkis, di mana pimpinan utama disebut terlebih dahulu sebelum merinci satu per satu tim di bawahnya secara sistematis.
'''