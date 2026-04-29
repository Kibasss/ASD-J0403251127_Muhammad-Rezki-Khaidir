# ================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Implementasi DFS
# ================================================================

# Menggunakan fitur deque untuk membuat antrean (queue) yang efisien
from collections import deque

# Representasi graph (peta jaringan) menggunakan dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

# Fungsi untuk menelusuri graph dengan metode DFS (Depth First Search)
def dfs(graph, node, visited):
    visited.add(node) # Tandai titik saat ini sebagai sudah dikunjungi
    print(node, end=" ") # Tampilkan titik yang sedang diproses ke layar
    # Cek semua tetangga dari titik saat ini
    for neighbor in graph[node]:
        if neighbor not in visited: # Jika tetangganya belum pernah dikunjungi
            dfs(graph, neighbor, visited) # Panggil kembali fungsi DFS untuk mengecek tetangga tersebut (Rekursif)

# Membuat tempat kosong untuk mencatat titik-titik yang sudah dikunjungi
visited = set()

# Menjalankan fungsi DFS dimulai dari titik 'A'
dfs(graph, "A", visited)