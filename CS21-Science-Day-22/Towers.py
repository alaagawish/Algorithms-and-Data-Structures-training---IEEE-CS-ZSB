
towers ,operationsNum = map(int , input().split())
towersHeights = list(map(int , input().split()))
changes = []
for i in range(operationsNum):
    minH ,maxH = min(towersHeights) , max(towersHeights)
    instability=max(towersHeights)-min(towersHeights)
    minindex , maxindex = towersHeights.index(minH) , towersHeights.index(maxH)
    if instability !=0 :
        changes.append(str(maxindex+1)+" " +str(minindex+1))
        towersHeights[minindex] += 1
        towersHeights[maxindex] -=1
        
        
print(max(towersHeights)-min(towersHeights) , len(changes))
for i in changes :
    print(i)
