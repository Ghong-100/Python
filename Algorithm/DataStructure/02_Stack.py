class Stack:
    def __init__(self):
        self.stack_list = list()
    def push(self, data):
        self.stack_list.append(data)
    def pop(self):
        data = self.stack_list[-1]
        del self.stack_list[-1]
        return data

stack = Stack()

for index in range(10):
    stack.push(index)

for index in range(len(stack.stack_list)):
    print(stack.pop())