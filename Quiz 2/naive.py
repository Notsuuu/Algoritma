#Muhammad Ali Mubaraq_F55123082
#Teknik Informatika C
mport random
import time

random.seed(40)
angka = [random.randint(0, 100) for _ in range(50)]

def naive_algorithm(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

start_time = time.perf_counter()
max_naive = naive_algorithm(angka)
end_time = time.perf_counter()

print(f"Angka: {angka}")
print(f"Max Ketika Menggunakan Naive Algorithm: {max_naive}")
print(f"Waktu Yang Dibutuhkan: {end_time - start_time:.6f} detik")
