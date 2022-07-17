def hourglassSum(arr):
    y=[]
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            a=0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if (k==(i+1)) and (l==(j) or l== (j+2)):
                        pass
                    else:
                        a+=arr[k][l]
            y.append(a)
    return max(y)

arr=[]
for i in range(6):
    arr.append([int(num) for num in input().split(' ',5)])
print()
print(hourglassSum(arr))