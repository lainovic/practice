from hashmap import HashMap


def most_frequent(arr):
    res = None
    max_count = 0
    count = HashMap()
    for n in arr:
        count[n] = count.get(n, 0) + 1
        if count[n] > max_count:
            max_count = count[n]
            res = n
    return res


def count_pairs_with_diff(arr, k):
    hm = HashMap()
    res = 0
    log_output = []
    for i, n in enumerate(arr):
        if n - k in hm:
            log_output.append(f"({n}, {n - k})")
            res += 1
        if n + k in hm:
            log_output.append(f"({n}, {n + k})")
            res += 1
        hm[n] = i
    print("[DEBUG]: " + ", ".join(log_output))
    return res


def two_sum(arr, target):
    res = []
    hm = HashMap()
    visited = []
    for i, n in enumerate(arr):
        needed = target - n
        if needed in hm and hm[needed] not in visited:
            sln = [hm[needed], i]
            res.append(sln)
            visited.extend(sln)
        hm[n] = i
    return res


if __name__ == "__main__":
    print(
        f"most_frequent([1, 2, 2, 3, 3, 3, 4]): {most_frequent([1, 2, 2, 3, 3, 3, 4])}")
    print(
        f"count_pairs_with_diff([1, 7, 5, 9, 2, 12, 3], 2): {count_pairs_with_diff([1, 7, 5, 9, 2, 12, 3], 2)}")
    print(
        f"two_sum([2, 7, 5, 11, 15, 4, 2], 9): {two_sum([2, 7, 5, 11, 15, 4, 2], 9)}")
