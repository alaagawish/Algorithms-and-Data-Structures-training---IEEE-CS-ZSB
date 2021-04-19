from collections import defaultdict
myname, p = input(), defaultdict(int)

for i in range(int(input())):
    action  = input().split()
    name1, operation = action [0], action [1][0]

    if operation == 'p': 
        name2, priority  = action [3][: -2], 15
    elif operation == 'c': 
        name2, priority  = action [3][: -2], 10
    else: 
        name2, priority  = action [2][: -2], 5
        
    if name1 == myname: 
        p[name2] += priority 
    elif name2 == myname: 
        p[name1] += priority 
    else: 
        p[name1], p[name2]
r = defaultdict(list)
for i, j in p.items(): 
    r[j].append(i)
    
for j in r: 
    r[j] = '\n'.join(sorted(r[j]))

q = sorted(r.items(), reverse = True)
print('\n'.join(i[1] for i in q))
