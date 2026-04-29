# ================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 1: Studi Kasus BFS (Jalur Terdekat Lokasi)
# ================================================================

# Menggunakan fitur deque untuk membuat antrean (queue) yang efisien
from collections import deque

# Representasi graph (peta jalur dari Rumah ke lokasi lain)
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

# Fungsi BFS untuk menelusuri rute
def bfs(graph, start):
    visited = set() # Menyimpan lokasi yang sudah dikunjungi biar nggak bolak-balik
    queue = deque([start]) # Membuat antrean kunjungan lokasi
    visited.add(start) # Tandai lokasi awal (start) sebagai sudah dikunjungi

    # Lakukan pencarian selama masih ada lokasi di antrean
    while queue:
        node = queue.popleft() # Ambil lokasi dari antrean paling depan
        print(node, end=" ") # Tampilkan lokasi yang sedang dikunjungi

        # Cek lokasi tujuan berikutnya (tetangga) dari tempat saat ini
        for neighbor in graph[node]:
            if neighbor not in visited: # Jika lokasinya belum pernah dikunjungi
                visited.add(neighbor) # Tandai sudah dikunjungi dan masukkan ke antrean
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')

'''Pertanyaan Analisis:
1. Node mana yang dikunjungi pertama?
Jawab: Node yang dikunjungi pertama kali adalah 'Rumah', karena titik tersebut dijadikan titik awal penelusuran (start node) saat memanggil fungsi bfs(graph, 'Rumah').
2. Mengapa BFS cocok untuk mencari jalur terdekat?
Jawab: Karena algoritma BFS menyebar secara bertahap atau lapis demi lapis. Lalu, dia akan mengecek semua lokasi yang jaraknya 1 langkah dulu dari titik awal, kemudian baru lanjut
ke lokasi yang jaraknya 2 langkah, dan seterusnya. Jadi, saat dia menemukan tujuan, itu sudah pasti jalur yang paling pendek atau paling dekat.
3. Apa perbedaan urutan BFS jika struktur graph diubah?
Jawab: Jika struktur graph diubah (misalnya urutan daftar tetangga di dalam dictionary ditukar posisinya atau ada jalur baru yang ditambahkan), maka urutan antrean
kunjungan (queue) juga akan berubah. BFS akan selalu membaca dan memproses daftar tetangga sesuai dengan urutan yang dituliskan di dalam graph.
'''