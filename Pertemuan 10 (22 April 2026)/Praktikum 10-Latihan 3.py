#=================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 3 : Search BST
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

def search(root,key): #Mencari data di BST
    if root is None: #Jika node kosong
        return False
    
    if root.data == key: #Jika data ditemukan
        return True

    if key < root.data: #Jika key lebih kecil, cari di kiri
        return search(root.left,key)
    else: #Jika key lebih besar, cari di kanan
        return search(root.right,key)
    
#Uji pencarian
key = 40
if search(root,key) is True:
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")

'''
Pembahasan:
Program ini menambahkan fungsi pencarian cerdas pada struktur Binary Search Tree (BST) untuk mendeteksi apakah suatu data tertentu ada di dalam sistem atau tidak.
Logikanya sangat efisien: sistem akan membandingkan angka yang dicari dengan posisi node saat ini; jika belum cocok, pencarian hanya akan berlanjut ke cabang kiri 
(untuk angka yang lebih kecil) atau cabang kanan (untuk angka yang lebih besar) tanpa harus mengecek seluruh data satu per satu. Dengan metode eliminasi ini,
proses pencarian menjadi sangat cepat karena sistem langsung mengabaikan jalur yang tidak relevan hingga data ditemukan atau dipastikan tidak ada.
'''