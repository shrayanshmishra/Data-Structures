class Queue:

    def __init__(self):

        self.queue = list()

    # to add an element

    def add_element(self, val):

        if val not in self.queue:

            self.queue.insert(0, val)

            return True

        return False

    # to remove an element

    def remove_element(self):

        if len(self.queue) > 0:

            return self.queue.pop()

        return "Queue is empty"

    # to get size of queue

    def size(self):

        return len(self.queue)

TheQueue = Queue()

TheQueue.add_element("Apple")
TheQueue.add_element("Mango")
TheQueue.add_element("Guava")
TheQueue.add_element("Papaya")

print("The length of Queue:", TheQueue.size())

print(TheQueue.queue)

print(TheQueue.remove_element())

print(TheQueue.remove_element())

# sorting the queue

import queue

q = queue.Queue()

q.put(14)
q.put(27)
q.put(11)
q.put(4)
q.put(1)

# bubble sort

n = q.qsize()

for i in range(n):

    # remove the element

    x = q.get()

    for j in range(n - 1):

        # remove the element

        y = q.get()

        if x > y:

            # put the smaller element at the beginning of the queue

            q.put(y)

        else:

            # the smaller one is put at the start of the queue

            q.put(x)

            x = y # the greater element is replaced by x and check again

    q.put(x)

while q.empty() == False:

    print(q.queue[0], end = " ")
    q.get()