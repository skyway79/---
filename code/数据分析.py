import os
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline, Pie, Line, Bar, Grid
import pandas as pd
import numpy as np
from pyecharts.charts import Page
from pyecharts.globals import ThemeType


def GDP():
    d = pd.read_csv('E:/lianxi/python/综合课设三/gmjj/GDP.csv')
    d = d.values.tolist()
    Quater = []  # 季度
    GDP_Absolute = []  # 国内生产总值绝对值
    GDP_YOY = []  # 国内生产总值同比增长
    Primary_Indusry_Abs = []  # 第一产业绝对值_亿元
    Primary_Indusry_YOY = []  # 第一产业同比增长
    Secondary_Indusry_Abs = []  # 第二产业绝对值_亿元
    Secondary_Indusry_YOY = []  # 第二产业同比增长
    Tertiary_Indusry_Abs = []  # 第三产业绝对值_亿元
    Tertiary_Indusry_YOY = []  # 第三产业同比增长
    for i in range(len(d) - 1, -1, -1):
        Quater.append(d[i][0][:4] + '-' + d[i][0][6:-2])
        GDP_Absolute.append(d[i][1])
        GDP_YOY.append(d[i][2][:-1])
        Primary_Indusry_Abs.append(d[i][3])
        Primary_Indusry_YOY.append(d[i][4][:-1])
        Secondary_Indusry_Abs.append(d[i][5])
        Secondary_Indusry_YOY.append(d[i][6][:-1])
        Tertiary_Indusry_Abs.append(d[i][7])
        Tertiary_Indusry_YOY.append(d[i][8][:-1])
    line = (Line().add_xaxis(Quater)
            .add_yaxis(series_name='国内生产总值同比增长', y_axis=GDP_YOY, is_smooth=True, yaxis_index=1,
                       label_opts=opts.LabelOpts(is_show=True)
                       )
            .extend_axis(yaxis=opts.AxisOpts(type_='value', name='GDP增长率',
                                             is_show=True,  # 展示该轴
                                             position='right',
                                             axislabel_opts=opts.LabelOpts(
                                                 formatter="{value}%")
                                             ))
            .extend_axis(yaxis=opts.AxisOpts(type_='value', name='GDP',
                                             is_show=True,  # 展示该轴
                                             position='left',
                                             axislabel_opts=opts.LabelOpts(
                                                 formatter="{value}亿元")
                                             ))
            .set_global_opts(title_opts=opts.TitleOpts(title='中国GDP情况'),
                             legend_opts=opts.LegendOpts(is_show=True, pos_left='15%'),
                             datazoom_opts=[
                                 opts.DataZoomOpts(
                                     range_start=98, range_end=100)]
                             )
            )
    bar = (Bar()
           .add_xaxis(Quater)
           .add_yaxis(series_name='国内生产总值绝对值', y_axis=GDP_Absolute, yaxis_index=2)
           .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
           .set_global_opts(legend_opts=opts.LegendOpts(is_show=True, pos_left='25%'))
           )
    bar1 = (Bar()
            .add_xaxis(Quater)
            .add_yaxis(series_name='第一产业总值', y_axis=Primary_Indusry_Abs)
            .add_yaxis(series_name='第二产业总值', y_axis=Secondary_Indusry_Abs)
            .add_yaxis(series_name='第三产业总值', y_axis=Tertiary_Indusry_Abs)

            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='中国三大产业产值情况', pos_left='5%'),
                             legend_opts=opts.LegendOpts(is_show=True, pos_left='25%'),
                             datazoom_opts=[
                                 opts.DataZoomOpts(
                                     range_start=98, range_end=100)]
                             )
            )
    line1 = (Line().add_xaxis(Quater)
             .add_yaxis(series_name='第一产业增长率', y_axis=Primary_Indusry_YOY, is_smooth=True,
                        label_opts=opts.LabelOpts(is_show=True)
                        )
             .add_yaxis(series_name='第二产业增长率', y_axis=Secondary_Indusry_YOY, is_smooth=True,
                        label_opts=opts.LabelOpts(is_show=True))
             .add_yaxis(series_name='第三产业增长率', y_axis=Tertiary_Indusry_YOY, is_smooth=True,
                        label_opts=opts.LabelOpts(is_show=True))
             .set_global_opts(legend_opts=opts.LegendOpts(is_show=True, pos_right='5%'),
                              datazoom_opts=[
                                  opts.DataZoomOpts(
                                      range_start=98, range_end=100)]
                              )
             )
    map2, map3, map4, map5 = economy()
    grid1 = Grid(init_opts=opts.InitOpts(width="1200px",
                                         height="700px"))
    grid1.add(map4, grid_opts=opts.GridOpts(pos_bottom="60%", pos_right='60%'))
    grid1.add(map5, grid_opts=opts.GridOpts(pos_bottom="60%", pos_left='60%'))
    grid1.add(map2, grid_opts=opts.GridOpts(pos_top="60%", pos_right='60%'))
    grid1.add(map3, grid_opts=opts.GridOpts(pos_top="60%", pos_left='60%'))
    line.overlap(bar)
    page = Page(layout=Page.DraggablePageLayout)
    page.add(grid1, line, bar1, line1)
    page.render('中国GDP.html')
    os.system('中国GDP.html')


