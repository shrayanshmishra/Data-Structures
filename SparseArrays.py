def matchingStrings(strings, queries):
    for i in queries:
        print(strings.count(i))

n=int(input())
strings=[]
for i in range(n):
    x=input()
    strings.append(x)
q=int(input())
queries=[]
for i in range(q):
    y=input()
    queries.append(y)
matchingStrings(strings,queries)