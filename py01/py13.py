lang1 = {"id":1,"name":"Python","type":"Script"}
lang2 = {"id":2,"name":"PHP","type":"Script"}
lang3 = {"id":3,"name":"Java","type":"Compile"}
lang4 = {"id":4,"name":"C#","type":"Compile"}
lang5 = {"id":5,"name":"JavaScript","type":"Script"}

for k,v in lang1.items():
  print(str(k) + ':' + str(v))

for v in lang1.values():
  print(v)

langs = [lang1,lang2,lang3,lang4,lang5] #辞書をリストに格納

for lang in langs:
  for k,v in lang.items():
    print(str(k) + ':' + str(v))