def CPI():
    d = pd.read_csv('E:/lianxi/python/综合课设三/gmjj/CPI.csv', nrows=49)  # 2018-2022/1
    d = d.values.tolist()
    Month = []
    Nation_YOY = []  # 全国同比增长
    Nation_Comparative_Rate = []  # 全国环比增长
    City_YOY = []  # 城市同比增长
    City_Comparative_Rate = []  # 城市环比增长
    Country_YOY = []  # 农村同比增长
    Country_Comparative_Rate = []  # 农村环比增长
    for i in range(len(d) - 1, -1, -1):
        Month.append(d[i][0])
        Nation_YOY.append(d[i][2][:-1])
        Nation_Comparative_Rate.append(d[i][3][:-1])
        City_YOY.append(d[i][6][:-1])
        City_Comparative_Rate.append(d[i][7][:-1])
        Country_YOY.append(d[i][10][:-1])
        Country_Comparative_Rate.append(d[i][11][:-1])
    line = (Line().add_xaxis(Month)
            .add_yaxis(series_name='全国同比增长', y_axis=Nation_YOY, is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=True),
                       markline_opts=opts.MarkLineOpts(
                           data=[opts.MarkLineItem(type_="average", name="平均值")]
                       ))
            .add_yaxis(series_name='全国环比增长', y_axis=Nation_Comparative_Rate, is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=True))
            .add_yaxis(series_name='城市同比增长', y_axis=City_YOY, is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=True))
            .add_yaxis(series_name='城市环比增长', y_axis=City_Comparative_Rate, is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=True))
            .add_yaxis(series_name='农村同比增长', y_axis=Country_YOY, is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=True))
            .add_yaxis(series_name='农村环比增长', y_axis=Country_Comparative_Rate, is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(title_opts=opts.TitleOpts(title='每月中国居民消费价格指数'),
                             legend_opts=opts.LegendOpts(is_show=True, pos_left='25%'),
                             datazoom_opts=[
                                 opts.DataZoomOpts(type_="inside",
                                                   range_start=98, range_end=100)]
                             )
            )
    return line


