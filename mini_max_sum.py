l = sorted(map(int, input().split()))
print(sum(l[:len(l)-1]), sum(l[1:]))
