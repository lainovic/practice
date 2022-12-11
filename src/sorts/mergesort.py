import math


def mergesort_top_bottom(arr):
    def mergesort(lo, hi):
        if hi - lo <= 1:
            return
        m = math.ceil((lo + hi) / 2)
        mergesort(lo, m)
        mergesort(m, hi)
        merge(lo, m, hi)

    def merge(lo, m, hi):
        i, j, k = lo, m, 0
        out = [0] * (hi - lo)
        while i < m and j < hi:
            if arr[i] <= arr[j]:
                out[k] = arr[i]
                i += 1
            else:
                out[k] = arr[j]
                j += 1
            k += 1
        while i < m:
            out[k] = arr[i]
            i += 1
            k += 1
        while j < hi:
            out[k] = arr[j]
            j += 1
            k += 1
        for i in range(lo, hi):
            arr[i] = out[i - lo]

    mergesort(0, len(arr))
    return arr


def mergesort_bottom_up(arr):
    def merge(lo, m, hi):
        i, j = lo, m
        out = [0] * (hi - lo)
        for k in range(len(out)):
            if i < m and (j >= hi or arr[i] <= arr[j]):
                out[k] = arr[i]
                i += 1
            else:
                out[k] = arr[j]
                j += 1
        for i in range(len(out)):
            arr[lo + i] = out[i]

    p = 1
    while p <= len(arr):
        i = 0
        while i < len(arr):
            lo = i
            hi = min(i + 2*p, len(arr))
            m = math.ceil((lo + hi) / 2)
            merge(lo, m, hi)
            i += 2*p
        p *= 2
    return arr
