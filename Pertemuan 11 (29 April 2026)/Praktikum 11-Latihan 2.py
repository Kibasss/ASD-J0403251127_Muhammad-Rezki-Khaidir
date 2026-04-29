# ================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Latihan 2: Studi Kasus DFS (Eksplorasi Jalur)
# ================================================================

# Representasi graph (peta jalur eksplorasi)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Fungsi DFS untuk menelusuri rute secara mendalam
def dfs(graph, node, visited):
    visited.add(node) # Tandai titik saat ini sebagai sudah dikunjungi
    print(node, end=" ") # Tampilkan titik yang sedang dikunjungi saat ini

    # Cek setiap tetangga dari titik saat ini
    for neighbor in graph[node]:
        if neighbor not in visited: # Jika tetangga belum dikunjungi, masuk terus ke dalam cabangnya
            dfs(graph, neighbor, visited) # Memanggil dirinya sendiri (rekursif) untuk masuk lebih dalam

# Menyiapkan himpunan kosong untuk mencatat titik yang sudah dilewati
visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited) # Menjalankan fungsi DFS dimulai dari titik 'A'

'''
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
Jawab: Karena DFS (Depth First Search) menggunakan prinsip rekursif atau "masuk terus sampai mentok". Saat menemukan cabang baru, dia tidak akan mengecek cabang lain
di sebelahnya, melainkan langsung masuk terus ke cabang pertama tersebut sampai habis (mencapai titik yang tidak punya tetangga lagi), baru setelah itu mundur untuk 
mengecek cabang yang dilewati tadi.
2. Apa yang terjadi jika urutan neighbor diubah?
Jawab: Jalur eksplorasinya akan berubah. Misalnya tetangga 'A' diubah menjadi ['C', 'B'], maka DFS akan mengeksplorasi seluruh cabang 'C' terlebih dahulu sampai mentok (A -> C -> F),
sebelum berbalik untuk mengeksplorasi cabang 'B'.
3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
Jawab: DFS akan mencetak urutan: A B D E C F (fokus masuk ke kedalaman cabang B sampai habis, baru ke cabang C). BFS akan mencetak urutan: A B C D E F (fokus melebar
untuk mengecek semua tetangga terdekat dulu lapis demi lapis).
'''