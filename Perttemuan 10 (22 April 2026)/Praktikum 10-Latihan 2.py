#=================================================
# Nama : Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 2 : Traversal Inorder
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


def inorder(root): #Traversal Inorder
    if root is not None: #Jika node tidak kosong
        inorder(root.left) #Kunjungi sub tree kiri
        print(root.data, end=' ') #Tampilkan data node
        inorder(root.right) #Kunjungi sub tree kanan

print("Hasil inorder :") #Menampilkan hasil traversal
inorder(root) #Menjalankan traversal inorder
