# ================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Implementasi BFS 
# ================================================================

# Menggunakan fitur deque untuk membuat antrean (queue) yang efisien
from collections import deque

# Representasi graph menggunakan dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

# Fungsi untuk menelusuri graph dengan metode BFS
def bfs(graph, start):
    queue = deque() # Membuat antrean kosong untuk titik yang akan diproses
    visited = set() # Menyimpan titik-titik yang sudah dikunjungi agar tidak dicek ulang
    queue.append(start) # Masukkan titik awal ke antrean dan tandai sudah dikunjungi
    visited.add(start)

    # Lakukan perulangan selama antrean masih ada isinya
    while queue:
        node = queue.popleft()# Ambil titik paling depan dari antrean
        print(node, end=' ')# Tampilkan titik yang sedang diproses ke layar
        # Cek semua tetangga dari titik yang sedang diproses
        for neighbor in graph[node]:
            if neighbor not in visited: # Jika tetangganya belum dikunjungi
                visited.add(neighbor) # Tandai sudah dikunjungi
                queue.append(neighbor) # Masukkan tetangga tersebut ke antrean antrean untuk diproses nanti

# Menjalankan fungsi BFS dimulai dari titik 'A'
bfs(graph, 'A')