# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 4: 
# ===================================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Membuat fungsi inorder: left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left) # Kunjungi child kiri
        print(node.data, end=" ") # Kunjungi node saat ini
        inorder(node.right) # Kunjungi child kanan

# Membuat Tree
# Membuat Node Root
root = Node("A")

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan hasil Traversal Inorder
print("Hasil Traversal Inorder : ")
inorder(root) # Output: D B E A C

# Pembahasan:
'''
Pada kode di atas, kita membuat sebuah class Node yang memiliki atribut data, left, dan right.
Atribut data digunakan untuk menyimpan nilai pada node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan kanan dari node tersebut.
Pada contoh penggunaan, kita membuat sebuah node root dengan data "A" dan menambahkan child kiri "B" dan child kanan "C".
Selanjutnya, kita menambahkan child kiri "D" dan child kanan "E" pada node "B". Terakhir, kita menampilkan hasil dari traversal inorder yang mengunjungi child kiri terlebih dahulu, kemudian node saat ini, dan terakhir child kanan.
'''