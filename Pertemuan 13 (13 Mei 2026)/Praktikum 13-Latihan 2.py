# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 13 - Graph III: Spanning Tree (Kruskal's & Prim's Approaches)
# Latihan 2: Implementasi Sederhana Algoritma Kruskal's
# ===================================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()
mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

'''
Jawaban Analisis:
1. Edge mana yang dipilih pertama kali?
    Jawab: Edge C-D dengan bobot 1, karena merupakan bobot paling kecil dari seluruh graph.
2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
    Jawab: Karena prinsip Kruskal adalah mencari total biaya terminimum secara global, sehingga ia memprioritaskan mengambil yang termurah terlebih dahulu.
3. Berapa total bobot MST yang dihasilkan?
    Jawab: 6 (didapat dari 1 + 2 + 3).
4. Mengapa edge tertentu tidak dipilih?
    Jawab: Edge seperti A-B (bobot 4) dan A-D (bobot 5) diabaikan karena node tersebut sudah saling terhubung oleh rute lain. Jika tetap dimasukkan, akan membentuk cycle (jalur berputar).
'''