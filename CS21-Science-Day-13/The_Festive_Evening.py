n,k=map(int,input().split())
guests=input()
guest_dict,guest_set={},set()

for i in range(n):
    guest_dict[guests[i]]=i

for i in range(n):
    guest_set.add(guests[i])
    if(len(guest_set)>k):
        print("YES")
        break
    if(i==guest_dict[guests[i]]):
        guest_set.remove(guests[i])
if(len(guest_set)<=k):
    print("NO")

#time=O(N)
