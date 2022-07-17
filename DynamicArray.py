def dynamicArray(n,queries):
    arr = []
    lastAnswer=0
    answers=[]
    for i in range(n):
        arr.append([])
    for i in range(len(queries)):
        query=queries[i][0]
        x=queries[i][1]
        y=queries[i][2]
        if query == 1:
            idx=((x^lastAnswer)%n)
            arr[idx].append(y)
        if query == 2:
            idx=((x^lastAnswer)%n)
            lastAnswer=arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
    return answers

x=[int(i) for i in input().split(' ',1)]
a=x[0]
b=x[1]
queries=[]
for i in range(b):
    q=[int(num) for num in input().split(' ',b-1)]
    queries.append(q)
for i in dynamicArray(a,queries):
    print(i)