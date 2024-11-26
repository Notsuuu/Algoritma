#Muhammad Ali Mubaraq_F55123082
#Teknik Informatika C
import random
import time

random.seed(40)
angka = [random.randint(0, 100) for _ in range(50)]

def conquer_method(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left = conquer_method(arr[:mid])
    right = conquer_method(arr[mid:])
    return max(left, right)

start_time = time.perf_counter()
max_conquer = conquer_method(angka)
end_time = time.perf_counter()

print(f"Angka: {angka}")
print(f"Max Ketika Menggunakan Divide & Conquer: {max_conquer}")
print(f"Waktu Yang Dibutuhkan: {end_time - start_time:.6f} Detik")
