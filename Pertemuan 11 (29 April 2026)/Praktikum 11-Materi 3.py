# ================================================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Implementasi DFS
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

def dfs(graph, node, visited):
    #Fungsi untuk melakukan penelusuran graph menggunakan DFS
    #graph : dictionary yang mentimpan graph
    #node: menyimpan node yang sedang dikunjungi
    #Visited : Menyimpan node yang sudah dikunjungi

    #Tandai node saat ini udah dikunjungi
    visited.add(node)
    

    #Tampilkan node yang sedang ddikunjungi
    print(node, end=" ")
    for neighbor in graph[node]:
        #Jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

#Set visited
visited=set()

#Menjalankan data 
dfs(graph,"A",visited)