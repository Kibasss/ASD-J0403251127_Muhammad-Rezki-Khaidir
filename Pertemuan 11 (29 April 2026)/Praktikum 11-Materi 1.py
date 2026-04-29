# ================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Implementasi BFS (Dasar Graph)
# ================================================================

# Membuat dictionary untuk menyimpan struktur graph
# Key = Titik asal, Value = Titik tetangga yang terhubung
graph = {
    'A': ['B', 'C'], # Titik A terhubung ke B dan C
    'B': ['A', 'D'], # Titik B terhubung ke A dan D
    'C': ['A', 'D'], # Titik C terhubung ke A dan D
    'D': ['B', 'C']  # Titik D terhubung ke B dan C
}

# Looping untuk mengambil setiap titik (node) di dalam graph
for node in graph:
    print(node, "->", graph[node]) # Menampilkan titik asal beserta tetangganya ke layar