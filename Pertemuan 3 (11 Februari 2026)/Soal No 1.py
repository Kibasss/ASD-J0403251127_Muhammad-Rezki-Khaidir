class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Fungsi nambah data ke belakang satu per satu
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Fungsi hapus sesuai gambar tugasmu
    def delete_node(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            print(f"\nOops! Angka {key} tidak ada di list.")
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        print("\nIsi Linked List saat ini:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# --- Bagian Input Satu Per Satu ---
ll = LinkedList()

print("=== Silahkan Input Data Satu Per Satu ===")
while True:
    input_user = input("Masukkan angka (atau ketik 'n' untuk berhenti): ")
    
    if input_user.lower() == 'n':
        ll.display()
        break
    
    # Cek apakah yang diinput benar-benar angka
    if input_user.isdigit():
        ll.append(int(input_user))
    else:
        print("Tolong masukkan angka yang valid ya!")

# --- Bagian Hapus Data ---
if ll.head:
    hapus = input("\nMasukkan angka yang ingin kamu hapus: ")
    if hapus.isdigit():
        ll.delete_node(int(hapus))
        print("Hasil akhir setelah dihapus:")
        ll.display()
else:
    print("List kosong, tidak ada yang bisa dihapus.")