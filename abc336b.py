def create_binary_string(N):
    return format(N , 'b')
N = int(input())
binaryN = create_binary_string(N)
binaryN = binaryN[::-1]
ans = 0
for s in binaryN:
    if s == '0':
        ans += 1
    else:
        break
print(ans)