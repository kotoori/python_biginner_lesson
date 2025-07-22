def calculateBMI(weight, height):
  heightInMeter = height / 100 #cmからmに変換
  bmi = weight / (heightInMeter ** 2) #bmiの計算 **2は2乗
  return bmi #計算結果を返す

def getBMIStatus(bmi):
  if bmi < 18.5:
    return 'やせすぎ'
  elif bmi < 25:
    return '標準'
  elif bmi < 30:
    return 'ちょっと肥満'
  else:
    return '肥満'


userWeight = 53 #体重 kg
userHeight = 176 #身長 cm
userBMI = calculateBMI(userWeight, userHeight)
print(userBMI)
print(getBMIStatus(userBMI))
