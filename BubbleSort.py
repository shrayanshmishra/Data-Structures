def bubbleSort(list):

    n = len(list)

    for i in range(n - 1):

        for j in range(n):

            if list[i] > list[j]:

                temp = list[i]
                list[i] = list[j]
                list[j] = temp

    return list