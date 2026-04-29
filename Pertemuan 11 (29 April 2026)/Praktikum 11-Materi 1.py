# ================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Implementasi BFS (Dasar Graph)
# ================================================================

graph = {
    'A': ['B', 'C'], # Titik A terhubung ke B dan C
    'B': ['A', 'D'], # Titik B terhubung ke A dan D
    'C': ['A', 'D'], # Titik C terhubung ke A dan D
    'D': ['B', 'C']  # Titik D terhubung ke B dan C
}

for node in graph:
    print(node, "->", graph[node])