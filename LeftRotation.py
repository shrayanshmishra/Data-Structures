def rotateLeft(n,d,arr):
    if d > 0 and d < n:
        x = arr[ :d]
        y = arr[d: ]
        arr.clear()
        arr.extend(y)
        arr.extend(x)
        return arr
    else:
        d %= n
        x = arr[ :d]
        y = arr[d: ]
        arr.clear()
        arr.extend(x)
        arr.extend(y)
        return arr
n,d=[int(i) for i in input().split(' ',1)]
arr=[int(i) for i in input().split(' ',n-1)]
if d == 0 or d == n:
    print(arr)
else:
    print(rotateLeft(n,d,arr))