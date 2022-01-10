class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
        
    def __len__(self):
        return self.size

    def PrintList(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
            
    def append(self, newdata):
        newNode=Node(newdata)
        current=self.head
        if self.head:
            while current.next:
                current=current.next
            current.next=newNode
            self.size+=1
        else:
            self.head=newNode
            self.size+=1

    def middle(self):
        counter=0
        position=self.size//2
        current=self.head
        if self.head:
            while current.next:
                current=current.next
                counter+=1
                if counter==position:
                    return current.data

    def rotate(self,k):
        counter=1
        current=self.head
        while (counter <k and current is not None):
            current=current.next
            counter+=1
        kpointer=current

        while current.next:
            current=current.next
        current.next=self.head
        self.head=kpointer.next
        kpointer.next=None

    def reverse(self):
        prev=None
        current=self.head
        
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next

        self.head=prev

   
        
        
        
        
s=LinkedList()
s.append('r')
s.append('a')
s.append('d')
s.append('a')
s.append('r')

s.reverse()


print(s==s.reverse())







