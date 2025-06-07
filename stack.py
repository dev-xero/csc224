class Stack:
    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._data = []
    
    def push(self, item):
        if (self.is_full()):
            raise Exception("Stack overflow: capacity exceeded")
        self._data.append(item)
        self._size += 1

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack underflow: cannot pop from empty stack")
        self._size -= 1
        return self._data.pop()
    
    def peek(self):
        """Return the top element without removing it"""
        if self.is_empty():
            raise Exception("Cannot peek: stack is empty")
        return self._data[-1]

    def is_empty(self):
        """Check if stack is empty"""
        return self._size == 0
    
    def is_full(self):
        """Check if stack is at capacity"""
        return self._size >= self._capacity

    def get_size(self):
        "Return stack size"
        return self._size

    def get_capacity(self):
        "Return capacity of the stack"
        return self._capacity
    

if __name__ == "__main__":
    stack = Stack(10)
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(f"Peek: {stack.peek()}")
    print(f"size: {stack.get_size()}")
    print(f"Popped: {stack.pop()}")

