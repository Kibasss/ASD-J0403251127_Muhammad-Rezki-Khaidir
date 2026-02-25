# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# ===================================

# ===================================
# Materi Rekursif Faktorial
# Rekursif Case => 3! = 3 x 2 x 1
# Base Case => 0 Berhenti
# ===================================

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
    
print("========= Program Faktorial =========")
print("Hasil Faktorial: ", faktorial(3))