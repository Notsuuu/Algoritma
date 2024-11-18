import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
B = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]

start_time = time.time()
bubblesortA = bubble_sort(A[:])
bubblesortB = bubble_sort(B[:])
bubble_time = time.time() - start_time

start_time = time.time()
quicksortA = quick_sort(A[:])
quicksortB = quick_sort(B[:])
quick_time = time.time() - start_time

print("Array A Sebelum di Sort :", A)
print("Array B Sebelum di Sort :", B)
print("\nHasil Bubble Sort Array A:", bubblesortA)
print("Hasil Bubble Sort Array B:", bubblesortB)
print("\nHasil Quick Sort Array A:", quicksortA)
print("Hasil Quick Sort Array B:", quicksortB)
print("\nWaktu Yang Dibutuhkan Bubble Sort: {:.10f} detik".format(bubble_time))
print("Waktu Yang Dibutuhkan Quick Sort: {:.10f} detik".format(quick_time))

# Jawaban untuk Nomor 2 = Algoritma yang lebih efektif dalam menyelesaikan sorting tipe ascending pada kedua array adalah Quick Sorting, karena cara kerja dari quick sort yang lebih efisien.
# Hal ini disebabkan karena quick sort menggunakan pendekatan "Divide & Conquer" sehingga dapat membantu quick sort nya dalam menyortir array nya dengan lebih cepat jika dibandingkan dengan
# Bubble sort. Sementara itu, bubble sort kurang efisien karena algoritma nya harus memeriksa dan menukar elemen dari array yang ada satu per satu sehingga membuat perhitungan yang dilakukan.
# Tak lupa juga bahwa bubble sort merupakan algoritma qudaratic yang secara teori kinerja nya lebih buruk jikd dibandingkan dengan quick sort yang merupakan algoritma asymtotic.
# oleh karena itulah, quick sort lebih efisien jika dibandingkan dengan bubble sort.