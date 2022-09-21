n = int(input())
candles = list(map(int, input().split()))

MAX = 0
count = 0

for i in range(len(candles)):
    if MAX < candles[i]:
        MAX = candles[i]
        
for i in range(len(candles)):
    if candles[i] == MAX:
        count += 1 

print(count)