def price():
    d = pd.read_csv('E:/lianxi/python/综合课设三/gmjj/Gas_Price.csv', nrows=40)
    d = d.values.tolist()
    date = []
    Gas_Price = []
    Gas_Price_Change = []
    Diesel_Price = []
    Diesel_Price_Change = []
    for i in range(len(d)):  # 从2019年12月到2022年3月
        date.append(d[i][0])
        Gas_Price.append(d[i][1])
        Diesel_Price.append(d[i][3])
        if d[i][2][0] == '↑':
            d[i][2] = d[i][2][1:]
            Gas_Price_Change.append(d[i][2])
        if d[i][4][0] == '↑':
            d[i][4] = d[i][4][1:]
            Diesel_Price_Change.append(d[i][4])
        if d[i][4][0] == '↓':
            d[i][4] = d[i][4][1:]
            d[i][4] = '-' + d[i][4]
            Diesel_Price_Change.append(d[i][4])
        if d[i][2][0] == '↓':
            d[i][2] = d[i][2][1:]
            d[i][2] = '-' + d[i][2]
            Gas_Price_Change.append(d[i][2])
    line = (Line().add_xaxis(list(reversed(date)))
            .add_yaxis(series_name='汽油涨幅', y_axis=list(reversed(Gas_Price_Change)), is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False)
                       )
            .add_yaxis(series_name='柴油涨幅', y_axis=list(reversed(Diesel_Price_Change)), is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='中国油价调整情况', pos_left='5%'),
                             legend_opts=opts.LegendOpts(is_show=True, pos_right='15%'),
                             datazoom_opts=[
                                 opts.DataZoomOpts(
                                     range_start=98, range_end=100)]
                             )
            )
    bar = (Bar()
           .add_xaxis(list(reversed(date)))
           .add_yaxis(series_name='汽油价格', y_axis=list(reversed(Gas_Price)))
           .add_yaxis(series_name='柴油价格', y_axis=list(reversed(Diesel_Price)))
           .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
           .set_global_opts(legend_opts=opts.LegendOpts(is_show=True, pos_left='15%'),
                            datazoom_opts=[
                                opts.DataZoomOpts(
                                    range_start=98, range_end=100)]
                            )
           )
    return bar, line


def economy():
    d = pd.read_csv('E:/lianxi/python/综合课设三/gmjj/GDP.csv')
    d = np.array(d)
    year = []
    for i in range(len(d)):
        year.append(d[i][0][:4])
    year = list(set(year))
    year.sort()
    y_GDP = []  # 存储每一年的GDP总值以及增长率
    y_GDP_zzl = []
    y_Pri = []
    y_Pri_zzl = []
    y_Sec = []
    y_Sec_zzl = []
    y_Ter = []
    y_Ter_zzl = []
    for i in year:
        for j in range(len(d)):
            if d[j][0][:4] == i:
                y_GDP.append(d[j][1])  # 取一年的GDP
                y_GDP_zzl.append(d[j][2][:-1])
                y_Pri.append(d[j][3])
                y_Pri_zzl.append(d[j][4][:-1])
                y_Sec.append(d[j][5])
                y_Sec_zzl.append(d[j][6][:-1])
                y_Ter.append(d[j][7])
                y_Ter_zzl.append(d[j][8][:-1])
                break
    bar1 = (Bar(init_opts=opts.InitOpts(width="650px",
                                        height="400px")).add_xaxis(xaxis_data=year)
            .add_yaxis(series_name='GDP总值', y_axis=y_GDP,
                       itemstyle_opts=opts.ItemStyleOpts(color='#088A08'))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='中国GDP情况', pos_left='5%', pos_top='50%'),
                             legend_opts=opts.LegendOpts(is_show=True, pos_left='15%', pos_top='55%')
                             ))
    line1 = (Line().add_xaxis(year)
             .add_yaxis(series_name='GDP增长率', y_axis=y_GDP_zzl, is_smooth=True,
                        label_opts=opts.LabelOpts(is_show=True))
             .set_global_opts(title_opts=opts.TitleOpts(title='中国一年GDP同比增长率', pos_right='5%', pos_top='50%'),
                              legend_opts=opts.LegendOpts(is_show=True, pos_right='25%', pos_top='55%'))
             )
    bar2 = (Bar()
            .add_xaxis(year)
            .add_yaxis(series_name='第一产业总值', y_axis=y_Pri)
            .add_yaxis(series_name='第二产业总值', y_axis=y_Sec)
            .add_yaxis(series_name='第三产业总值', y_axis=y_Ter)

            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='中国三大产业产值情况', pos_left='5%'),
                             legend_opts=opts.LegendOpts(is_show=True, pos_left='25%'))
            )
    line2 = (Line().add_xaxis(year)
             .add_yaxis(series_name='第一产业增长率', y_axis=y_Pri_zzl, is_smooth=True,
                        label_opts=opts.LabelOpts(is_show=False)
                        )
             .add_yaxis(series_name='第二产业增长率', y_axis=y_Sec_zzl, is_smooth=True,
                        label_opts=opts.LabelOpts(is_show=False))
             .add_yaxis(series_name='第三产业增长率', y_axis=y_Ter_zzl, is_smooth=True,
                        label_opts=opts.LabelOpts(is_show=False))
             .set_global_opts(legend_opts=opts.LegendOpts(is_show=True, pos_right='5%'))
             )
    return bar1, line1, bar2, line2


