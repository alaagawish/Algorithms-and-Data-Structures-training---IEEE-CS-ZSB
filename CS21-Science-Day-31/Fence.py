n, k =map(int,input().split())
 
h =list(map(int,input().split()))
 
ans = (sum(h[:k]), 0)

minn = ans[0]

if k==n or len(list(set(h)))==1:
    print(1)
else:
    for i in range(1, n - k + 1):
        s = minn - h[i - 1] + h[i + k - 1]
        minn = s
        if s < ans[0]:
            ans = (s, i)

    print(ans[1] + 1)
