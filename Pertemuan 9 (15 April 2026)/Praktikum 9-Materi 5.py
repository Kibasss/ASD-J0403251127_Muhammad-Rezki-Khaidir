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
Kode ini menerapkan teknik Traversal Postorder, yaitu metode pembacaan pohon dengan urutan Kiri -> Kanan -> Root, yang secara prinsip memproses seluruh anak atau cabang terlebih dahulu sebelum akhirnya memproses induknya sendiri. 
Melalui fungsi rekursif postorder(node), program akan menelusuri jalur paling dalam hingga mencetak "D" dan "E" sebagai ujung terbawah, baru kemudian naik ke induk mereka yaitu "B", dilanjutkan ke sisi kanan yaitu "C", dan diakhiri dengan akar paling utama yaitu "A", sehingga urutan "D E B C A" ini mencerminkan proses penyelesaian tugas dari tingkat yang paling bawah atau daun menuju ke arah akar.
'''