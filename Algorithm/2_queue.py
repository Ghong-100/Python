'''
import queue
import random

# 일반적인 FIFO 큐
data_queue = queue.Queue()

for i in range(5):
    num = random.randint(1,10)
    print(num)
    data_queue.put(num)

print("---------------------")
for i in range(data_queue.qsize()):
    print(data_queue.get())

# LIFO 큐
data_queue = queue.LifoQueue()

for i in range(5):
    num = random.randint(1,10)
    print(num)
    data_queue.put(num)

print("---------------------")
for i in range(data_queue.qsize()):
    print(data_queue.get())

# Priority 큐
data_queue = queue.PriorityQueue()

for i in range(5):
    num = random.randint(1,10)
    print(num)
    data_queue.put(i,num)

print("---------------------")
for i in range(data_queue.qsize()):
    print(data_queue.get())

'''

class myQueue:
    queue_list = []
    def __init__(self):
        self.queue_list = []
    
    def enqueue(self, data):
        self.queue_list.append(int(data))
    
    def dequeue(self):
        data = self.queue_list[0]
        del self.queue_list[0]
        return data

    
qq = myQueue()

for i in range(5):
    qq.enqueue(i)

for i in range(len(qq.queue_list)):
    print(qq.dequeue())