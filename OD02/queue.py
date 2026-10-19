from collections import deque

class Queue:                       
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Удаление из пустой очереди")
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Получение из пустой очереди")
        return self.items[0]

    def __bool__(self):
        return bool(self.items)

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"Очередь({list(self.items)!r})"

    @classmethod
    def from_list(cls, items):
        queue = cls()
        for i in items:
            queue.enqueue(i)
        return queue


class QueuePrinter: 
    @staticmethod
    def to_text(queue: Queue) -> str:
        return "\n".join(str(i) for i in list(queue.items))

queue = Queue.from_list([1,2,3])
queue.enqueue(4)

print(QueuePrinter.to_text(queue))

queue.dequeue()

print(queue)

    