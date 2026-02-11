class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # --- Latihan 5: Metode Reverse (Sesuai Gambar Tugas) ---
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        temp = self.head
        if not temp:
            print("null")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# --- Bagian Input Satu Per Satu ---
llr = LinkedList()

print("=== Input Data Linked List untuk di-Reverse ===")
while True:
    input_user = input("Masukkan angka (atau ketik 'n' untuk mulai membalikkan): ")
    
    if input_user.lower() == 'n':
        break
    
    if input_user.lstrip('-').isdigit():
        llr.append(int(input_user))
    else:
        print("Input salah, masukkan angka ya!")

# --- Proses Reverse ---
if llr.head:
    print("\n" + "="*30)
    print("Linked List sebelum dibalik:", end=" ")
    llr.display()

    llr.reverse()

    print("Linked List setelah dibalik:", end=" ")
    llr.display()
    print("="*30)
else:
    print("\nWah, list-nya masih kosong, nggak ada yang bisa dibalik!")