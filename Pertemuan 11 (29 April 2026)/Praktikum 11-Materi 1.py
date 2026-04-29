# ================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Implementasi BFS (Dasar Graph)
# ================================================================

graph ={
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

for node in graph:
    print(node, "->", graph[node])
