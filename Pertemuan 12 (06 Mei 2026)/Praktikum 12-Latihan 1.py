# ===================================
# Nama: Muhammad Rezki Khaidir
# NIM: J0403251127
# Kelas: TPL PB/1
# Praktikum 12 - Graph II: Shortest Path
# Latihan No 1: Weighted Graph dan Perhitungan Jalur
# ===================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

'''
Jawaban Analisis:
1. Berapa tota bobot jalur A -> B -> D?
    Jawab: Total bobotnya adalah 9. (A ke B yaitu 4, ditambah B ke D yaitu 5, 4+5 = 9).
2. Berapa tota bobot jalur A -> C -> D?
    Jawab: Total bobotnya adalah 3. (A ke C yaitu 2, ditambah C ke D yaitu 1, 2+1 = 3).
3. Jalur mana yang dilpilih sebagai jalur terpendek?
    Jawab: Jalur A -> C -> D. Karena total bobotnya (3) lebih kecil dibandingkan jalur A -> B -> D (9), 3 < 9.
4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
    Jawab: Karena dalam weighted graph (graf berbobot), setiap jalan penghubung (edge) memiliki nilai atau jarak (bobot) yang berbeda-beda.
                Bisa saja sebuah rute hanya melewati sedikit jalan, tapi jarak tempuhnya sangat jauh (bobot besar). Sebaliknya, rute lain mungkin melewati
                banyak belokan (edge banyak), tapi setiap jalannya sangat pendek (bobot kecil), sehingga total waktu/jaraknya justru lebih cepat.
                Jadi, dalam kasus graf berbobot, kita harus mempertimbangkan total bobot (jarak) dari seluruh rute, bukan hanya jumlah jalan yang dilalui.
'''