# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 12 - Graph II: Shortest Path
# Latihan 5: Studi Kasus dengan Program Shortest Path
# ===================================

import heapq

# Representasi graph berbobot menggunakan dictionary berdasarkan data soal: Bogor -> Jakarta (5), Bogor -> Depok (2), dll.
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {} # Bandung jadi tujuan akhir, tidak ada jalan keluar lagi di soal
}

# Fungsi Dijkstra
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph} # Buat catatan jarak, awalnya semua dianggap tak terhingga (inf)
    distances[start] = 0 # Jarak ke titik awal itu sendiri adalah 0
    priority_queue = [(0, start)] # Antrean untuk memprioritaskan pengecekan dari jarak terdekat
    while priority_queue: # Selama masih ada titik yang perlu dicek
        current_distance, current_node = heapq.heappop(priority_queue) # Ambil titik dengan jarak terdekat saat ini
        if current_distance > distances[current_node]: # Abaikan kalau kita menemukan rute yang lebih lambat dari catatan yang sudah ada, karena kita sudah punya rute yang lebih cepat ke node ini. Kita tidak perlu memprosesnya lagi.
            continue
        for neighbor, weight in graph[current_node].items(): # Cek rute ke kota tetangga dari kota saat ini
            distance = current_distance + weight # Hitung total jarak ke tetangga melalui kota saat ini
            if distance < distances[neighbor]: # Kalau nemu jalan yang totalnya lebih cepat, catat dan masukkan antrean untuk dicek lagi nanti
                distances[neighbor] = distance # Perbarui catatan jarak kita dengan jarak baru yang lebih cepat ini
                heapq.heappush(priority_queue, (distance, neighbor)) # Masukkan tetangga ini ke antrean agar jalurnya bisa dicek lagi nanti
                
    return distances

# Input node awal (Penentuan node awal = Bogor)
node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

# Output jarak terpendek dari node awal ke semua node
print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")

'''
Jawaban Analisis:
1. Node awal yang digunakan apa?
    Jawab: Node awal yang digunakan adalah 'Bogor' sesuai dengan data soal yang diberikan. Kita mulai menghitung jarak terpendek dari Bogor ke semua kota lainnya (Jakarta, Depok, Bandung).
2. Node mana yang memiliki jarak paling kecil dari node awal?
    Jawab: Node 'Depok', dengan jarak hanya 2. (Tidak menghitung node Bogor itu sendiri yang jaraknya 0). Jarak ke Depok lebih kecil dibandingkan ke Jakarta (5) dan Bandung (8).
3. Node mana yang memiliki jarak paling besar dari node awal?
    Jawab: Node 'Bandung', dengan jarak terpendeknya adalah 8. Jarak ke Bandung lebih besar dibandingkan ke Depok (2) dan Jakarta (5).
4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
    Jawab: Algoritma mulai "berdiri" di Bogor. Ia melihat ada dua jalan: ke Depok (2) dan ke Jakarta (5). Karena ke Depok lebih dekat, ia fokus cek jalan dari Depok dulu.
                Dari Depok, ternyata ada jalan pintas ke Jakarta dengan jarak 2. Jadi total dari Bogor -> Depok -> Jakarta adalah 4 (lebih cepat dari jalan langsung yang nilainya 5).
                Sistem akan meng-update catatan jarak Jakarta menjadi 4.Lalu untuk ke Bandung, sistem mengecek dari Depok (total 2 + 6 = 8) dan dari Jakarta (total 4 + 7 = 11).
                Karena 8 lebih kecil dari 11, maka sistem memutuskan rute tercepat ke Bandung adalah lewat Depok dengan total jarak 8.
'''