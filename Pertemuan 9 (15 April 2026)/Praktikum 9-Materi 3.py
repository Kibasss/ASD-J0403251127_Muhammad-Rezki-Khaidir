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
Kode ini memperkenalkan fungsi Traversal Preorder, yaitu sebuah teknik untuk "berkunjung" dan mencatat setiap data dalam pohon dengan urutan sistematis yang dimulai dari Root (induk), lalu masuk ke cabang Left (kiri), dan terakhir ke cabang Right (kanan). 
Melalui fungsi preorder(node), program menggunakan cara kerja rekursif di mana ia akan terus mendatangi anak sebelah kiri sedalam mungkin (dari A ke B, lalu ke D) sebelum akhirnya mundur untuk mengecek cabang kanan yang tersisa, sehingga menghasilkan urutan cetak "A B D E C" yang menggambarkan rute perjalanan menyusuri sisi kiri pohon hingga tuntas sebelum berpindah ke sisi lainnya.
'''