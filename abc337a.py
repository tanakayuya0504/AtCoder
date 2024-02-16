N = int(input())

TakahashiScore = 0 
AokiScore = 0 :

for i in range(N):
    X, Y = map(int, input().split())
       
    TakahashiScore += X
    AokiScore += Y

if TakahashiScore > AokiScore:
    print('Takahashi')
elif TakahashiScore < AokiScore:
    print('Aoki')
else:
    print('Draw')
