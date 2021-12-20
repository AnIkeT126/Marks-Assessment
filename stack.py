class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
        print(self.items)
 
    def pop(self):
        return self.items.pop() 
        #for queue write return self.items.pop(0) 
 
 
s = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('choose one ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break