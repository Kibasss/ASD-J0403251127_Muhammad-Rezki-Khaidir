# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 12 - Graph II: Shortest Path
# Implementasi Algoritma Dijkstra
# ===================================

import heapq # Alat untuk membuat antrean yang selalu memprioritaskan nilai (jarak) terkecil

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {} # Kosong karena tidak ada jalan keluar lagi dari titik D
}


def dijkstra(graph, start): # Fungsi utama untuk mencari jalan terpendek menggunakan Algoritma Dijkstra
    distances = {node: float('inf') for node in graph} # Menyimpan jarak minimum. Awalnya semua jarak kita anggap tidak terhingga (inf)
    distances[start] = 0 # Jarak dari titik awal ke titik awal itu sendiri adalah 0
    pq = [(0, start)] # Antrean jadwal kunjungan (Priority queue). Diisi dengan (jarak_sementara, nama_titik)
    while pq: # Lakukan langkah di bawah ini terus selama masih ada titik di dalam antrean
        current_distance, current_node = heapq.heappop(pq) # Ambil titik dari antrean yang jaraknya paling dekat saat ini
        for neighbor, weight in graph[current_node].items(): # Periksa semua tetangga yang terhubung langsung dengan titik saat ini
            distance = current_distance + weight # Hitung total jarak: Jarak saat ini + jarak ke tetangga tersebut
            if distance < distances[neighbor]: # Jika ditemukan jarak lebih kecil dari catatan sebelumnya
                distances[neighbor] = distance # Perbarui catatan jarak kita dengan jarak baru yang lebih cepat ini
                heapq.heappush(pq, (distance, neighbor)) # Masukkan tetangga ini ke antrean agar jalurnya bisa dicek lagi nanti
    return distances # Kembalikan buku catatan hasil akhir yang berisi jarak terpendek ke semua titik

# Hasil akhir: Cari jarak terpendek menggunakan 'graph' dimulai dari titik 'A'
hasil = dijkstra(graph, 'A')
print(hasil)