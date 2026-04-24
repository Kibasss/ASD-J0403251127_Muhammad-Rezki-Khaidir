#=================================================
# Nama : Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 4 : Membuat BST yang tidak seimbang
#=================================================

class Node:
    def __init__(self, data):  #Inisialisasi
        self.data = data
        self.right = None
        self.left = None

def insert(root,data): #Menambahkan Node
    if root is None: #Jika belum ada node, buat node baru
        return Node(data)
    
    if data<root.data:  # Jika data lebih kecil, geser ke kiri
        root.left = insert(root.left,data)
    elif data>root.data: #Jika lebih besar, geser ke kanan
        root.right = insert(root.right,data)

    return root

#Mengisi data BST
root = None
data_list = [50,30,70,20,40,50,80]
for data in data_list:
    root = insert(root,data)


def preorder(root): #Traversal Preorder
    if root is not None:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)

def tampil_struktur(root, level=0, posisi="Root"): #Menampilkan struktur BST
    if root is not None:
        print(" "*level + f"{posisi}: {root.data}")
        tampil_struktur(root.left,level+1,"L")
        tampil_struktur(root.right,level+1,"R")


# ----------------------------- 
# Program utama 
# ----------------------------- 

print("Preorder BST:") 
preorder(root) 
print("\n\nStruktur BST:") 
tampil_struktur(root)

'''
Pembahasan:
Kode ini bertujuan untuk memvisualisasikan bagaimana sebuah Binary Search Tree (BST) terbentuk dan bercabang secara nyata di dalam memori. 
Dengan menggunakan fungsi tampil_struktur, program akan memetakan posisi setiap angka mulai dari akar utama (root) hingga ke cabang kiri (L) dan kanan (R) 
secara hierarkis sesuai urutan input data. Selain itu, terdapat fitur Preorder Traversal yang menampilkan urutan data dengan prinsip mengunjungi induk terlebih dahulu 
sebelum turun ke anak-anaknya, sehingga siapa pun yang melihat kode ini bisa memahami gambaran utuh apakah struktur pohon yang dihasilkan sudah seimbang
atau justru condong ke satu sisi tertentu.
'''