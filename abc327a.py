N = int(input())
S = input()
for i in range(N-1):
    if S[i] == 'a' and S[i + 1] == 'b':
        print('Yes')
        exit()
    elif S[i] == 'b' and S[i + 1] == 'a':
        print('Yes')
        exit()
print('No')
        
