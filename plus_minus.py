n = int(input())
arr = list(map(int, input().split()))

pos = 0
neg = 0
zero = 0

for num in arr:
    if num > 0:
        pos+=1
    elif num <0:
        neg+=1
    else:
        zero+=1
        
print("{}\n{}\n{}\n".format(pos/n, neg/n, zero/n))
