class Queue:
    '''A simple implementation of a queue data structure using a list.'''

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Peek from an empty queue")

    def size(self):
        return len(self.items)
    
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue size: {queue.size()}")
    print(f"Front item: {queue.peek()}")
    print(f"Dequeue item: {queue.dequeue()}")
    print(f"Queue size after dequeue: {queue.size()}")