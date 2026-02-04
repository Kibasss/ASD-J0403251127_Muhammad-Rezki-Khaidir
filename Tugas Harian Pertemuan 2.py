nama_file = 'stock_barang.txt'

def load_data_barang(nama_file):
    data_barang = {}
    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()
            kode, nama, stok = baris.split(',')

            data_barang[kode] = {
                'nama': nama,
                'stok': int(stok)
            }
    return data_barang

buka_data = load_data_barang(nama_file)
# print(load_data_barang(nama_file))
# print("Jumlah Data Barang:", len(buka_data))

def tampil_data_barang(data_barang):
    print("\n=== Data Barang ===")
    print(f"{'Kode':10} | {'Nama':<12} | {'Stok':>10}")
    print("-" * 50)

    for kode in sorted(data_barang.keys()):
        nama = data_barang[kode]['nama']
        stok = data_barang[kode]['stok']
        print(f"{kode:10} {nama:<12} {stok:>10}")

# tampil_data_barang(buka_data)