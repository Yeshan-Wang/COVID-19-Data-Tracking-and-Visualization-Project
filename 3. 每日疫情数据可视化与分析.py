import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts

# 读取任务1获取到的疫情数据，确定任务所需的数据字段
daily_data = pd.read_csv(r'C:/Users/Yestin/Desktop/2020-06-11更新_中国每日疫情历史数据.csv', encoding="utf_8_sig")

# 绘制 全国现有确诊趋势 折线图
line1 = (
    Line()
    # x轴
    .add_xaxis(list(daily_data.date))
    # y轴
    .add_yaxis('现有确诊', list(daily_data.nowConfirm))
    # 标题
    .set_global_opts(title_opts=opts.TitleOpts(title="全国现有确诊趋势"))
)

# 绘制 全国累计确诊/治愈/死亡趋势 折线图
line2 = (
    Line()
    # x轴
    .add_xaxis(list(daily_data.date))
    # y轴
    .add_yaxis('确诊人数', list(daily_data.confirm))
    .add_yaxis('治愈人数', list(daily_data.heal))
    .add_yaxis('死亡人数', list(daily_data.dead))
    # 标题
    .set_global_opts(title_opts=opts.TitleOpts(title="全国累计确诊/治愈/死亡趋势"))
)

# 绘制 全国治愈率/病死率趋势 折线图
line3 = (
    Line()
    # x轴
    .add_xaxis(list(daily_data.date))
    # y轴
    .add_yaxis('治愈率', list(daily_data.healRate))
    .add_yaxis('病死率', list(daily_data.deadRate))
    # 标题
    .set_global_opts(title_opts=opts.TitleOpts(title="全国治愈率/病死率趋势"))
)

# 绘制 境外输入累计趋势 折线图
line4 = (
    Line()
    # x轴
    .add_xaxis(list(daily_data.date))
    # y轴
    .add_yaxis('累计境外输入病例', list(daily_data.importedCase))
    # 标题
    .set_global_opts(title_opts=opts.TitleOpts(title="境外输入累计趋势"))
)

# 保存为html文件
line1.render(r'C:/Users/Yestin/Desktop/全国现有确诊趋势.html')
line2.render(r'C:/Users/Yestin/Desktop/全国累计确诊治愈死亡趋势.html')
line3.render(r'C:/Users/Yestin/Desktop/全国治愈率病死率趋势.html')
line4.render(r'C:/Users/Yestin/Desktop/境外输入累计趋势.html')
