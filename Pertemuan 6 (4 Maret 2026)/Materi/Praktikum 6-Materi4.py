# =========================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# =========================================

# =========================================
# Merge Sort (Ascending)
# =========================================

def merge_sort(data,depth=0):
    indent = " " * depth
    print(f"{indent}mergesort({data})")

    if len(data) <= 1:
        return data
    
    mid = len(data)//2
    left = data[:mid]
    right = data[mid:]

    print(f"{indent}divide -> left = {left} | right = {right}")

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merge -> {left_sorted} + {right_sorted} = {merged}")

    return merged

    return merged(left_sorted, right_sorted)

def merge(left,right):
    result = []
    i = 0
    j = 0

    while i < len (left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

angka = [13, 7, 28, 5, 19, 36, 4]

print("Hasil Sorting :", merge_sort(angka))