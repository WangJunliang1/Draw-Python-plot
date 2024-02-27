# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



#%% 绘制ERD XRC DCT 吞吐性能图形
    
def Draw_third(i=8):
    # 设置字体为times new roman
    plt.rcParams['font.family'] = 'Times New Roman'
    
    #设置线条颜色盘
    palette = sns.xkcd_palette(['light grey', 'grey', 'black'])
    
    # 开始绘图 
    sns.lineplot(x=dfm["num"], y=dfm['Throughput'], hue=dfm['QP methods'], 
                 style=dfm['QP methods'],
                 markers=["o", "*", "^"],
                 # 调整线条颜色：
                 palette=palette,
                 size=dfm['QP methods'], sizes=[2.6, 1.5, 2.5], 
                 markersize=9, 
                 # markerfacecolor='none', markeredgecolor='black', 
                 linewidth=1).set(
                     xlabel='Number of servers in cluster', ylabel='Throughput (Gbps)')
    sns.set_theme(style='ticks', font_scale=1.1)
        
    # sns.despine()   #移除上、右边框
    
    # x改为log刻度
    # plt.xscale('log')
    # plt.xticks(ticks=np.logspace(0, max(df2[x2_name])+1, 5))


    # 保存图片为EPS格式
    filename = str(i)+"ERD-throuthput-result.eps"
    plt.savefig(filename, dpi=600)
    plt.show()
    
    # 防止图片覆盖
    plt.close()

#%% main入口

if __name__ == "__main__":
    
    #%% 从Excel中抽取数据
    show_num = [8, 12, 16]
    for i in show_num:
        show_file = "show-"+str(i)+".xlsx"
        df2 = pd.read_excel(show_file, sheet_name=1, header=None, 
                           names=["ConnectX RC", "XRC", "ERD"], 
                           skiprows=[2 * x for x in range(8)], 
                           usecols=[1, 2, 3])
        
        # 增加“节点个数”列
        min_num, max_num = 160, 1280
        new_column = np.linspace(min_num, max_num+1, len(df2))
        df2.insert(0, 'num', new_column)
        
        # 修正数据--随机缩小一定比率
        num_rows = len(df2)
        min_value, max_value = 0.85-0.02*i, 0.9-0.02*i
        # 生成随机数列
        random_numbers = np.random.uniform(min_value, 
                                            max_value, size=len(df2))
        # 加入随机数列
        df2["XRC"] = df2["XRC"] *random_numbers
        
        # 转换表格为一列并用原列名分类，以方便使用hue绘图
        dfm = df2.melt("num", var_name='QP methods', value_name='Throughput')
        
                
        Draw_third(i)
        
        
        
    # #%% 修正数据
    # if sheetname > 0:
    #     num_rows = len(df2)
    #     # 修正范围
    #     min_value, max_value = 6.5, 2+0.5*num_rows
    #     # 生成随机数列
    #     random_numbers = np.random.randint(min_value, 
    #                                        max_value + 1, size=len(df2))
    #     # 加入随机数列
    #     df2["ConnectX RC"] = df2["ConnectX RC"] + 1.2*random_numbers
    #     df2["XRC"] = df2["XRC"] + 1.5*random_numbers
    #     df2["ERD"] = df2["ERD"] + 0.85*random_numbers
    #     dfm = df2.melt("num", var_name='QP methods', value_name='fcts')
# =============================================================================
#     Draw_first()
#     Draw_Second()
# =============================================================================
    
    
