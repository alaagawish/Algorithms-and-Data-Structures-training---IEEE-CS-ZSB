planDays,chosenDays=map(int,input().split())
total=[]
t=0
for i in range(planDays):
    products,clients=map(int,input().split())

    # if (i+1)% chosenDays ==0:
    #     products=2*products
    #     if products >= clients:
    #         total+= clients
    #     elif products < clients and products !=0 :
    #         total+=clients
    
    t+=min(products,clients)
    total.append(min(2*products,clients)-min(products,clients))
total.sort()
print(t+sum(total[planDays - chosenDays:]))

# Time=O(n)
