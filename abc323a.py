S = input()


count = True
for i in range(1,16,2):
    if S[i] != '0':
        count = False

if count:
    print('Yes')
else:
    print('No')
