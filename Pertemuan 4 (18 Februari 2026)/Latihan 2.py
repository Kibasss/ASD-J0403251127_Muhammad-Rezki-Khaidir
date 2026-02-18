# ===================================
# Implemetasi Dasar: Queue Dengan Linked List
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# ===================================

class Node:
    def __init__(self, data):  
        self.data = data 
        self.next = None 

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        nodeBaru = Node(data)
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    def dequeue(self):
        if self.is_empty():
            print("Queue kosong, tidak bisa dequeue")
            return None
        
        data_terhapus = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return data_terhapus
    
    def tampilkan(self):
        if self.is_empty():
            print("Queue kosong")
            return
        
        current = self.front
        print("\n--- Antrian Saat Ini Adalah ---")
        print("Front -> ", end="")

        while current is not None:
            if current.next is None:
                print(current.data,"-> Rear ", end="")
            else:
                print(current.data,"-> ", end="")
            current = current.next
        
        print("\n-------------------------------\n")

# Instantiasi QueueLL dan menambahkan elemen
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
