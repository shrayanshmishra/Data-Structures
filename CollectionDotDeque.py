# working with collection.deque class

from collections import deque

que = deque()

que.append('Apple')
que.append('Mango')
que.append('Banana')

print(que)
deque(['Apple ', 'Mango', 'Banana'])

print(que.popleft())

print(que.popleft())

print(que.popleft())

que.popleft()