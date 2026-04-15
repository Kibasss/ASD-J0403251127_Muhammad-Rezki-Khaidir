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
        inorder(node.data, end=" ") # Kunjungi node saat ini
        inorder(node.right) # Kunjungi child kanan
