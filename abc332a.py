N,S,K =list(map(int,input().split()))
sum = 0
for i in range(N):
    p,q =list(map(int,input().split()))
    sum += p * q 
if S <= sum:
    sum += 0
else:
    sum += K
print(sum)
