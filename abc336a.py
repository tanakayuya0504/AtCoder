def solve(N):
    S = 'L'
    for idx in range(N):
        S += 'o'
        
    S += 'ng'
    
    return S
    
N = int(input())
ans = solve(N)

print(ans)
