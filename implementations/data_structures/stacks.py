class Stack:
    '''A simple implementation of a stack data structure using a list.'''

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    

# Example usage:
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    print("Stack items:", my_stack.stack)  # Output: Stack items: [1, 2, 3, 4]
    print("Top item:", my_stack.peek())  # Output: Top item: 4
    print("Stack size:", my_stack.size())  # Output: Stack size: 4
    print("Popped item:", my_stack.pop())  # Output: Popped item: 4
    print("Stack size after pop:", my_stack.size())  # Output: Stack size after pop: 3      
    print("Is stack empty?", my_stack.is_empty())  # Output: Is stack empty? False
    print("Popped item:", my_stack.pop())  # Output: Popped item: 3
    print("Popped item:", my_stack.pop())  # Output: Popped item: 2
    print("Popped item:", my_stack.pop())  # Output: Popped item: 1
    print("Is stack empty after popping all items?", my_stack.is_empty())  # Output: Is stack empty after popping all items? True