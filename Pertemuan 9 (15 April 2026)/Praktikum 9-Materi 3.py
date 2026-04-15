# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 3: Membuat Traversal Preorder
# ===================================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# Fungsi Preorder : Root -> Left -> Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ") # Menampilkan data pada node
        preorder(node.left) # Traversal ke child kiri
        preorder(node.right) # Traversal ke child kanan

# Membuat Node Root
root = Node("A") # Membuat node root dengan data "A"

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan hasil Traversal Preorder
print("Hasil Traversal Preorder : ")
preorder(root) # Output: A B D E C

# Pembahasan:
'''
Pada kode di atas, kita membuat sebuah class Node yang memiliki atribut data, left, dan right. 
Atribut data digunakan untuk menyimpan nilai pada node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan kanan dari node tersebut.
Pada contoh penggunaan, kita membuat sebuah node root dengan data "A" dan menambahkan child kiri "B" dan child kanan "C".
Selanjutnya, kita menambahkan child kiri "D" dan child kanan "E" pada node "B". Terakhir, kita menampilkan hasil dari traversal preorder yang mengunjungi node root terlebih dahulu, kemudian child kiri, dan terakhir child kanan.
'''