class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.size=0
        
    def PrintStack(self):
        current=self.top
        while current is not None:
            print(current.data,'-->', end="")
            current=current.next
        print('null')
        
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.top is None
    
    def getTop(self):
        return self.top.data
    
    def pop(self):
        assert not self.isEmpty()
        top=self.top
        self.top=self.top.next
        self.size-=1
        return top.data
    
    def push(self,newData):
        newNode=Node(newData)
        if self.top:
            newNode.next=self.top
            self.top=newNode
            self.size+=1
        else:
            self.top=newNode
            self.size+=1
        
    
s=Stack()
s.push('y')
s.push('h')
s.push('t')


print(s.pop())

