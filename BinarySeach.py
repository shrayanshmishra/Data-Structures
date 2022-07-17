def binarySearch(list, value):
    
    left, right = 0, len(list) - 1

    while left <= right:

        mid = (left + right) // 2

        if list[mid] < value:

            left = mid + 1

        elif list[mid] > value:

            right = mid - 1

        else:

            return mid

    return -1