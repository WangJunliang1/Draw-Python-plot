# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#%% 从Excel中抽取数据

# 抽取QP数-吞吐信息------------
x_name = "QP num"
y_name = "Throuthput"
df = pd.read_excel("ch2图表.xlsx", sheet_name=0, header=None, 
                   names=[x_name, y_name], skiprows=[0, 1], usecols=[0, 1])
x_line = df[x_name]
y_line = df[y_name]

# 抽取节点数-丢包率信息-------------
x1_name = "Server num"
y1_name = "Loss rate"
df1 = pd.read_excel("ch2图表.xlsx", sheet_name=1, header=None, 
                   names=[x1_name, y1_name], skiprows=[0, 1], usecols=[0, 1])
x1_line = df1[x1_name]
y1_line = df1[y1_name]

# 抽取中文期刊的最后图信息-------------
x2_name = "Server num"
df2 = pd.read_excel("ch2图表.xlsx", sheet_name=2, header=None, 
                   names=[x2_name, "XRC", "DCT", "ERD"], 
                   skiprows=[0, 1], usecols=[0, 1, 2, 3])
# 转换表格为一列并用原列名分类，以方便使用hue绘图
dfm = df2.melt(x2_name, var_name='QP methods', value_name='puts')

#%% 绘制QP数-NIC性能图形\
    
def Draw_first():
    sns.lineplot(x=x_line, y=y_line, marker="o", color='black', 
                 markersize=9, 
                 # markerfacecolor='none', markeredgecolor='black', 
                 linewidth=1).set(
                     xlabel='Number of QPs on NIC', ylabel='NIC Throuthput (Gb/s)')
    sns.set_theme(style='ticks', font_scale=1.2)
        
    # sns.despine()   #移除上、右边框
    
    # 保存图片为EPS格式
    plt.savefig("Plot-output1.eps", dpi=600)
    plt.show()
    
    # 防止图片覆盖
    plt.close()

#%% 绘制节点数-网络丢包率图形

def Draw_Second():
    sns.lineplot(x=x1_line, y=y1_line, marker="^", color='black', 
                 markersize=9, 
                 # markerfacecolor='none', markeredgecolor='black', 
                 linewidth=1).set(
                     xlabel='Number of Servers in Cluster', ylabel='Loss Rate')
    
    #设置为对数轴显示
    plt.yscale('log')   
    
    # 设置x轴刻度频率
    plt.xticks(ticks=np.arange(0, max(x1_line)+1, 5000))
    
    sns.set_theme(style='ticks', font_scale=1.2)

    # sns.despine()   #移除上、右边框
    
    # 保存图片为EPS格式
    plt.savefig("Plot-output2.eps", dpi=600)
    plt.show()
    
    # 防止图片覆盖
    plt.close()

#%% 绘制ERD XRC DCT 吞吐性能图形
    
def Draw_third():
    # 设置字体为times new roman
    plt.rcParams['font.family'] = 'Times New Roman'
    # 开始绘图 
    sns.lineplot(x=dfm[x2_name], y=dfm['puts'], hue=dfm['QP methods'], 
                 style=dfm['QP methods'],
                 markers=["o", "*", "^"], 
                 size=dfm['QP methods'], sizes=[0.6, 1.2, 2.5], 
                 markersize=9, 
                 # markerfacecolor='none', markeredgecolor='black', 
                 linewidth=1).set(
                     xlabel='Number of servers in cluster', ylabel='NIC Throuthput (Gb/s)')
    sns.set_theme(style='ticks', font_scale=1.1)
        
    # sns.despine()   #移除上、右边框
    
    # x改为log刻度
    # plt.xscale('log')
    # plt.xticks(ticks=np.logspace(0, max(df2[x2_name])+1, 5))


    # 保存图片为EPS格式
    plt.savefig("CNjournal-erd.png", dpi=600)
    plt.show()
    
    # 防止图片覆盖
    plt.close()

#%% main入口

if __name__ == "__main__":
    Draw_first()
    Draw_Second()
    Draw_third()
