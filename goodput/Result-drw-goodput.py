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
    palette = sns.xkcd_palette(['grey', 'black', 'slate'])
    
    # 开始绘图 
    # sns.set(font_scale=1.1)
    
    sns.lineplot(x=dfm["loss rate"], y=dfm['Goodput'], hue=dfm['Transmission path number'], 
                 style=dfm['Transmission path number'],
                 markers=["s", "o", "d"],
                 # 调整线条颜色：
                 palette=palette,
                 size=dfm['Transmission path number'], sizes=[1.5, 1.5, 2.5], 
                 markersize=7, 
                 # markerfacecolor='none', markeredgecolor='black', 
                 linewidth=1).set(
                     xlabel='Loss rate in cluster', ylabel='Goodput (Gbps)')
    sns.set_theme(style='ticks', font_scale=1.2)
        
    # sns.despine()   #移除上、右边框
    
    # x改为log刻度
    plt.xscale('log')
    # plt.xticks(ticks=np.logspace(0, max(df2[x2_name])+1, 5))


    # 保存图片为EPS格式
    filename = str(i)+"ERD-goodput-result.eps"
    plt.savefig(filename, dpi=600, bbox_inches = 'tight') #设置bbox防止显示不全
    plt.show()
    
    # 防止图片覆盖
    plt.close()

#%% main入口

if __name__ == "__main__":
    
    #%% 从Excel中抽取数据
    show_num = [8, 48, 64] # 8, 48, 64
    for i in show_num:
        show_file = "show-"+str(i)+".xlsx"
        df2 = pd.read_excel(show_file, sheet_name=1, header=None, 
                           names=["loss rate", "Path num = 2", "Path num = 4", "Path num = 6"], 
                           skiprows=[0, 1], 
                           usecols=[0, 1, 2, 3])
        
        # # 增加“loss rate”x轴列
        # min_num, max_num = 160, 1280
        # new_column = np.linspace(min_num, max_num+1, len(df2))
        # df2.insert(0, 'num', new_column)
        
        # # 修正数据--随机缩小一定比率
        # num_rows = len(df2)
        # min_value, max_value = 0.85-0.02*i, 0.9-0.02*i
        # # 生成随机数列
        # random_numbers = np.random.uniform(min_value, 
        #                                     max_value, size=len(df2))
        # # 加入随机数列
        # df2["XRC"] = df2["XRC"] *random_numbers
        
        # 转换表格为一列并用原列名分类，以方便使用hue绘图
        dfm = df2.melt("loss rate", var_name='Transmission path number', value_name='Goodput')
        
                
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
    
    
