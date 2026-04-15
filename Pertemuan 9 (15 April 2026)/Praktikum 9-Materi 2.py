# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 2:
# ===================================================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data pada node
        self.left = None # Child kiri, awalnya None
        self.right = None # Child kanan, awalnya None

# Membuat Node Root
root = Node("A") # Membuat node root dengan data "A"

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi node root dan childnya
print("Data pada root : ", root.data) # Output: A
print("Data Child kiri root : ", root.left.data) # Output: B
print("Data Child kanan root : ", root.right.data) # Output: C
print("Data Child kiri dari B : ", root.left.left.data) # Output: D
print("Data Child kanan dari B : ", root.left.right.data) # Output: E

# Pembahasan: 
'''
Pada kode di atas, kita membuat sebuah class Node yang memiliki atribut data, left, dan right. 
Atribut data digunakan untuk menyimpan nilai pada node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan kanan dari node tersebut. 
Pada contoh penggunaan, kita membuat sebuah node root dengan data "A" dan menambahkan child kiri "B" dan child kanan "C". 
Selanjutnya, kita menambahkan child kiri "D" dan child kanan "E" pada node "B". Terakhir, kita menampilkan isi dari node root dan childnya.
'''