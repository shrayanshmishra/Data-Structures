# working with queue.Queue class

from queue import Queue

que = Queue()

que.put('Apple')
que.put('Mango')
que.put('Papaya')

print(que)

print(que.get())

print(que.get())

print(que.get())

print(que.get_nowait())

print(que.get())