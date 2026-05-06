# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 12 - Graph II: Shortest Path
# Latihan 3: Implementasi Bellman-Ford
# ===================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    distances = {node: float('inf') for node in graph} # Semua jarak awal dibuat tak hingga
    distances[start] = 0 # Jarak dari start ke start adalah 0
    for _ in range(len(graph) - 1):  # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
        for node in graph: # Periksa semua edge dalam graph
            for neighbor, weight in graph[node].items(): # Cek semua tetangga dari node saat ini
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: # Jika jarak ke node saat ini sudah diketahui, dan ditemukan jarak yang lebih kecil ke neighbor, maka lakukan update jarak ke neighbor tersebut
                    distances[neighbor] = distances[node] + weight
    return distances

# Menjalankan program: Cari jarak terpendek menggunakan 'graph' dimulai dari titik 'A'
hasil = bellman_ford(graph, 'A')

# Cetak hasil akhir ke layar
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

'''
Jawaban Analisis:
1. Berapa bobot langsung dari A ke B?
    Jawab: Bobot langsungnya adalah 5. Didapat langsung dari bobot edge A ke B yaitu 5.
2. Berapa total bobot jalur A -> C -> B?
    Jawab: Total bobotnya adalah 2. (Didapat dari A ke C yaitu 4, ditambah C ke B yaitu -2. Jadi 4 + (-2) = 2).
3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
    Jawab: Jalur A -> C -> B, karena total bobotnya (2) lebih kecil daripada lewat jalur langsung A -> B (5).
4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
    Jawab: Karena Bellman-Ford mengecek dan memperbarui (relaksasi) semua jalur berulang-ulang kali. Ia tidak langsung mengunci jarak tercepat di awal.
                Jadi, kalau di tengah jalan ia menemukan ada jalur dengan nilai negatif yang bikin total jarak jadi lebih kecil, ia akan memperbarui hitungannya.
5. Apa yang dimaksud dengan proses relaksasi edge?
    Jawab: Relaksasi edge adalah proses mengecek dan memperbarui catatan jarak. Kalau kita nemu rute baru menuju suatu titik yang ternyata lebih cepat
                (lebih kecil nilainya) daripada rute lama yang udah dicatat, maka catatannya di-update pakai rute yang baru ini.
6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
    Jawab:      - Dijkstra: Kerjanya lebih cepat karena langsung fokus milih jalan terpendek dari antrean, tapi kelemahannya dia bisa salah hitung (error)
                                     kalau ada jalan yang nilainya minus/negatif.
                    - Bellman-Ford: Kerjanya lebih lambat karena harus ngecek semua jalan berulang kali, tapi kelebihannya dia sangat kebal dan bisa menghitung
                                     dengan benar walaupun ada jalan yang nilainya minus/negatif.
'''