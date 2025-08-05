import json # jsonライブラリ(標準ライブラリー)を読み込む

students = [
    {"name": "田中太郎", "scores": {"国語": 70, "数学": 80, "英語": 90}},
    {"name": "鈴木花子", "scores": {"国語": 85, "数学": 78, "英語": 88}},
    {"name": "佐藤次郎", "scores": {"国語": 92, "数学": 75, "英語": 85}}
]

subjects = students[0]["scores"].keys()
print(subjects)

#各科目ごとの合計点と平均点を出す
# 合計点を計算するための辞書を作成する
total = {subj:0 for subj in subjects}
print(total)

count = len(students) #生徒数を取得

for student in students:
  for subj,score in student["scores"].items():
    total[subj] += score

print(total)

# 平均点を計算する
avg = {subj:round(total[subj]/count,1) for subj in subjects}
print(avg)

# JSONデータを作成する
result = {
  "students": students,
  "average": avg
}

print(json.dumps(result, ensure_ascii=False, indent=2))
