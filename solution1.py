L , B = map(int, input().split())
count = 0
while L <= B:
  L *= 3
  B *= 2
  count +=1
print(count)