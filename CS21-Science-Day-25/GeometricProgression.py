
nums , favNum = map(int,input().split())
  
n =list(map(int,input().split()))
c=0
dic = {}
dicNums = {}
# if len(list(set(n)))==1 and favNum==1:
#   print(1)
# else:
#     for i in range(0,nums-1):
#         if (n[i]*favNum in list(set(n[i+1:]))) and ( n[i]*(favNum)**2 in list(set(n[i+1:])) ):

#             c+=n[i+1:].count(n[i]*favNum)+n[i+1:].count(n[i]*(favNum)**2)
    
#     print(c)

for i in range(nums):
    element = n[i]
    if (element % favNum == 0):
        c += dic.get(element/ favNum , 0)
        dic[element] = dic.get(element, 0) + dicNums.get(element/ favNum , 0)
    dicNums[element] = dicNums.get(element, 0)+1
print(c)
