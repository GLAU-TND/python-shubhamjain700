a=int(input())


res=list(map(int,input().split()))

h=max([res.count(i) for i in res])

print(h)


