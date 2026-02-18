# ===================================
# Implementasi Dasar: Node Pada Linked List
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# ===================================

# Membuat kelas Node yang merupakan unit dasar dari linked list
class Node:
    def __init__(self, data): # Konstruktor untuk menginisialisasi node dengan data dan pointer ke node berikutnya
        self.data = data # Menyimpan data yang diberikan saat pembuatan node
        self.next = None # Inisialisasi pointer next sebagai None, yang berarti node ini belum terhubung ke node lain

# Proses Pertama Membuat Node Secara Satu Per Satu
nodeA=Node("A")
nodeB=Node("B")
nodeC=Node("C")

# Menghubugkan Node: A -> B -> C
nodeA.next = nodeB # Node A menunjuk ke Node B
nodeB.next = nodeC # Node B menunjuk ke Node C

# Menentukan Node Pertama
head = nodeA

# Traversal: Menelusuri Dari Head Sampai None
current = head
while current is not None: 
    print(current.data) # Cetak data dari node saat ini
    current = current.next # Pindah ke node 
    
# ===================================
# Implementasi Dasar:  Linked List + Insert Awal
# ===================================

class LinkedList:
    def __init__(self):
        self.head = None # Inisialisasi head sebagai None, yang berarti linked list kosong

    def insert_awal(self, data):
        nodeBaru = Node(data)
        nodeBaru.next = self.head 
        self.head = nodeBaru 

    def hapus_awal(self):
        data_terhapus = self.head.data
        self.head = self.head.next
        print("Data", data_terhapus, "telah dihapus")

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


print("=== List Awal ===")
ll=LinkedList()
ll.insert_awal("A")
ll.insert_awal("B")
ll.insert_awal("C")
ll.tampilkan()
ll.hapus_awal()
print("=== List Setelah Hapus Awal ===")
ll.tampilkan()