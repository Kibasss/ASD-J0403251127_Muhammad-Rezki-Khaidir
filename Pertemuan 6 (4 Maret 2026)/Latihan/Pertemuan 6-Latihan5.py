# =========================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# =========================================

'''Soal No 1(Lengkapi kondisi agar menjadi ascending):'''
def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

'''
Soal No 2 (Jelaskan fungsi result.extend()):
Jawab: Fungsi result.extend() bertujuan untuk menambahkan seluruh elemen yang tersisa dari list left atau right ke dalam list result. Hal ini terjadi setelah proses pembandingan pada proses while selesai, berfungsi untuk memastikan tidak ada elemen yang tertinggal.
'''