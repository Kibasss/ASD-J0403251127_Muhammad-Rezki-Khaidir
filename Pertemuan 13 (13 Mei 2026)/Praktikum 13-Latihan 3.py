# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 13 - Graph III: Spanning Tree (Kruskal's & Prim's Approaches)
# Latihan 3: Implementasi Sederhana Algoritma Prim's
# ===================================================================

import heapq
from xml.dom.minidom import Node

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)

'''
Jawaban Analisis:
1. Node awal apa yang digunakan?
    Jawab: Node 'A'.
2. Edge mana yang dipilih pertama kali?
    Jawab: Edge A-C (bobot 2), karena itu jalur terpendek yang terhubung langsung dengan node A.
3. Bagaimana Prim menentukan edge berikutnya?
    Jawab: Algoritma mengecek seluruh edge yang terhubung ke node-node yang sudah dikunjungi (dalam hal ini A dan C), lalu memilih bobot paling kecil
                menuju node yang belum pernah dikunjungi.
4. Berapa total bobot MST yang dihasilkan?
    Jawab: 6.
5. Apa perbedaan pendekatan Prim dan Kruskal?
    Jawab: Kruskal memilah dan mengambil edge terkecil secara acak di seluruh bagian secara global, sedangkan Prim membangun rute menjalar secara bertahap 
                seperti akar pohon dari satu node awal ke sekitarnya.
'''