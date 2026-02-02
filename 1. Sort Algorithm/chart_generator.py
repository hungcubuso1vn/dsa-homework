import matplotlib.pyplot as plt

# Dữ liệu thời gian chạy (giây)
tests = list(range(10))

quicksort = [
    1.578206, 1.525276, 3.641570, 3.540690, 3.753601,
    3.820885, 3.682530, 3.630978, 3.690016, 3.838820
]

heapsort = [
    4.167984, 4.267859, 5.748998, 6.159670, 5.850394,
    6.203418, 5.812511, 6.494832, 6.085292, 6.452808
]

mergesort = [
    1.925916, 1.958055, 3.532715, 3.648979, 3.565845,
    3.591252, 3.595470, 3.801388, 3.708661, 3.752135
]

plt.figure()
plt.plot(tests, quicksort, marker='o', label="QuickSort")
plt.plot(tests, heapsort, marker='o', label="HeapSort")
plt.plot(tests, mergesort, marker='o', label="MergeSort")

plt.xlabel("Test")
plt.ylabel("Thời gian chạy (giây)")
plt.title("So sánh thời gian chạy các thuật toán sắp xếp")
plt.legend()
plt.grid(True)

# Lưu hình ra file PNG
plt.savefig("chart.png", dpi=300, bbox_inches="tight")
plt.close()
