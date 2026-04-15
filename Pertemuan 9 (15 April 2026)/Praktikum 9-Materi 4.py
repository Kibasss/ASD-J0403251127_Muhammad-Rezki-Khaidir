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
Pada latihan keempat ini, kode ini menggunakan teknik Traversal Inorder, yaitu metode pembacaan pohon dengan urutan Kiri -> Root -> Kanan yang bertujuan untuk mengunjungi data dari sisi paling kiri terlebih dahulu sebelum naik ke induknya dan berpindah ke sisi kanan. 
Melalui fungsi rekursif inorder(node), program akan terus menelusuri cabang kiri sampai ujung (ke node "D"), baru kemudian mencetak nilai induknya ("B"), lanjut ke anak kanan ("E"), kembali ke akar utama ("A"), dan diakhiri dengan sisi kanan paling luar ("C"), sehingga menghasilkan urutan "D B E A C" yang memberikan gambaran data dari perspektif horizontal atau mendatar.
'''