def zx_ym(new_date):
    d = pd.read_csv('owid-covid-data.csv', usecols=['location', 'date', 'total_vaccinations'])
    d['total_vaccinations'] = d['total_vaccinations'].fillna(0)  # 将空格的地方补0
    d = d.values.tolist()
    country = []
    World = []
    Upper_middle_income = []  # 中高收入地区
    Low_income = []
    High_income = []
    Lower_middle_income = []  # 4847244337.0
    for i in new_date:
        for j in range(len(d) - 1):
            if d[j][0] == 'Upper middle income':
                if d[j][1][:7] == i and d[j + 1][1][:7] != i:
                    Upper_middle_income.append(d[j][2])
            elif d[j][0] == 'Low income':
                if d[j][1][:7] == i and d[j + 1][1][:7] != i:
                    Low_income.append(d[j][2])
            elif d[j][0] == 'High income':
                if d[j][1][:7] == i and d[j + 1][1][:7] != i:
                    High_income.append(d[j][2])
            elif d[j][0] == 'Lower middle income':
                if d[j][1][:7] == i and d[j + 1][1][:7] != i:
                    Lower_middle_income.append(d[j][2])
    line = (Line().add_xaxis(new_date)
            .add_yaxis(series_name='低收入国家', y_axis=Low_income, is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False)
                       )
            .add_yaxis(series_name='中低收入国家', y_axis=Lower_middle_income, is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='中高收入国家', y_axis=Upper_middle_income, is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis(series_name='高收入国家', y_axis=High_income, is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='各国疫苗接种情况'),
                             legend_opts=opts.LegendOpts(is_show=True, pos_left='15%'),
                             datazoom_opts=[
                                 opts.DataZoomOpts(
                                     range_start=98, range_end=100)]
                             )
            )
    # line.render('疫苗接种情况.html')
    # os.system('疫苗接种情况.html')
    world_ym = {}
    new_country = []
    location = ['European Union', 'North America', 'South Africa', 'World', 'Africa', 'Upper middle income',
                'Lower middle income',
                'High income', 'Europe', 'South America', 'Asia']
    for i in range(len(d)):
        if d[i][0] not in location:
            new_country.append(d[i][0])
    new_country = list(set(new_country))
    for i in new_country:
        qz = 0
        for j in range(len(d) - 1):  # 获取每个国家接种疫苗总数
            if d[j][0] == i and d[j + 1][0] != i:  #
                qz = d[j][2]
        world_ym[i] = qz
    world_ym = sorted(world_ym.items(), key=lambda e: e[1], reverse=True)
    pie = Pie()  # 或者自定义颜色
    pie.add('疫苗接种情况', world_ym[:10],
            radius=["30%", "50%"]  # 控制内外半径，即图的大小
            )
    pie.set_global_opts(title_opts=opts.TitleOpts(title='疫苗接种总数接种前十'),
                        legend_opts=opts.LegendOpts(is_show=True, pos_left='25%'))
    pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    return line, pie


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
    for i in range(len(d)):
        date.append(d[i][3][:7])
    new_date = list(set(date))
    new_date.sort()
    page = Page(layout=Page.DraggablePageLayout)
    map0 = map(new_date)
    map1, map2 = zx_ym(new_date)
    GDP()
    line = CPI()
    bar1, line1 = price()
    # grid2 = Grid(init_opts=opts.InitOpts(width="1200px",
    #                                      height="700px"))
    # grid2.add(map1, grid_opts=opts.GridOpts(pos_right='55%'))
    # grid2.add(map2, grid_opts=opts.GridOpts(pos_left='80%'))
    # grid2.add(line1, grid_opts=opts.GridOpts(pos_top="60%", pos_left='60%'))
    page.add(map0, map1, map2, line, bar1, line1)
    page.render("中国经济.html")
    os.system("中国经济.html")


#
# economy()
main()
