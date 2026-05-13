# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 13 - Graph III: Spanning Tree (Kruskal's & Prim's Approaches)
# Implementasi Kruskal's
# ===================================================================

# 1. Menyiapkan daftar jalan/kabel (edges) yang menghubungkan titik (node)
# Daftar Edge: (Bobot, Node 1, Node 2)
edges = [
    (1,'C','D'),
    (2,'A','C'),
    (3,'A','D'),
    (4,'A','B'),
    (5,'A','D'),
]

# 2. Kruskal mengurutkan semua jalan dari yang biayanya paling murah ke yang paling mahal supaya hasilnya bisa minimum
edges.sort()

# 3. Wadah kosong untuk menyimpan jalan yang dipilih untuk MST
mst = []
total_weight = 0

# 4. Catatan untuk memantau titik mana saja yang sudah terhubung dalam MST 
connected = set()

# 5. Proses pemilihan jalan untuk MST
for weight, u, v in edges:

    # Pengecekan terhubung ke jaringan, untuk mencegah adanya cycle (jalur berputar)
    if u not in connected or v not in connected:

        # Jika aman, masukkan jalan tersebut ke dalam MST
        mst.append((u, v, weight))

        # Tambahkan bobot jalan tersebut ke total bobot MST
        total_weight += weight

        # Tandai kedua titik sebagai terhubung dalam MST
        connected.add(u)
        connected.add(v)

# 6. Menampilkan hasil MST
print("Minimum Spanning Tree: ")

for edge in mst:
    print(edge)

# tampilkan total bobot MST yang paling efisien
print("Total Bobot MST:", total_weight)