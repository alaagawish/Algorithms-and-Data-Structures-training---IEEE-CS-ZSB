nodes , edges = map(int,input().split())
  
x=list(map(int,input().split()))

error =0

for i in range(edges):
  
    a,b,c = map(int,input().split())
    
    error  = max(error , (x[a-1]+x[b-1])/c)
    
print(error)
