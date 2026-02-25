# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# ===================================

# ===================================
# Materi Rekursif Call Stack
# Tracing Bilangan (Masuk-Keluar)
# Input 3
# 3-2-1 | 1-2-3
# ===================================

def hitung(n):
    if n == 0:
        print("Selesai.")
        return
    
    print("Masuk: ", n)
    hitung(n-1)
    print("keluar: ", n)

print("========= Program Hitung =========")
hitung(3)