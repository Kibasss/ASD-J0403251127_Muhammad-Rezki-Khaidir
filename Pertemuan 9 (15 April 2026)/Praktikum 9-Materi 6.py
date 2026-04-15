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
Pada kode di atas, kita membuat sebuah class Node yang memiliki atribut data, left, dan right.
Atribut data digunakan untuk menyimpan nilai pada node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan kanan dari node tersebut.
Pada contoh penggunaan, kita membuat sebuah node root dengan data "Direktur" dan menambahkan child kiri "Manajer A" dan child kanan "Manajer B".
Selanjutnya, kita menambahkan child kiri "Staff 1" dan child kanan "Staff 2" pada node "Manajer A", serta child kiri "Staff 3" pada node "Manajer B". 
Terakhir, kita menampilkan struktur organisasi perusahaan menggunakan traversal preorder yang mengunjungi node root terlebih dahulu, kemudian child kiri, dan terakhir child kanan.
'''