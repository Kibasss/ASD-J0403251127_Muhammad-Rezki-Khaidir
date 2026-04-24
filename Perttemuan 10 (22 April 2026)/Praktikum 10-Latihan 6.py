# =================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 6 : Rotasi Kanan (Right Rotate) pada BST
# =================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Fungsi standard untuk menyisipkan data baru ke BST
def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
        
    return root

# Fungsi untuk menampilkan struktur pohon agar mirip dengan visualisasi gambar
def visualisasi(root, indent="", position="Root"):
    if root is not None:
        print(f"{indent}{position}: {root.data}")
        visualisasi(root.left, indent + "    ", "L")
        visualisasi(root.right, indent + "    ", "R")

# Preorder traversal untuk melihat urutan penyimpanan data (Root, Kiri, Kanan)
def preorder(root):
    if root is not None:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def right_rotate(y):
    print(f"\n*** Melakukan Rotasi Kanan pada node: {y.data} ***")
    # 1. Identifikasi root baru (x) dan sub-tree kanan root baru (T2)
    x = y.left       # x = root baru (misal: 20)
    T2 = x.right    # T2 = sub-tree kanan dari x, yang akan dipindahkan (misal: None)

    # 2. Lakukan Rotasi
    x.right = y      # Old root (30) menjadi anak kanan dari new root (20)
    y.left = T2      # Sub-tree kanan dari new root (None) menjadi anak kiri dari old root (30)

    # 3. Kembalikan New Root untuk memperbarui pointer pohon
    return x

# ----------------------------- 
# Program utama 
# ----------------------------- 

# Data dari gambar: 30, 20, 10
data_to_skew = [30, 20, 10] 
root = None

print("=========================================")
print("  LATIHAN 6: ROTASI KANAN PADA BST  ")
print("=========================================\n")

print(f"Data input: {data_to_skew}")

for data in data_to_skew:
    root = insert(root, data)

print("\n--- KEADAAN AWAL: POHON TIDAK SEIMBANG (Left-Left Skewed) ---")
print("Visualisasi Struktur Pohon (mirip gambar 'Sebelum'):")
visualisasi(root)
print("\nTraversal Preorder (urutan data): ", end="")
preorder(root)
print()

new_root = right_rotate(root)

print("\n--- KEADAAN AKHIR: POHON SEIMBANG (Balanced BST) ---")
print("Visualisasi Struktur Pohon (mirip gambar 'Sesudah'):")
visualisasi(new_root)
print("\nTraversal Preorder (urutan data baru): ", end="")
preorder(new_root)
print()

'''
Pembahasan:
Program ini mengimplementasikan teknik Rotasi Kanan (Right Rotate) untuk menyeimbangkan Binary Search Tree (BST) yang mengalami kondisi berat sebelah ke kiri (Left-Left Skewed).
Ketika data dimasukkan secara berurutan dari besar ke kecil (misalnya 30, lalu 20, lalu 10), pohon akan membentuk garis lurus ke cabang kiri yang membuat proses pencarian menjadi lambat.
Melalui fungsi right_rotate, sistem memperbaiki struktur ini dengan cara menggeser posisi node searah jarum jam: nilai 20 "dinaikkan" posisinya menjadi akar (root) utama yang baru,
sementara nilai 30 (akar yang lama) "diturunkan" menjadi anak sebelah kanannya. Apabila node 20 sebelumnya memiliki anak di sebelah kanan, data tersebut akan dialihkan menjadi anak kiri dari node 30.
Proses rotasi ini secara efektif mengubah struktur yang miring sebelah menjadi pohon yang seimbang, sehingga performa sistem tetap optimal.
'''