def algorithm(trackLength, regularSpeed, turboSpeed, turboCooldown,
              Turboduration):
  turboDistance = turboSpeed * Turboduration
  regularDistance = regularSpeed * turboCooldown
  ctr = (trackLength //
         (turboDistance + regularDistance)) * ((turboSpeed + regularSpeed) / 2)
  x = trackLength % (turboDistance + regularDistance)

  if x > turboDistance:
    ctr += Turboduration
    ctr += (x - turboDistance) / regularSpeed
  else:
    ctr += x / turboDistance

  if turboSpeed < regularSpeed:
    return trackLength / regularSpeed
  else:
    return ctr
  
t = int(input())

for i in range(t):
  l1 = list(map(int, input().split()))

  timeArr = []
  for r in range(l1[1]):
    carLine = list(map(int, input().split()))

    carTime = algorithm(l1[0], carLine[1], carLine[2], carLine[3], carLine[4])

    timeArr.append(carTime)

  ans = min(timeArr)
  carNum = timeArr.index(ans)

  print("Case #" + str(i + 1) + ":", carNum)

#https://challenges.reply.com/tamtamy/challenge/code-teen-2023/detail
