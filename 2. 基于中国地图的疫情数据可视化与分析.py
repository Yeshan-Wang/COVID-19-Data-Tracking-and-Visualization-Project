import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts

# 读取任务1获取到的疫情数据，确定任务所需的数据字段
china_data = pd.read_csv(r'C:/Users/Yestin/Desktop/2020-06-11更新_中国各省疫情数据.csv', encoding="utf_8_sig")
chinaMap_data = china_data[['province', 'total_confirm', 'total_nowConfirm']].groupby('province').sum().sort_values(by='total_confirm', ascending=False)



# 绘制中国各省累计确诊数据分布图
total_confirm_map = (
    Map()
    .add('', [list(z) for z in zip(chinaMap_data.index, chinaMap_data.total_confirm)], 'china')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
            # 设置标题
            title_opts=opts.TitleOpts(title="中国各省累计确诊数据分布图"),
            tooltip_opts=opts.TooltipOpts(formatter='{b}: {c}'),
            # 设置视觉效果
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                              pieces=[
                                                  {'min': 10001, 'label': '>10000', "color": "#893448"},
                                                  {'min': 1000, 'max': 10000, 'label': '1000-10000', "color": "#ff585e"},
                                                  {'min': 500, 'max': 999, 'label': '500-999', "color": "#ffb248"},
                                                  {'min': 100, 'max': 499, 'label': '100-499', "color": "#fff2d1"},
                                                  {'min': 1, 'max': 99, 'label': '1-99', "color": "#f7f7f7"}
                                              ]),
        )
)

# 绘制中国各省现存确诊数据分布图
total_nowConfirm_map = (
    Map()
    .add('', [list(z) for z in zip(chinaMap_data.index, chinaMap_data.total_nowConfirm)], 'china')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
            # 设置标题
            title_opts=opts.TitleOpts(title="中国各省现存确诊数据分布图"),
            tooltip_opts=opts.TooltipOpts(formatter='{b}: {c}'),
            # 设置视觉效果
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                              pieces=[
                                                  {'min': 21, 'label': '20人以上', "color": "#55ff55"},
                                                  {'min': 11, 'max': 20, 'label': '11-20人', "color": "#ffb248"},
                                                  {'min': 1, 'max': 10, 'label': '1-10人', "color": "#fff2d1"},
                                                  {'max': 0, 'label': '0人', "color": "#f7f7f7"}
                                              ]),
        )
)

# 保存为html文件
total_confirm_map.render(r'C:/Users/Yestin/Desktop/中国各省累计确诊数据分布图.html')
total_nowConfirm_map.render(r'C:/Users/Yestin/Desktop/中国各省现存确诊数据分布图.html')