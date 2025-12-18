import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import random

# 1. Implementasi Linear Search (Rak Berantakan)
def linear_search(katalog, id_buku):
    for i in range(len(katalog)):
        if katalog[i] == id_buku:
            return i
    return -1

# 2. Implementasi Binary Search (Rak Terurut)
def binary_search(katalog, id_buku):
    low = 0
    high = len(katalog) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if katalog[mid] == id_buku:
            return mid
        elif katalog[mid] < id_buku:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Variabel untuk menyimpan data grafik
jumlah_buku_list = []
linear_times = []
binary_times = []

# Fungsi update grafik (Sama seperti referensi)
def update_graph():
    plt.figure(figsize=(10, 6))
    plt.plot(jumlah_buku_list, linear_times, label='Linear Search O(N)', marker='o', color='red')
    plt.plot(jumlah_buku_list, binary_times, label='Binary Search O(log N)', marker='x', color='blue')
    plt.title('Perbandingan Waktu Pencarian Buku: Linear vs Binary')
    plt.xlabel('Jumlah Buku dalam Katalog (N)')
    plt.ylabel('Waktu Eksekusi (detik)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Fungsi cetak tabel (Sama seperti referensi)
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Jumlah Buku (N)", "Linear Search (s)", "Binary Search (s)"]
    for i in range(len(jumlah_buku_list)):
        table.add_row([jumlah_buku_list[i], format(linear_times[i], '.8f'), format(binary_times[i], '.8f')])
    print(table)

# --- PROGRAM UTAMA ---
print("=== Simulasi Katalog Perpustakaan Digital ===")
print("Skenario: Mencari ID Buku yang berada di POSISI TERAKHIR (Worst Case)")

while True:
    try:
        input_n = input("Masukkan jumlah buku dalam katalog (atau ketik -1 untuk keluar): ")
        n = int(input_n)
        
        if n == -1:
            print("Program selesai.")
            break
        if n <= 0:
            print("Jumlah buku harus positif!")
            continue

        # Generate Data Buku (ID berurut 0 sampai N-1)
        # Binary search mewajibkan data terurut, Linear search bisa handle keduanya.
        # Agar adil, kita gunakan data yang sama (sudah terurut).
        katalog_buku = list(range(n)) 
        
        # Target pencarian: Buku paling akhir (Worst Case untuk Linear Search)
        target_buku = n - 1 

        jumlah_buku_list.append(n)

        # 1. Ukur Linear Search
        start_time = time.time()
        linear_search(katalog_buku, target_buku)
        linear_time = time.time() - start_time
        linear_times.append(linear_time)

        # 2. Ukur Binary Search
        start_time = time.time()
        binary_search(katalog_buku, target_buku)
        binary_time = time.time() - start_time
        binary_times.append(binary_time)

        # Output Hasil
        print(f"\nBerhasil mencari buku ID {target_buku} dari {n} buku.")
        print_execution_table()
        update_graph()

    except ValueError:
        print("Masukkan angka integer yang valid!")