import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import sys # Diperlukan untuk mengatur batas rekursi

# --- PENGATURAN AWAL ---
# Kita set limit rekursi lebih tinggi dari default (biasanya 1000)
# agar tidak error saat N besar.
sys.setrecursionlimit(10**6) 

# 1. Implementasi Linear Search (Iteratif / Looping Biasa)
def linear_search_iterative(katalog, id_buku):
    for i in range(len(katalog)):
        if katalog[i] == id_buku:
            return i
    return -1

# 2. Implementasi Linear Search (Rekursif / Memanggil Diri Sendiri)
def linear_search_recursive(katalog, id_buku, index=0):
    # Basis: Jika index sudah melebihi panjang list, artinya tidak ketemu
    if index >= len(katalog):
        return -1
    
    # Basis: Jika ketemu
    if katalog[index] == id_buku:
        return index
    
    # Rekurens: Cek index berikutnya
    return linear_search_recursive(katalog, id_buku, index + 1)

# Variabel untuk menyimpan data grafik
jumlah_buku_list = []
iterative_times = []
recursive_times = []

# Fungsi update grafik
def update_graph():
    plt.figure(figsize=(10, 6))
    
    # Plot Iteratif (Merah)
    plt.plot(jumlah_buku_list, iterative_times, label='Linear Iterative', marker='o', color='red')
    
    # Plot Rekursif (Biru)
    plt.plot(jumlah_buku_list, recursive_times, label='Linear Recursive', marker='x', color='blue')
    
    plt.title('Perbandingan Waktu: Linear Search Iteratif vs Rekursif')
    plt.xlabel('Jumlah Buku dalam Katalog (N)')
    plt.ylabel('Waktu Eksekusi (detik)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Fungsi cetak tabel
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["N (Jumlah Buku)", "Iterative (s)", "Recursive (s)"]
    for i in range(len(jumlah_buku_list)):
        table.add_row([
            jumlah_buku_list[i], 
            format(iterative_times[i], '.8f'), 
            format(recursive_times[i], '.8f')
        ])
    print(table)

# --- PROGRAM UTAMA ---
print("=== Perbandingan Linear Search: Iteratif vs Rekursif ===")
print("Skenario: Mencari ID Buku di POSISI TERAKHIR (Worst Case)")
print("Catatan: Rekursif mungkin akan error atau crash jika N terlalu besar karena memori stack.")

while True:
    try:
        input_n = input("\nMasukkan jumlah buku (N) atau -1 untuk keluar: ")
        n = int(input_n)
        
        if n == -1:
            print("Program selesai.")
            break
        if n <= 0:
            print("Jumlah buku harus positif!")
            continue

        # Validasi limit rekursi
        # Jika N sangat besar, Python mungkin tetap crash karena Stack Overflow meski limit dinaikkan
        if n > 5000:
            print("WARNING: N > 5000 pada Linear Search Rekursif mungkin menyebabkan lambat/crash.")
        
        # Atur ulang limit rekursi dinamis sesuai N agar aman
        current_limit = sys.getrecursionlimit()
        if n >= current_limit:
            sys.setrecursionlimit(n + 2000)

        # Generate Data
        katalog_buku = list(range(n))
        target_buku = n - 1 # Worst case (di ujung akhir)

        jumlah_buku_list.append(n)

        # 1. Ukur Linear Search ITERATIF
        start_time = time.time()
        linear_search_iterative(katalog_buku, target_buku)
        iter_time = time.time() - start_time
        iterative_times.append(iter_time)

        # 2. Ukur Linear Search REKURSIF
        start_time = time.time()
        linear_search_recursive(katalog_buku, target_buku)
        recur_time = time.time() - start_time
        recursive_times.append(recur_time)

        # Output Hasil
        print(f"Berhasil mencari buku ID {target_buku} dari {n} buku.")
        print_execution_table()
        update_graph()

    except ValueError:
        print("Masukkan angka integer yang valid!")
    except RecursionError:
        print(f"ERROR: Terjadi RecursionError pada N={n}. Memori Stack penuh.")
        # Hapus data terakhir agar grafik tidak error
        jumlah_buku_list.pop()
        iterative_times.pop()
        # Masukkan dummy data untuk recursive agar loop tidak putus total (opsional)