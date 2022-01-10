n=int(input())   
disks=list(map(int, input().split()))
priorityDisk=[i for i in range(n,0,-1)]  #create a priority list
diffList=[]   #difference list
tower=[]    #list to get correct output
pick=1       #picks from priority list
maxDisk=max(disks)
varMaxDisk=maxDisk
for i in range(n):
    diffList.append(maxDisk-disks[i])   #appends difference 
    if disks[i]==varMaxDisk:
        sortDiffList=sorted(diffList)   #sorts difference list
        for j in range(len(sortDiffList)):
            if sortDiffList[j]!=sortDiffList[-1]:
                if sortDiffList[j+1]-sortDiffList[j]==1: #if difference between an item and next item in difference list is 1
                    pick+=1
                else:
                    break
        for k in range(pick):
            tower.append(str(priorityDisk.pop(0)))
            sortDiffList.pop(0)
        print(" ".join(tower))
        tower=[]
        diffList=sortDiffList
        varMaxDisk-=pick
        pick=1                
    else:
        print("\n")

        
