# ================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Implementasi BFS 
# ================================================================

from collections import deque

#representasi graph
graph ={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
        
}

def bfs(graph,start):
    #Fungsi untuk melakukan penelusuran graph dengan bfs
    # graph : dictionary yang menyimpan struktur dari graph
    # start : node awal penelusuran
    
    #Queue digunakan untuk menyimpan node yang akan dipreoses / dibaca
    queue = deque()

    #Variabel yang digunakan untuk menyimpan node yang suda diproses/sudah dikunjungi
    visited = set()

    #Masukkan node awal ke queue
    queue.append(start)

    #Tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    while queue:
        node = queue.popleft()

        #Tampilkan node yang sedang dikunjungi
        print(node, end=' ')

        #Periksa semua tetangga dari node yang diambil:
        for neighbor in graph[node]:
            #Jika tetangga belum dikunjungi
            if neighbor not in visited:
                #Tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                #Masukkan tetangga ke queue untuk diproses
                queue.append(neighbor)

#Bfs dari node A
bfs(graph,'A')
