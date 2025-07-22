import math

def calculateCircleLength(radius):
  circleLength = radius * 2 * math.pi
  return circleLength

inputRadius = int(input('半径を入力してください: '))
circleLength = calculateCircleLength(inputRadius)
print(circleLength)