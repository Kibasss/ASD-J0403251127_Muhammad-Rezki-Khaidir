#=================================================
# Nama : Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 1 : BST
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

for data in data_list: #Menambahkan setiap elemen dalam data_list ke dalam Node
    root = insert(root,data)

print("BST berhasil dibuat")

'''
Pembahasan:
Kode ini mengimplementasikan struktur data Binary Search Tree (BST), yang berfungsi untuk mengorganisir sekumpulan data angka secara hierarkis agar proses pencarian 
menjadi lebih efisien. Setiap data baru yang masuk akan dibandingkan dengan nilai induk (node); jika nilainya lebih kecil, data akan diarahkan ke cabang kiri, dan jika lebih besar,
data akan diarahkan ke cabang kanan secara rekursif melalui fungsi insert. Dengan mengikuti aturan penempatan tersebut, kode ini secara otomatis membentuk struktur "pohon"
yang seimbang dari daftar angka yang diberikan, memastikan seluruh data tersusun rapi sesuai urutan besarnya.
'''