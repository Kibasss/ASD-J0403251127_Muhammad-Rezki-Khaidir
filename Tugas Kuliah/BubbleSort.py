# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# ===================================

# ===================================
# Bubble Sort
# Menjelaskan serta Live Coding terkait Bubble Sort
# ===================================

# Versi Standar atau Umum (Berdasarkan Program No. 3 yang ada pada Modul)
def bubble_sort(data):
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

# Versi Efisien / Short Bubble Sort (Berdasarkan Program No. 4 yang ada pada Modul)
def short_bubble_sort(alist):
    exchange = True
    i = len(alist) - 1
    while i > 0 and exchange:
        exchange = False
        for j in range(i):
            if alist[j] > alist[j+1]:
                exchange = True
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
        i = i-1

angka = [56, 24, 93, 18, 78, 33, 46, 59, 20]
print("Data awal: ", angka)
#bubble_sort(angka)
short_bubble_sort(angka)
print("Setelah diurutkan: ", angka)
