# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 12 - Graph II: Shortest Path
# Implementasi Algoritma Bellman-Ford
# ===================================

graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

def bellman_ford(graph, start): # Fungsi utama untuk mencari jalan terpendek dengan metode Bellman-Ford
    # 1. Persiapan Awal
    distances = {node: float('inf') for node in graph} # Buat buku catatan jarak. Awalnya semua jarak kita anggap tidak terhingga (inf)
    distances[start] = 0 # Jarak dari titik awal ke titik awal itu sendiri sudah pasti 0
    # 2. Proses Relaksasi
    for _ in range(len(graph) - 1): # Kita ulangi proses pencarian ini sebanyak (jumlah titik/kota dikurang 1) kali.
        for node in graph: # Cek setiap titik/kota yang ada di dalam peta kita
            for neighbor, weight in graph[node].items(): # Cek semua titik tetangga dari kota tersebut beserta jarak jalannya (weight)
                if distances[node] + weight < distances[neighbor]: # Jika jarak ke titik saat ini + jarak jalan ke tetangga lebih pendek dari catatan sebelumnya maka perbarui catatan jaraknya dengan jalur yang lebih cepat ini
                    distances[neighbor] = distances[node] + weight # Perbarui catatan jaraknya dengan jalur yang lebih cepat ini
    # 3. CEK SIKLUS NEGATIF (Jebakan jalur muter-muter yang nilainya makin minus)
    for node in graph: # Ini untuk memastikan hitungan kita valid dan tidak ada rute error.
        for neighbor, weight in graph[node].items(): # Cek semua titik tetangga dari kota tersebut beserta jarak jalannya (weight)
            if distances[node] + weight < distances[neighbor]: # Kalau setelah diulang-ulang tadi ternyata masih ketemu jalan yang lebih pendek lagi, berarti ada rute error (siklus negatif) di dalam peta. Hitungan jadi tidak valid.
                print("Peringatan: Ada rute muter-muter bernilai negatif di dalam Graph!") # Berarti ada jalur error (siklus negatif) di dalam peta. Hitungan jadi tidak valid.
                return None # Hentikan program dan kembalikan nilai kosong karena hitungan tidak valid
    # Jika aman dari rute error, kembalikan buku catatan hasil jarak terpendek
    return distances

# Menjalankan program: Cari jarak terpendek menggunakan 'graph' dimulai dari titik 'A'
hasil = bellman_ford(graph, 'A')

# Jika hasilnya ada (bukan None), maka cetak hasil akhirnya ke layar
if hasil:
    print(hasil)