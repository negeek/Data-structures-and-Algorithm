class Queue:
    def __init__(self):
        self._qList=list()

    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self._qList)
    def enqueue(self, data):
        self._qList.append(data)
        
    def dequeue(self):
        assert not self.isEmpty()
        return self._qList.pop(0)
    def printQueue(self):
        print(self._qList)




q=Queue()
q.enqueue(3)
q.enqueue(4)
q.printQueue()
