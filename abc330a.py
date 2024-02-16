n,l = map(int,input().split())
a = list(map(int,input().split()))
ok = 0

for x in a:
    if x >= l:
        ok += 1

print(ok)
