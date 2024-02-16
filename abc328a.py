N,X = list(map(int,input().split()))
S = list(map(int,input().split()))

Y = 0
for s in S:
    if s <= X:
        # print(Y)
        Y += s
print(Y)