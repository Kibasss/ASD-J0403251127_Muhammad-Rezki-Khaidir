# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 12 - Graph II: Shortest Path
# Latihan 2: Implementasi Dijkstra
# ===================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    distances = {node: float('inf') for node in graph} # Semua jarak awal dibuat tak hingga
    distances[start] = 0 # Jarak dari start ke start adalah 0
    priority_queue = [(0, start)] # Priority queue menyimpan pasangan (jarak, node)
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) # Ambil node dengan jarak terkecil dari antrean
        if current_distance > distances[current_node]:# Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, maka proses dilewati karena sudah ada jalur yang lebih cepat ke node ini. Kita tidak perlu memprosesnya lagi.
            continue
        for neighbor, weight in graph[current_node].items(): # Periksa semua tetangga dari node saat ini
            distance = current_distance + weight # Hitung jarak ke tetangga melalui node saat ini
            if distance < distances[neighbor]: # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
                distances[neighbor] = distance # Perbarui jarak ke tetangga tersebut
                heapq.heappush(priority_queue, (distance, neighbor)) # Masukkan tetangga ke dalam antrean untuk diproses nanti
    return distances

# Menjalankan program: Cari jarak terpendek menggunakan 'graph' dimulai dari titik 'A'
hasil = dijkstra(graph, 'A')

# Cetak hasil akhir ke layar
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

'''
Jawaban Analisis:
1. Berapa jarak terpendek dari A ke B?
    Jawab: Jarak terpendeknya adalah 4. Didapatkan langsung dari bobot edge A ke B yaitu 4.
2. Berapa jarak terpendek dari A ke C?
    Jawab: Jarak terpendeknya adalah 2. Didapatkan langsung dari bobot edge A ke C yaitu 2.
3. Berapa jarak terpendek dari A ke D?
    Jawab: Jarak terpendeknya adalah 3. Diperoleh melalui jalur A -> C -> D, (A ke C = 2) + (C ke D = 1) = (2 + 1 = 3), yang lebih kecil dibandingkan jalur A -> B -> D, (A ke B = 4) + (B ke D = 5) = (4 + 5 = 9).
4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
    Jawab: Karena jika ditotal, bobot jalur A -> C -> D adalah 3 (2 + 1), 
                sedangkan jika melalui B, bobot jalur A -> B -> D adalah 9 (4 + 5). 
                Oleh karena itu, lewat C jauh lebih cepat atau dekat.
5. Apa fungsi priority_queue dalam algoritma Dijkstra?
    Jawab: Fungsinya seperti antrean khusus. Ia akan selalu mengurutkan dan memprioritaskan 
                node/titik yang jarak sementaranya paling kecil untuk diproses lebih dulu. 
6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
    Jawab: Algoritma Dijkstra punya prinsip: "setelah sebuah titik diproses dari antrean, 
                jaraknya sudah pasti yang paling pendek dan tidak akan berubah". Ia berasumsi kalau
                kita jalan terus, jarak pasti akan bertambah. Nah, kalau ada jalan yang nilainya 
                negatif (minus), jarak total justru bisa berkurang di tengah jalan, sehingga 
                merusak perhitungan dan prinsip awal Dijkstra tadi.
                Jadi, Dijkstra tidak bisa menangani graph dengan bobot negatif karena bisa menyebabkan hasil yang salah atau tidak akurat.

'''