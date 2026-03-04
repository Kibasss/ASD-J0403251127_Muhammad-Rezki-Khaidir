# =========================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# =========================================

def insertion_data(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i -1
        while j >= 0 and data[j] > key:
            data[j +1] = data [j]
            j -= 1
        data[j + 1] = key
    return data

'''
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
Jawab: Karena indeks 0 atau elemen pertama itu kita anggap posisinya sudah benar dan juga itu untuk jadi pembanding dengan elemen-elemen selanjutnya yang ada di sebelah kiri.
2. Apa fungsi Variabel key?
Jawab: Variabel key berfungsi sebagai tempat sementara untuk nyimpan data yang mau dipindahin sampai data yang dipindahin ini diletakkan diurutan yang sesuai.
3. Mengapa digunakan while, bukan for?
Jawab: Karena saat pengeseran ke kiri itu jumlahnya tidak selalu sama. Jadi, penggunaan while lebih efisien karena akan langsung berhenti ketika sudah mencapai ujung kiri urutan atau menemukan nilai yang lebih kecil dari key.
4. Operasi apa yang terjadi di dalam while?
Jawab: Operasi yang terjadi di dalam while yaitu operasi penggeseran ke kanan. Jika angka indeks 2 lebih kecil dari key (indeks 3), maka angka tersebut akan dipindahkan ke posisi kanannya. Setelah itu, posisi indeks j dikurangi satu agar pengecekan tetap dilakukan hingga ditemukan posisi yang cocok untuk key.
'''