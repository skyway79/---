import codecs
import csv
import matplotlib.pyplot as plt
from pyecharts.charts import Line,Page
import pyecharts.options as opts
import pandas as pd
import os
num1=[]
newmap_name=[]
#data=pd.read_csv("D:\综合课程设计三\gmjj\PPI.csv",usecols=['Month','Curent_Month','Curent_Month_YOY'])
#print(data)
with codecs.open('D:\综合课程设计三\gmjj\PPI.csv', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f, skipinitialspace=True):
        num = []
        a=row['Month']
        #num.append(a[:4])
        num.append(a)
        num.append(row['Curent_Month'])
        num.append(row['Curent_Month_YOY'])
        if row['Total']=='':
            num.append(0)
        else:
            num.append(row['Total'])
        num1.append(num)
x=[]
y1=[]
y2=[]
y3=[]
for i in range(0,36):
    x.append(num1[i][0])
    y1.append(num1[i][2][:-2])
    y2.append(num1[i][3])
    #y3.append(num1[i][4])
x.reverse()
y1.reverse()
y2.reverse()
y3.reverse()
def Line_charts():
    c = Line()
    c.add_xaxis(xaxis_data=x)
    c.add_yaxis(series_name='当月出口价格',y_axis=y1,is_smooth=True)
    c.add_yaxis(series_name='当月同比增长', y_axis=y2,is_smooth=True)
    #c.add_yaxis(series_name='累计', y_axis=y3)
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    data_zoom = {
        "show": False,
        "title": {"zoom": "data zoom", "back": "data zoom restore"}
    }
    c.set_global_opts(
        # 设置标题
        title_opts=opts.TitleOpts(title="中国工业品出口价格"),
        # 设置图例is_show=False是不显示图例
        legend_opts=opts.LegendOpts(is_show=True),
        # 设置提示项
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
        # 工具箱的设置
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(data_zoom=data_zoom))

    )
    return c
arr=[]
with codecs.open('D:\综合课程设计三\gmjj\CPGI.csv', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f, skipinitialspace=True):
        num = []
        a=row['Month']
        #num.append(a[:4])
        num.append(a)
        num.append(row['CPGI'])#2
        num.append(row['CPGI_YOY'])
        num.append(row['CPGI_Comparative'])
        num.append(row['Agricultural_Products_Index'])
        num.append(row['API_YOY'])
        num.append(row['API_Comparative'])
        num.append(row['Mineral_Products_Index'])
        num.append(row['MPI_YOY'])
        num.append(row['MPI_Comparative'])
        num.append(row['Kerosene_Power_Index'])
        num.append(row['KPI_YOY'])
        num.append(row['KPI_Comparative'])
        arr.append(num)
x1=[]
yy1=[]
yy2=[]
yy3=[]
ln1=[]
ln2=[]#农产品
ck1=[]#矿产品
ck2=[]
sy1=[]#石油产品
sy2=[]
for i in range(0,50):
    x1.append(arr[i][0])
    yy1.append(arr[i][1])
    #print(arr[i][1])
    yy2.append(arr[i][2][:-2])
    yy3.append(arr[i][3][:-2])
    ln1.append(arr[i][4])
    ln2.append(arr[i][6][:-2])
    ck1.append(arr[i][7])
    ck2.append(arr[i][9][:-2])
    sy1.append(arr[i][10])
    sy2.append(arr[i][12][:-2])
x1.reverse()
yy1.reverse()
yy2.reverse()
yy3.reverse()
ln1.reverse()
ln2.reverse()
ck1.reverse()
ck2.reverse()
sy1.reverse()
sy2.reverse()
def Line_charts1():
    c = Line()
    c.add_xaxis(xaxis_data=x1)
    c.add_yaxis(series_name='总指数',y_axis=yy1,is_smooth=True)
    c.add_yaxis(series_name='当月同比增长', y_axis=yy2,is_smooth=True)
    c.add_yaxis(series_name='当月环比增长', y_axis=yy3,is_smooth=True)
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    data_zoom = {
        "show": False,
        "title": {"zoom": "data zoom", "back": "data zoom restore"}
    }
    c.set_global_opts(
        # 设置标题
        title_opts=opts.TitleOpts(title="中国企业商品价格指数"),
        # 设置图例is_show=False是不显示图例
        legend_opts=opts.LegendOpts(is_show=True),
        # 设置提示项
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
        # 工具箱的设置
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(data_zoom=data_zoom))

    )
    return c
def Line_charts2():
    c = Line()
    c.add_xaxis(xaxis_data=x1)
    c.add_yaxis(series_name='总指数',y_axis=yy1,is_smooth=True)
    c.add_yaxis(series_name='农产品指数',y_axis=ln1,is_smooth=True)
    c.add_yaxis(series_name='农产品当月环比增长', y_axis=ln2,is_smooth=True)
    c.add_yaxis(series_name='矿产品指数', y_axis=ck1,is_smooth=True)
    c.add_yaxis(series_name='矿产品当月环比增长', y_axis=ck2,is_smooth=True)
    c.add_yaxis(series_name='煤油产品指数', y_axis=sy1,is_smooth=True)
    c.add_yaxis(series_name='煤油产品当月环比增长', y_axis=sy2,is_smooth=True)
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    data_zoom = {
        "show": False,
        "title": {"zoom": "data zoom", "back": "data zoom restore"}
    }
    c.set_global_opts(
        # 设置标题
        title_opts=opts.TitleOpts(title="中国企业各个商品价格指数"),
        # 设置图例is_show=False是不显示图例
        legend_opts=opts.LegendOpts(is_show=True),
        # 设置提示项
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
        # 工具箱的设置
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(data_zoom=data_zoom))

    )
    return c
jin=[]
with codecs.open('D:\综合课程设计三\gmjj\Import_Export.csv', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f, skipinitialspace=True):
        num=[]
        num.append(row['Month'])
        num.append(row['Current_Export'])
        num.append(row['Current_Import'])
        num.append(row['Total_Export'])
        num.append(row['Total_Import'])
        jin.append(num)
x3=[]
z1=[]
z2=[]
z3=[]
z4=[]
for i in range(0,40):
    x3.append(jin[i][0])
    z1.append(jin[i][1])
    z2.append(jin[i][2])
    z3.append(jin[i][3])
    z4.append(jin[i][4])
#print(x3)
x3.reverse()
z1.reverse()
z2.reverse()
z3.reverse()
z4.reverse()
def Line_charts3():
    c = Line()
    c.add_xaxis(xaxis_data=x3)
    c.add_yaxis(series_name='当月出口额',y_axis=z1,is_smooth=True)
    c.add_yaxis(series_name='当月进口额',y_axis=z2,is_smooth=True)
    c.add_yaxis(series_name='累计出口额', y_axis=z3,is_smooth=True)
    c.add_yaxis(series_name='累计进口额', y_axis=z4,is_smooth=True)
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    data_zoom = {
        "show": False,
        "title": {"zoom": "data zoom", "back": "data zoom restore"}
    }
    c.set_global_opts(
        # 设置标题
        title_opts=opts.TitleOpts(title="中国海关进出口额"),
        # 设置图例is_show=False是不显示图例
        legend_opts=opts.LegendOpts(is_show=True),
        # 设置提示项
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
        # 工具箱的设置
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(data_zoom=data_zoom))

    )
    return c
c = Line_charts()
c1=Line_charts1()
c2=Line_charts2()
c3=Line_charts3()
page=Page(layout=Page.DraggablePageLayout)
page.add(c,c3,c1,c2)
page.render("经济分析.html")
os.system("经济分析.html")
