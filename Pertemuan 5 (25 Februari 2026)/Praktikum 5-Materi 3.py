# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# ===================================

# ===================================
# Menjumlahkan Elemen List
# ===================================

def jumlah_list(data, index=0):
    if index == len(data):
        return 0
    return data[index] + jumlah_list(data, index+1)

print("=========Program Menjumlahkan List =========")
print(jumlah_list([2,4,5]))