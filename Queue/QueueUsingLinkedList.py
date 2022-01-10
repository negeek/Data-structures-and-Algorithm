class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self._qhead=None
        self._qtail=None
        self._count=0
    def isEmpty(self):
        return self._qhead is None
    def __len__(self):
        return self._count
    def enqueue(self,data):
        node=Node(data)
        if self.isEmpty():
            self._qhead=node
        else:
            self._qtail.next=node

        self._qtail=node
        self._count+=1
    def dequeue(self):
        assert not self.isEmpty()
        node=self._qhead
        if self._qhead is self._qtail:
            self._qtail=None
        self._qhead=self._qhead.next
        self._count-=1
        return node.data


s=Queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)

print(s.dequeue())
        
