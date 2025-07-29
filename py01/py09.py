import random #標準ライブラリのrandomモジュールを読み込む

inputNum = int(input('1から10の整数を入力してください：'))

while True:
  num = random.randint(1, 10) #1から10の整数をランダムに生成
  if num == inputNum:
    print('一致')
    break
  else:
    print('不一致(' + str(num) + ', ' + str(inputNum) + ')')

