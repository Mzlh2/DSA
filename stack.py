class Stack:
    def __init__(self,myCapacity):
        self.top = -1
        self.capacity = myCapacity
        self.stackArray = [None] * self.capacity

    def push(self, mydata):
        if self.top == self.capacity - 1:
            print("Stack overflow")
            return
        self.top += 1
        self.stackArray[self.top] = mydata
    
    def pop(self):
        if self.top == -1:
            print("stack underflow")
            return
        
        mydata = self.stackArray[self.top]
        self.top -= 1
        return mydata
    
    def peek(self):
        if self.top == -1:
            return
        
        return self.stackArray[self.top]
    
    def isEmpty(self):
        if self.top == -1:
            return False
        
    def isFull(self):
        if self.top == self.capacity - 1:
            return True
        return False
    
myStack = Stack(5)
print(myStack.isEmpty())
print(myStack.isFull())
myStack.push(10)
myStack.push(12)
myStack.push(13)
myStack.push(14)
myStack.push(15)
myStack.push(8)
myStack.push(9)
print("popped data:",myStack.pop())
print("popped data:",myStack.pop())
print("popped data:",myStack.pop())
print("popped data:",myStack.pop())
print("popped data:",myStack.pop())
print("popped data:",myStack.pop())
print("popped data:",myStack.pop())