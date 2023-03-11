def solution(dict, f, i):
  plays = 0
  while f>i:
    maxReturn = 0
    for key, value in dict.items():
      if key <= i:
        if value > maxReturn:
          maxReturn = value
    i+=maxReturn
    plays+=1
  return plays

def createDict(n):
  dict = {}
  for i in range(n):
    cost,reward = map(int, input().split())
    if cost not in dict:
      dict[cost] = reward-cost
    else:
      if reward-cost > dict[cost]:
        dict[cost] = reward-cost
  return dict


t = int(input())
for i in range(t):
  l1 = list(map(int, input().split()))  
  dict = createDict(l1[0])

  ans = solution(dict , l1[1], l1[2])

  print("Case #" + str(i + 1) + ":", ans)



