arr = [56,87,62,26,71,52,61,79,92,42]
path = 'sample01.txt' #ファイルパス

def toStr(num):
  return str(num) + '\n'

with open(path, mode='w') as f:  #ファイルを書き込みモードで開く（ファイルポインタがfに入る）
  arrStr = list(map(toStr, arr))
  f.writelines(arrStr)

with open(path, mode='r') as f:
  lines = f.read()
  print(lines)

with open(path, mode='r') as f:
  lineList = f.readlines()
  print(lineList)
  for num in lineList:
    print(num.strip()) #stripで改行コードを除去して出力