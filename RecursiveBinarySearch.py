def recBinarySearch(list, low, high, n):

    if low <= high:

        mid = (low + high) // 2

        if list[mid] == n:

            return mid

        elif list[mid] < n:

            recBinarySearch(list, mid + 1, high)

        else:

            recBinarySearch(list, low, mid - 1)

    return -1