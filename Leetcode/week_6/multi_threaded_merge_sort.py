import threading


def merge_sort(arr):

    def _merge(arr1, arr2):
        i, j = 0, 0
        l1, l2 = len(arr1), len(arr2)
        arr_sorted = [0] * (l1 + l2)
        idx = 0
        while i < l1 and j < l2:
            if arr1[i] < arr2[j]:
                arr_sorted[idx] = arr1[i]
                i += 1
            else:
                arr_sorted[idx] = arr2[j]
                j += 1
            idx += 1

        while i < l1:
            arr_sorted[idx] = arr1[i]
            i += 1
            idx += 1
        while j < l2:
            arr_sorted[idx] = arr2[j]
            j += 1
            idx += 1
        return arr_sorted

    def _recursive_sort(arr):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left_arr = _recursive_sort(arr[:mid])
        right_arr = _recursive_sort(arr[mid:])
        return _merge(left_arr, right_arr)

    return _recursive_sort(arr)


def merge_sort_inplace(arr):

    def _merge(arr, start, mid, end):
        start2 = mid + 1

        while start <= mid and start2 <= end:

            if arr[start] <= arr[start2]:  # elem in right place
                start += 1
            else:
                orig_start2 = arr[start2]
                idx = start2
                # shift all elements between start and start2
                # to the right by one place
                while idx != start:
                    arr[idx] = arr[idx - 1]
                    idx -= 1
                arr[start] = orig_start2

                start += 1
                mid += 1
                start2 += 1

    def _recursive_sort(arr, left, right):
        if left < right:
            mid = left + ((right - left) // 2)
            _recursive_sort(arr, left, mid)
            _recursive_sort(arr, mid + 1, right)
            _merge(arr, left, mid, right)

    _recursive_sort(arr, 0, len(arr) - 1)


def _merge(arr, start, mid, end):
    start2 = mid + 1

    while start <= mid and start2 <= end:

        if arr[start] <= arr[start2]:  # elem in right place
            start += 1
        else:
            orig_start2 = arr[start2]
            idx = start2
            # shift all elements to the right by one place
            while idx != start:
                arr[idx] = arr[idx - 1]
                idx -= 1
            arr[start] = orig_start2

            start += 1
            mid += 1
            start2 += 1


def _recursive_sort(arr, left, right):
    if left < right:
        mid = left + ((right - left) // 2)
        _recursive_sort(arr, left, mid)
        _recursive_sort(arr, mid + 1, right)
        _merge(arr, left, mid, right)

# _recursive_sort(arr, 0, len(arr) - 1)


if __name__ == "__main__":

    ar = [2, 4, 1, 2, 4, 5, 8, 2, 351, 2, 0]

    thread1 = threading.Thread(
        target=_recursive_sort, args=(ar, 0, len(ar) // 2),)
    thread2 = threading.Thread(
        target=_recursive_sort, args=(ar, (len(ar) // 2) + 1, len(ar) - 1,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    _merge(ar, 0, len(ar) // 2, len(ar) - 1)
    print(ar)
