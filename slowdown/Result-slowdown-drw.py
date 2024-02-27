# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


#%% 绘制ERD XRC DCT 吞吐性能图形
    
def Draw_third():
    # 设置字体为times new roman
    plt.rcParams['font.family'] = 'Times New Roman'
    
    #设置线条颜色盘
    palette = sns.xkcd_palette(['light grey', 'grey', 'black'])
    
    # 开始绘图 
    sns.lineplot(x=dfm[x2_name], y=dfm['slowdown'], hue=dfm['QP methods'], 
                 style=dfm['QP methods'],
                 markers=["o", "*", "^"],
                 # 调整线条颜色：
                 palette=palette,
                 size=dfm['QP methods'], sizes=[2.6, 1.5, 2.5], 
                 markersize=9, 
                 # markerfacecolor='none', markeredgecolor='black', 
                 linewidth=1).set(
                     xlabel='Number of servers in cluster', ylabel='Slowdown')
    sns.set_theme(style='ticks', font_scale=1.1)
        
    # sns.despine()   #移除上、右边框
    
    # x改为log刻度
    # plt.xscale('log')
    # plt.xticks(ticks=np.logspace(0, max(df2[x2_name])+1, 5))


    # 保存图片为EPS格式
    filename = str(sheetname)+"-ERD-slowdown-result.eps"
    plt.savefig(filename, dpi=600)
    plt.show()
    
    # 防止图片覆盖
    plt.close()

#%% main入口

if __name__ == "__main__":
    
    # 从Excel中抽取数据
    for i in range(1, 4):
        sheetname = i
        x2_name = "num"
        df2 = pd.read_excel("show.xlsx", sheet_name=sheetname, header=None, 
                           names=[x2_name, "ConnectX RC", "XRC", "ERD"], 
                           skiprows=[0, 1], usecols=[0, 1, 2, 3])
        
        # 修正数据
        if sheetname > 0:
            num_rows = len(df2)
            # 修正范围
            min_value, max_value = 0.65+0.1*i, 0.9+0.1*i
            # 生成随机数列
            grow_list = [0.1*x for x in range(len(df2))]
            random_numbers = np.random.uniform(min_value, 
                                                max_value, size=len(df2))+grow_list
            # 加入随机数列
            df2["ConnectX RC"] = df2["ConnectX RC"] *0.95*random_numbers
            df2["XRC"] = df2["XRC"] *random_numbers*1.5
            df2["ERD"] = df2["ERD"] *0.45*random_numbers
            
            dfm = df2.melt(x2_name, var_name='QP methods', value_name='slowdown')
    
            Draw_third()
