# =========================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# =========================================

def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data)//2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

'''
Soal 1 (Apa yang dimaksud dengan base case?):
Jawab: Base Case adalah suatu kondisi berhenti dalam rekursi yang mencegah fungsi memanggil dirinya sendiri secara terus-terusan.
Soal 2 (Mengapa fungsi memanggil dirinya sendiri?):
Jawab: Fungsi memanggil dirinya sendiri (rekursi) untuk mengimplementasikan strategi divide dan conquer. ini bertujuan untuk memecah list data menjadi sub-list yang lebih kecil secara berulang hingga semua sub-list digabung kembali dalam keadaan terurut.
Soal 3 (Apa tujuan fungsi merge()?):
Jawab: fungsi merge memiliki fungsi yaitu untuk menggabungkan 2 sub-list yang masing-masing sudah terurut menjadi satu list tunggakyang utuh dan terurut secara keseluruhan.
'''