class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        temp = self.head
        print("Isi Doubly Linked List saat ini:", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("null")

# --- Bagian Input Satu Per Satu ---
dll = DoublyLinkedList()

print("=== Silahkan Input Data Doubly Linked List Satu Per Satu ===")
while True:
    input_user = input("Masukkan elemen (atau ketik 'n' untuk selesai): ")
    
    if input_user.lower() == 'n':
        dll.display()
        break
    
    if input_user.lstrip('-').isdigit(): # Support angka negatif juga
        dll.append(int(input_user))
    else:
        print("Input tidak valid, masukkan angka ya!")

# --- Bagian Pencarian ---
if dll.head:
    target = input("\nMasukkan elemen yang ingin dicari: ")
    if target.lstrip('-').isdigit():
        target_int = int(target)
        if dll.search(target_int):
            print(f"Elemen {target_int} ditemukan dalam Doubly Linked List.")
        else:
            print(f"Elemen {target_int} tidak ditemukan.")
else:
    print("List kosong, tidak ada yang bisa dicari.")