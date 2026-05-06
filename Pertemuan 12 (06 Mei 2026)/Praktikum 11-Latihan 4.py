# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 12 - Graph II: Shortest Path
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ===================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start): # Fungsi utama untuk mencari jalan terpendek menggunakan Algoritma Dijkstra
    distances = {node: float('inf') for node in graph} # Menyimpan jarak minimum. Awalnya semua jarak kita anggap tidak terhingga (inf)
    distances[start] = 0 # Jarak dari titik awal ke titik awal itu sendiri adalah 0
    priority_queue = [(0, start)] # Antrean jadwal kunjungan (Priority queue). Diisi dengan (jarak_sementara, nama_titik)
    while priority_queue: # Lakukan langkah di bawah ini terus selama masih ada titik di dalam antrean
        current_distance, current_node = heapq.heappop(priority_queue) # Ambil titik dari antrean yang jaraknya paling dekat saat ini
        if current_distance > distances[current_node]: # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, maka proses dilewati karena sudah ada jalur yang lebih cepat ke node ini. Kita tidak perlu memprosesnya lagi.
            continue
        for neighbor, weight in graph[current_node].items(): # Periksa semua tetangga yang terhubung langsung dengan titik saat ini
            distance = current_distance + weight # Hitung total jarak: Jarak saat ini + jarak ke tetangga tersebut
            if distance < distances[neighbor]: # Jika ditemukan jarak lebih kecil dari catatan sebelumnya perbarui catatan jarak kita dengan jarak baru yang lebih cepat ini
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) # Masukkan tetangga ini ke antrean agar jalurnya bisa dicek lagi nanti
    return distances

# Menjalankan program: Cari jarak terpendek menggunakan 'graph' dimulai dari titik 'Gerbang'
hasil = dijkstra(graph, 'Gerbang')

# Cetak hasil akhir ke layar
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

'''
Jawaban Analisis:
1. Lokasi mana yang paling dekat dari Gerbang?
    Jawab: Kantin, dengan waktu tempuh hanya 2 menit. Didapat langsung dari bobot edge Gerbang ke Kantin yaitu 2 menit.
2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
    Jawab: Waktu tempuh terpendeknya adalah 7 menit. (Jalurnya: Gerbang -> Kantin -> Lab -> Aula, yaitu 2 + 4 + 1 = 7 menit).
3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
    Jawab: Tidak selalu. Contohnya dari Kantin ke Aula. Kalau kita pakai jalur langsung (Kantin -> Aula) butuh waktu 7 menit.
                Tapi kalau kita mutar sedikit lewat Lab (Kantin -> Lab -> Aula), waktu tempuhnya justru lebih cepat, yaitu 4 + 1 = 5 menit.
4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
    Jawab: Karena perjalanan fisik di dunia nyata (seperti pindah gedung di kampus) pasti selalu memakan waktu, artinya nilainya selalu positif. 
                Tidak ada yang namanya waktu tempuh minus (bobot negatif). Algoritma Dijkstra bekerja paling maksimal, pintar, dan cepat untuk 
                mencari rute terpendek selama semua jarak/waktunya bernilai positif.
'''