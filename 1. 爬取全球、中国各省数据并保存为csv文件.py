import json
import requests
import csv

# url_china 中国各省市实时数据
url_china = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
response_china = requests.get(url=url_china).json()
data_china = json.loads(response_china['data'])

# url_daily 中国每日疫情历史数据
url_daily = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
response_daily = requests.get(url=url_daily).json()
data_daily = json.loads(response_daily['data'])

# url_world 全球实时及历史数据
url_world = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign'
response_world = requests.get(url=url_world).json()
data_world = json.loads(response_world['data'])

lastUpdateTime = data_china["lastUpdateTime"]  # 数据最近更新时间
directory = "C:/Users/Yestin/Desktop/"  # 定义保存路径

# 获取中国各省当日实时数据
china_data = data_china["areaTree"][0]["children"]
filename = directory + lastUpdateTime.split(' ')[0] + "更新_中国各省疫情数据.csv"
with open(filename, "w+", encoding="utf_8_sig", newline="") as csv_file:
    writer = csv.writer(csv_file)
    header = ["province", "total_confirm", "total_nowConfirm", "total_dead", "total_heal", "today_confirm"]
    writer.writerow(header)
    for i in range(len(china_data)):
        province = china_data[i]["name"]  # 省份
        total_confirm = china_data[i]["total"]["confirm"]  # 总确诊病例
        total_nowConfirm = china_data[i]["total"]["nowConfirm"]  # 现存确诊
        total_dead = china_data[i]["total"]["dead"]  # 总死亡病例
        total_heal = china_data[i]["total"]["heal"]  # 总治愈病例
        today_confirm = china_data[i]["today"]["confirm"]  # 今日确诊病例
        data_row = [province, total_confirm, total_nowConfirm, total_dead, total_heal, today_confirm]
        writer.writerow(data_row)

# 获取中国每日疫情历史数据
DailyData = data_daily["chinaDayList"]
filename = directory + lastUpdateTime.split(' ')[0] + "更新_中国每日疫情历史数据.csv"
with open(filename, "w+", encoding="utf_8_sig", newline="") as csv_file:
    writer = csv.writer(csv_file)
    header = ["confirm", "dead", "heal", "nowConfirm", "importedCase", "deadRate", "healRate", "date"]
    writer.writerow(header)
    for i in range(len(DailyData)):
        confirm = DailyData[i]["confirm"]  # 累计确诊病例
        dead = DailyData[i]["dead"]  # 累计死亡病例
        heal = DailyData[i]["heal"]  # 累计治愈病例
        nowConfirm = DailyData[i]["nowConfirm"]  # 现有确诊病例
        importedCase = DailyData[i]["importedCase"]  # 累计境外输入病例
        deadRate = DailyData[i]["deadRate"]  # 实时死亡率
        healRate = DailyData[i]["healRate"]  # 实时治愈率
        date = DailyData[i]["date"][:2]+"/"+DailyData[i]["date"][3:]  # 日期
        data_row = [confirm, dead, heal, nowConfirm, importedCase, deadRate, healRate, date]
        writer.writerow(data_row)

# 获取国外疫情数据
global_data = data_world["foreignList"]
filename = directory + lastUpdateTime.split(' ')[0] + "更新_国外疫情数据.csv"
with open(filename, "w+", encoding="utf_8_sig", newline="") as csv_file:
    writer = csv.writer(csv_file)
    header = ["country", "continent", "total_confirm", "total_nowConfirm", "total_dead", "total_heal", "date"]
    writer.writerow(header)
    for i in range(len(global_data)):
        country = global_data[i]["name"]  # 国家
        continent = global_data[i]["continent"]  # 所在地区
        total_confirm = global_data[i]["confirm"]  # 总确诊病例
        total_nowConfirm = global_data[i]["nowConfirm"]  # 现存确诊
        total_dead = global_data[i]["dead"]  # 总死亡病例
        total_heal = global_data[i]["heal"]  # 总治愈病例
        date = global_data[i]["date"][:2]+"/"+global_data[i]["date"][3:]  # 日期
        data_row = [country, continent, total_confirm, total_nowConfirm, total_dead, total_heal, date]
        writer.writerow(data_row)
