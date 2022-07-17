from multiprocessing import Queue

que = Queue()

que.put("Apple")
que.put("Mango")
que.put("Banana")

print(que)

print(que.get())

print(que.get())

print(que.get())