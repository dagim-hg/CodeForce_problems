n = int(input())
List = list(map(int, input().split()))
start = 0
end = len(List)-1

for i in range(n):
  sub_max = List.index(max(List[start:end+1]))
  if sub_max == List[end]:
    end -=1
  else:
    List[sub_max], List[end] = List[end], List[sub_max]
    end -=1
print(List)