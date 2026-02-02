import time
import numpy as np

from quicksort import quicksort
from heapsort import heapsort
from mergesort import mergesort


print("TEST | QuickSort | HeapSort | MergeSort | NumPy Sort")
print("-" * 55)

for i in range(10):
    with open(f"testcases/test{i}.inp") as f:
        data = list(map(float, f.readline().split()))

    t0 = time.perf_counter()
    quicksort(data.copy())
    t_qs = time.perf_counter() - t0

    t0 = time.perf_counter()
    heapsort(data.copy())
    t_hs = time.perf_counter() - t0

    t0 = time.perf_counter()
    mergesort(data.copy())
    t_ms = time.perf_counter() - t0

    arr = np.array(data)
    t0 = time.perf_counter()
    np.sort(arr)
    t_np = time.perf_counter() - t0

    print(
        f"{i:>4} | "
        f"{t_qs:.6f} | "
        f"{t_hs:.6f} | "
        f"{t_ms:.6f} | "
        f"{t_np:.6f}"
    )
