# ==========================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Fungsi preorder untuk melihat isi tree
def preorder(root):
        if root is not None:
            print(root.data, end=" ")
            preorder(root.left)
            preorder(root.right)

# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
        if root is not None:
            print(" " * level + f"{posisi}: {root.data}")
            tampil_struktur(root.left, level + 1, "L")
            tampil_struktur(root.right, level + 1, "R")

# Fungsi rotasi kiri
def rotate_left(x):
    # x adalah root lama
    y = x.right # y adalah child kanan x
    T2 = y.left # subtree kiri milik y disimpan sementara

    # Proses rotasi
    y.left = x # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2
    # y menjadi root baru
    return y

# -----------------------------
# Program utama
# -----------------------------
# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)

'''
Pembahasan:
Program ini dirancang untuk memperbaiki struktur Binary Search Tree (BST) yang tidak seimbang karena terlalu condong ke sebelah kanan (Right-Right Skewed),
seperti pada kasus masuknya data 10, 20, dan 30 secara berurutan. Melalui fungsi rotate_left, sistem akan melakukan pergeseran arah
berlawanan jarum jam: node 10 (akar utama yang lama) akan "diturunkan" menjadi anak sebelah kiri, sementara node 20 "dinaikkan" posisinya untuk menjadi akar (root) yang baru.
Jika node 20 sebelumnya memiliki anak di sebelah kiri, anak tersebut akan otomatis dipindahkan menjadi anak kanan dari node 10. Melalui rotasi ini,
susunan pohon yang tadinya hanya memanjang lurus ke kanan berhasil diubah menjadi struktur pohon yang seimbang dan efisien.
'''