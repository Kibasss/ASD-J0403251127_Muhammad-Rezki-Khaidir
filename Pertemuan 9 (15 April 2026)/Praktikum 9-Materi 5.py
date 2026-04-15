# ==========================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 5: Membuat Traversal Postorder
# ==========================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# Fungsi Postorder : Left -> Right -> Root
def postorder(node):
    if node is not None:
        postorder(node.left) # Traversal ke child kiri
        postorder(node.right) # Traversal ke child kanan
        print(node.data, end=" ") # Menampilkan data pada node

# Membuat Node Root
root = Node("A") # Membuat node root dengan data "A"

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan hasil Traversal Postorder
print("Hasil Traversal Postorder : ")
postorder(root) # Output: D E B C A

# Pembahasan:
'''
Pada kode di atas, kita membuat sebuah class Node yang memiliki atribut data, left, dan right.
Atribut data digunakan untuk menyimpan nilai pada node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan kanan dari node tersebut.
Pada contoh penggunaan, kita membuat sebuah node root dengan data "A" dan menambahkan child kiri "B" dan child kanan "C".
Selanjutnya, kita menambahkan child kiri "D" dan child kanan "E" pada node "B". Terakhir, kita menampilkan hasil dari traversal postorder yang mengunjungi child kiri terlebih dahulu, kemudian child kanan, dan terakhir node root.
'''