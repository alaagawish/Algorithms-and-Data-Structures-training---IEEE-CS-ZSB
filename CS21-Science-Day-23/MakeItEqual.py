towersNum , slices = map(int,input().split())
 
towers=list(map(int,input().split()))
towers.sort(reverse=True)
 
c=0
last=towers[-1]
first=towers[0]
next=1
m=0
while first != last:
    while first == towers[next]:
        next+=1
    if c+next > slices:
        m+=1
        c=next
    else:
        c+=next
    first-=1
    
if c>0:
    m+=1
    
print(m)
