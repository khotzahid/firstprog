class CircularQueue:
    def __init__(self):
        self.queue= list()
        self.head= 0
        self.tail= 0
        self.maxSize = 8

    def enqueue(self,data):
        if self.size() == self.maxSize-1:
            return("queue full")
        self.queue.append(data)
        self.tail  = (self.tail +1 ) % self.maxSize
        return True

    def dequeue(self):
        if self.size()==0:
            return ("queue empty")
        data = self.queue[self.head]
        self.head = (self.head + 1)% self.maxSize
        return data
    def size(self):
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.maxSize-(self.head-self.tail))
q= CircularQueue()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q.enqueue(5))
print(q.enqueue(6))
print(q.enqueue(7))
print(q.enqueue(8))
print(q.enqueue(9))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())