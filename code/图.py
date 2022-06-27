import os
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline, Pie, Line, Bar
import pandas as pd
import numpy as np
from pyecharts.charts import Page
from pyecharts.globals import ThemeType


def economy():
    d = pd.read_csv('E:\lianxi\python\综合课设三\gmjj\GDP.csv', usecols=['Quater', 'GDP_Absolute', 'GDP_YOY'])
    d = np.array(d)
    year = []
    for i in range(len(d)):
        year.append(d[i][0][:4])
    year = list(set(year))
    year.sort()
    y_GDP = []  # 存储每一年的GDP总值以及增长率
    y_GDP_zzl = []
    for i in year:
        for j in range(len(d)):
            if d[j][0][:4] == i:
                y_GDP.append(d[j][1])  # 取一年的GDP
                y_GDP_zzl.append(d[j][2][:-1])
                break
    print(y_GDP_zzl)
    bar = (Bar().add_xaxis(xaxis_data=year)
           .add_yaxis(series_name='GDP总值', y_axis=y_GDP, yaxis_index=1)
           # 对y轴配置，value代表数据
           .extend_axis(yaxis=opts.AxisOpts(type_='value', name='GDP',
                                            is_show=True,  # 展示该轴
                                            min_=10000,  # 轴的刻度
                                            max_=2000000, position='left',
                                            ))
           .extend_axis(yaxis=opts.AxisOpts(type_='value', name='GDP增长率',
                                            is_show=True,  # 展示该轴
                                            min_=1,  # 轴的刻度
                                            max_=20, position='right',
                                            axislabel_opts=opts.LabelOpts(
                                                formatter="{value}%")
                                            ))
           .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
           .set_global_opts(title_opts=opts.TitleOpts(title='中国GDP情况', pos_left='%0'), legend_opts=opts.LegendOpts(
        pos_left="15%")))
    line = (Line().add_xaxis(year)
            .add_yaxis(series_name='GDP增长率', y_axis=y_GDP_zzl, yaxis_index=2, is_smooth=True, label_opts=opts.LabelOpts(is_show=False))
            )
    bar.overlap(line)
    bar.render('中国经济.html')
    os.system('中国经济.html')


def zx(new_country):
    d = pd.read_csv('owid-covid-data.csv', usecols=['location', 'date', 'total_vaccinations'])
    d['total_vaccinations'] = d['total_vaccinations'].fillna(0)  # 将空格的地方补0
    d = np.array(d)
    world_ym = {}
    for i in new_country:
        qz = 0
        for j in range(len(d) - 1):  # 获取每个国家接种疫苗总数
            if d[j][0] == i and d[j + 1][0] != i:  #
                qz = d[j][2]
        world_ym[i] = qz
    world_ym = sorted(world_ym.items(), key=lambda e: e[1], reverse=True)
    pie = Pie(init_opts=opts.InitOpts(width='1920px', height='1080px', theme=ThemeType.INFOGRAPHIC))  # 或者自定义颜色
    pie.add('疫苗接种情况', world_ym[:20],
            radius=["10%", "125%"],
            center=["50%", "66%"],
            rosetype="area",
            is_clockwise=False)
    pie.set_global_opts(title_opts=opts.TitleOpts(title='各国疫苗接种情况'),
                        legend_opts=opts.LegendOpts(is_show=True, pos_left='75%'))
    pie.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    return pie


def map(new_date):
    d = pd.read_csv('owid-covid-data.csv', usecols=['location', 'date', 'total_cases'])
    d = np.array(d)
    world_yq = {}
    for i in new_date:
        qz = []
        for j in range(len(d) - 1):  # 获取每个国家每月累计确诊人数
            if d[j][1][:7] == i and d[j + 1][1][:7] != i:  # 取每个月的最后一天
                qz.append([d[j][0], d[j][2]])  # 确诊病例数
        world_yq[i] = qz
    tl = Timeline()
    # 自定义的每一段的取值范围
    during = [
        {"min": 10000000},
        {"min": 1000000, "max": 9999999},
        {"min": 100000, "max": 999999},
        {"min": 10000, "max": 99999},
        {"min": 1000, "max": 9999},
        {"min": 0, "max": 999},
    ]
    # range_color=["#F6CECE", "#B40404"]
    for i in new_date:
        map0 = (
            Map()
                .add("最新确诊人数", world_yq[i], "world", is_map_symbol_show=False)
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}全球疫情情况".format(i)),
                visualmap_opts=opts.VisualMapOpts(max_=10000000, is_piecewise=True, pieces=during),
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # label_opts:标签配置项设置，is_show：是否显示视觉映射配置
        )
        tl.add(map0, "{} ".format(i))
    tl.add_schema(is_auto_play=True, play_interval=1000)  # 自动播放，跳动的间隔为1000ms
    return tl


def main():
    # 读取数据
    data = pd.read_csv("owid-covid-data.csv")
    d = np.array(data)
    date = []  # 日期：年-月
    country = []
    for i in range(len(d)):
        date.append(d[i][3][:7])
        country.append(d[i][2])
    new_date = list(set(date))
    new_date.sort()
    new_country = list(set(country))
    page = Page(layout=Page.DraggablePageLayout)
    map0 = map(new_date)
    map1 = zx(new_country)
    page.add(map0, map1)
    page.render("全球疫情.html")
    os.system("全球疫情.html")
    zx(new_country)


economy()
# main()
