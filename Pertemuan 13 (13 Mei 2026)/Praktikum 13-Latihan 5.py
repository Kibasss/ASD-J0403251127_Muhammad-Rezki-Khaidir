# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 13 - Graph III: Spanning Tree (Kruskal's & Prim's Approaches)
# Latihan 5: Program MST untuk Kasus Baru
# Kasus 1: Jaringan Jalan Antar Kota
# ===================================================================
# Menggunakan Algoritma Kruskal

# Daftar edge: (bobot, kota1, kota2)
edges = [
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (4, 'Depok', 'Bandung'),
    (5, 'Bogor', 'Jakarta'),
    (6, 'Jakarta', 'Bandung')
]

# Urutkan bobot termurah
edges.sort()
mst = []
total_weight = 0
connected = set()

# Mencari jalur minimum (Kruskal)
for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Jaringan Jalan Terpilih:")
for edge in mst:
    print(edge)
print("Total biaya (bobot) minimum =", total_weight)

'''
Jawaban Analisis:
1. Kasus apa yang dipilih?
    Jawab: Kasus 1. Jaringan Jalan Antar Kota.
2. Algoritma apa yang digunakan?
    Jawab: Algoritma Kruskal.
3. Edge mana saja yang dipilih dalam MST?
    Jawab: Bogor - Depok, Depok - Jakarta, dan Depok - Bandung.
4. Berapa total bobot MST?
    Jawab: 9 (Didapat dari 2 + 3 + 4).
5. Mengapa edge tertentu tidak dipilih?
    Jawab: Rute Bogor - Jakarta (5) dan Jakarta - Bandung (6) diabaikan karena harganya lebih mahal. Jika jalan tersebut dibangun,
                akan menciptakan siklus (memutar ke kota yang sebenarnya bisa diakses lewat Depok) sehingga pembiayaannya tidak efisien.
'''