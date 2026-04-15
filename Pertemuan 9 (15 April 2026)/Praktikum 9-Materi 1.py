# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 1: Membuat Node
# ===================================================================

# Class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan Nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan

# Membuat Root
root = Node("A") # Membuat node root dengan data "A"

# Menampilkan isi node root
print("Data Root:", root.data) # Output: A
print("Data Child Kiri Root:", root.left) # Output: None
print("Data Child Kanan Root:", root.right) # Output: None


# Pembahasan :
# Pada kode di atas, kita membuat sebuah class Node yang memiliki atribut data, left, dan right. Atribut data digunakan untuk menyimpan nilai pada node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan kanan dari node tersebut. Pada contoh penggunaan, kita membuat sebuah node root dengan data "A" dan menampilkan isi dari node tersebut.