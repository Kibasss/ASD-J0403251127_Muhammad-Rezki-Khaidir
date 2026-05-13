# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 13 - Graph III: Spanning Tree (Kruskal's & Prim's Approaches)
# Latihan 4: Studi Kasus Jaringan Kabel Antar Gedung
# ===================================================================
# Menggunakan Algoritma Kruskal untuk penyelesaian

# Representasi edge: (Biaya Pemasangan, Gedung 1, Gedung 2)
edges = [
    (1, 'GedungC', 'GedungD'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (4, 'GedungA', 'GedungB'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan berdasarkan biaya termurah
edges.sort()
mst = []
total_weight = 0
connected = set()

# Implementasi Kruskal
for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Kabel yang dipasang antar Gedung (MST):")
for edge in mst:
    print(edge)
print("Total biaya minimum =", total_weight)

'''
Jawaban Analisis:
1. Algoritma apa yang digunakan?
    Jawab: Algoritma Kruskal.
2. Edge mana saja yang dipilih?
    Jawab: Gedung C - Gedung D (1), Gedung A - Gedung C (2), dan Gedung B - Gedung D (3).
3. Berapa total biaya minimum?
    Jawab: 6.
4. Mengapa MST cocok digunakan pada kasus ini?
    Jawab: Karena tujuan pada kasus ini adalah mengkoneksikan seluruh gedung ke dalam satu jaringan internet dengan meminimalkan biaya pemasangan kabel
                dan menghindari jalur kabel yang memutar tanpa guna.
'''