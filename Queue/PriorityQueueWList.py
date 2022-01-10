class PriorityQueue:
    def __init__(self):
        self._qList=[]

    def isEmpty(self):
        return len(self)== 0
    def __len__(self):
        return len(self._qList)
    def enqueue(self, data, priority):
        index=0
        entry=_PriorityQEntry(data, priority)
        if self.isEmpty():
            self._qList.insert(0, entry)
        else:
            for i in range(self.__len__()):
                if entry.priority<self._qList[i].priority:
                    index=i
                    break
                else:
                    index=i+1
                
                    
            self._qList.insert(index,entry)
    def dequeue(self):
        assert not self.isEmpty()
        entry=self._qList.pop(0)
        return entry.data


class _PriorityQEntry:
    def __init__(self,data, priority):
        self.data=data
        self.priority=priority


s=PriorityQueue()
s.enqueue('f',1)
s.enqueue('o',2)
s.enqueue('v',1)
s.enqueue('c',3)
s.enqueue('d',0)

print(s.dequeue())



    
