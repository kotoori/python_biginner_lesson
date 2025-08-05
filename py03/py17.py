import requests
import json
import matplotlib.pyplot as plt

# 日本語フォントの指定
plt.rcParams["font.family"] = "YuGothic"

#WebAPIからJSONデータを取得し、JSON形式で返す
def get_weather_data():
  url = "https://api.open-meteo.com/v1/forecast?latitude=35.68&longitude=139.76&hourly=temperature_2m&timezone=Asia%2FTokyo"
  res = requests.get(url) #URLからデータを取得
  return res.json() #JSON形式で返す

# データをファイルに保存する関数
def save_to_file(filename, data):
  with open(filename, "w", encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)

#ファイルを読み出す関数 pythonのデータ型に変換して返す
def load_from_file(filename):
  with open(filename, "r", encoding="utf-8") as f:
    return json.load(f)

# メイン関数 データを処理して、グラフを作成する関数
def main():
  data = get_weather_data()

  #取得したデータ空1日分の時間と気温を取得する
  times = data["hourly"]["time"][:24] # 1日分(先頭から24個分)の時間を取得
  temps = data["hourly"]["temperature_2m"][:24]
  
  #時間と気温のペアを作る
  daily_weather = [{"time":t, "temp":temp} for t,temp in zip(times,temps)]
  save_to_file("weather.json", daily_weather)
  loaded = load_from_file("weather.json")
  print("1日分の気温データ")
  for entry in loaded:
    print(f"{entry['time']}時:{entry['temp']}℃")

  # グラフを作成する
  x_labels = [t[-5:] for t in times] # 文字を一部切り取り
  plt.figure(figsize=(10,5))
  plt.plot(x_labels, temps, marker="o")
  plt.title("今日の気温")
  plt.xlabel("時刻")
  plt.ylabel("気温")
  plt.xticks(rotation=45)
  plt.grid()
  plt.tight_layout()
  plt.show()
  
if __name__ == "__main__":
  main()
