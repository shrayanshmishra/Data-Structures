n=int(input())
x=[int(num) for num in input().split(' ',n-1)]
def rev(x):
    y=[x[i] for i in range(-1,-len(x)-1,-1)]
    return y
print(rev(x))