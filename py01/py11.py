fruits = ['apple','grape','orange','meron']

for item in fruits:
  print(item)

inputFruit = input('追加の果物を入力してください：')
addItem = [inputFruit] #リストに変換
fruits += addItem #リストに追加(リスト同士なら結合できる)

for item in fruits:
  print(item)