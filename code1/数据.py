import codecs
import csv
import matplotlib.pyplot as plt
from pyecharts.charts import Line,Page
import pyecharts.options as opts
import os
num1=[]
newmap_name=[]
with codecs.open('D:\综合课程设计三\owid-covid-data.csv', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f, skipinitialspace=True):
        num=[]
        '''for j in row:
            #print(j)
            if j=='continent' or :
                num.append(row[j])'''
        num.append(row['continent'])
        num.append(row['location'])
        '''if row['location'] not in newmap_name:
            newmap_name.append(row['location'])'''
        num.append(row['date'])
        num.append(row['total_cases'])
        if row['new_cases']=='':
            num.append(0)
        else:
            num.append(row['new_cases'])
        #if
        num.append(row['total_deaths'])
        if row['new_deaths']=='':
            num.append(0)
        else:
            num.append(row['new_deaths'])
        num1.append(num)
#print(len(newmap_name))
list1=[]
for i in num1:
    #if 'World' in i[1] :
    if 'China' in i[1]:
        #print(i[2][:-3],i[3])
         list1.append([i[2][:-3],i[3],i[4],i[5],i[6]])
num=[]
x=[]
y=[]
y1=[]
x.append(list1[0][0])
y.append(list1[0][1])
y1.append(list1[0][2])
d=[]
d1=[]
d.append(list1[0][3])
d1.append(list1[0][4])
num.append(list1[0])
for i in list1:
    if i[0]==num[-1][0]:
        num[-1][1]=i[1]
        y[-1]=int(float(i[1]))
        d[-1]=int(float(i[3]))
        y1[-1]=int(float(y1[-1]))+int(float(i[2]))
        d1[-1]=int(float(d1[-1]))+int(float(i[4]))
    else:
        num.append(i)
        x.append(i[0])
        y.append(int(float(i[1])))
        y1.append(int(float(i[2])))
        d.append(int(float(i[3])))
        d1.append(int(float(i[4])))
# 定义一个Line_charts函数
def Line_charts():
    c = Line()
    c.add_xaxis(xaxis_data=x)
    c.add_yaxis(series_name='确诊新冠总人数',y_axis=y)
    c.add_yaxis(series_name='该月新增人数', y_axis=y1)
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    data_zoom = {
        "show": False,
        "title": {"zoom": "data zoom", "back": "data zoom restore"}
    }
    c.set_global_opts(
        # 设置标题
        title_opts=opts.TitleOpts(title="全国新冠疫情确诊人数变化"),
        # 设置图例is_show=False是不显示图例
        legend_opts=opts.LegendOpts(is_show=True),
        # 设置提示项
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
        # 工具箱的设置
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(data_zoom=data_zoom))

    )
    return c
def Line_charts1():
    c1= Line()
    c1.add_xaxis(xaxis_data=x)
    c1.add_yaxis(series_name='死亡总人数',y_axis=d)
    c1.add_yaxis(series_name='该月死亡新增人数', y_axis=d1)
    c1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    data_zoom = {
        "show": False,
        "title": {"zoom": "data zoom", "back": "data zoom restore"}
    }
    c1.set_global_opts(
        # 设置标题
        title_opts=opts.TitleOpts(title="全国新冠疫情死亡人数变化"),
        # 设置图例is_show=False是不显示图例
        legend_opts=opts.LegendOpts(is_show=True),
        # 设置提示项
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
        # 工具箱的设置
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(data_zoom=data_zoom))

    )
    return c1
# 绘制图表
c = Line_charts()
c1=Line_charts1()
page=Page(layout=Page.DraggablePageLayout)
page.add(c,c1)
page.render('全国疫情情况统计.html')
os.system('全国疫情情况统计.html')
'''
c.render("全球新冠疫情统计.html")
c1.render("全球死亡人数.html")
os.system("全球死亡人数.html")
os.system("全球新冠疫情统计.html")'''