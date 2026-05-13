# ===================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 13 - Graph III: Spanning Tree (Kruskal's & Prim's Approaches)
# Implementasi Prim's
# ===================================================================

# Import heapq supaya kita bisa pakai "Priority Queue" (Antrean Prioritas) agar memiliki angka kecil setiap kali kita ambil data (bobot termurah)
import heapq

# 1. Representasi Graph (Peta Jalan)
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    # 2. Catatan titik mana saja yang sudah dikunjungi (biar tidak muter-muter)
    visited = set([start])

    # 3. Daftar calon kabel yang bisa dipilih
    edges = []
    
    # Masukkan semua tetangga dari titik awal ke dalam daftar antrean
    for neighbor, weight in graph[start].items():

        # heapq.heappush akan memastikan bobot terkecil selalu ada di paling atas
        heapq.heappush(edges, (weight, start, neighbor))
        
    # Wadah kosong untuk menyimpan jalan yang dipilih untuk MST
    mst = []
    total_weight = 0
    
    # 4. Selama masih ada kabel yang bisa dicek
    while edges:

        # Ambil kabel dengan bobot paling murah (pop)
        weight, u, v = heapq.heappop(edges)

        # Jika titik tujuan (v) belum pernah dikunjungi, kita sambungkan!
        if v not in visited:
            visited.add(v) # Tandai sudah dikunjungi
            mst.append((u, v, weight)) # Masukkan ke daftar MST
            total_weight += weight # Tambah total biayanya

            # 5. Cek tetangga baru dari titik yang baru saja kita kunjungi tadi
            for neighbor, w in graph[v].items():
                
                # Kalau tetangganya belum dikunjungi, masukkan ke daftar antrean calon kabel
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Jalankan fungsi mulai dari titik 'A'
mst, total = prim(graph, 'A')

# 6. Cetak Hasil
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
    
print("Total bobot =", total)