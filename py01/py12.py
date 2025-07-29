import random

def doubleReturn():
  num1 = random.randint(1, 5)
  num2 = random.randint(1, 5)
  num3 = num1 * num2
  return num1, num2, num3 #タプルとして結果を返す

rev1,rev2,rev3 = doubleReturn()
print(rev1,rev2,rev3)