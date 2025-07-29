arr = [56,87,62,26,71,52,61,79,92,42]
total = 0 #初期化

for num in arr:
  total += num

print('total:' + str(total))
print('average:' + str(total / len(arr)))