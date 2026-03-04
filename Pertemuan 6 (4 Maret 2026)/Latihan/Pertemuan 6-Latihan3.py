# =========================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# =========================================

'''Buat Program dengan menggunakan algoritma insertion sort tracing'''
def insertion_sort(data,):
    print(f"Data awal: {data}")
    print("=" * 30)
    
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        pergeseran = 0
        
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            pergeseran += 1
            
        data[j + 1] = key
        print(f"Iterasi i={i} (key={key}): {data} | Pergeseran: {pergeseran}")

    print("=" * 30)
    return data

data_latihan = [5, 2, 4, 6, 1, 3]
hasil_akhir = insertion_sort(data_latihan)

print(f"Data Terurut: {hasil_akhir}")

'''
Soal 1 (Tuliskan isi list setelah iterasi i=1):
Jawab: list data_latihan setelah terjadi iterasi i=1 adalah, data_latihan = [2,5,4,6,1,3]. Karena pada iterasi i=1 hanya terjadi 1 kali penggeseran.
Soal 2 (Tuliskan isi list setelah iterasi i=3):
Jawab: list data_latihan setelah terjadi iterasi i=3 adalah, data_latihan = [2,4,5,6,1,3]. Karena pada iterasi i=3 tidak ada penggeseran karena nilai 6 lebih besar dari 5.
Soal 3 (Berapa kali penggeseran terjadi pada iterasi i=4):
Jawab: pada iterasi i=4 terjadi 4 kali penggesaran karena nilai key yaitu 1 lebih kecil dari 6, 5, 4, dan 2.
'''