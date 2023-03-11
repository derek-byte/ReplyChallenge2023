def solution(arr, f):
  dist = []
  for i in range(len(arr)):
    for j in range(len(arr)):
      dist.append(abs(arr[j][0] - arr[i][0]) + abs(arr[j][1] - arr[i][1]))
  print(dist)
      
      
  # for i in range(n):
    
def getArray(n):
  arr = []
  for i in range(n):
    arr.append(list(map(int, input().split())))
  return arr

t = int(input())
for i in range(t):
  l1 = list(map(int, input().split()))  

  arr = getArray(l1[3])
  ans = solution(arr, l1[2])

  print("Case #" + str(i + 1) + ":", ans)
