# =========================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# =========================================

def insertion_sort (data):
    print("Data Awal : ", data)
    print("="*50)

    for i in range(1,len(data)):

        key = data[i]
        j = i -1

        while j >= 0 and data [j] > key:
            data [j+1] = data [j]
            j -= 1

            data [j+1] = key

            print("Setelah Disisipkan: ", data)
            print("="*50)
        return data
    
angka = [7,8,5,2,4,6]
print("Hasil Sorting :", insertion_sort(angka))