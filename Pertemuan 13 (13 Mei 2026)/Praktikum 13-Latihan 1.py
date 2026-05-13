# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 13 - Graph III: Spanning Tree (Kruskal's & Prim's Approaches)
# Latihan 1: Konsep Spanning Tree
# ===================================================================

# Daftar edge graph sesuai gambar modul
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid (semua terhubung, tidak ada cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

'''
Jawaban Analisis:
1. Apa perbedaan graph awal dan spanning tree?
    Jawab: Graph awal masih memiliki jalur yang memutar (cycle) dan edge berlebih. Spanning tree adalah bagian dari graph awal yang menghubungkan
                semua node dengan jumlah edge seminimal mungkin tanpa ada cycle.
2. Mengapa spanning tree tidak boleh memiliki cycle?
    Jawab: Karena cycle berarti ada edge tambahan yang tidak diperlukan untuk menghubungkan node, yang nantinya hanya akan meningkatkan biaya total
                secara tidak efisien dan boros kabel/jalan.
3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
    Jawab: Karena spanning tree membuang edge yang berlebih dan memutar. Aturan pastinya, jika ada N node, maka edge pada spanning tree hanya N-1.
'''