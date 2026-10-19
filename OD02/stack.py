class Stack:                       
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Удаление из пустого стека")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Получение из пустого стека")
        return self.items[-1]

    def __bool__(self):
        return bool(self.items)

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"Стек({self.items!r})"

    @classmethod
    def from_list(cls, items):
        stack = cls()
        for x in items:
            stack.push(x)
        return stack


class StackPrinter: 
    @staticmethod
    def to_text(stack: Stack) -> str:
        return "\n".join(str(i) for i in reversed(stack.items))

stack = Stack.from_list([1,2,3])
stack.push(4)

print(StackPrinter.to_text(stack))

stack.pop()

print(stack)

    