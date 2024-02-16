N = input()
A =list(map(int,input().split()))
for a in A:
    if a != A[0]:
        print('No')
        exit()

print('Yes')         
