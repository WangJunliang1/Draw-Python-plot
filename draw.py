# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import seaborn as sns

#%% 从Excel中抽取数据

x_name = "QP num"
y_name = "Throuthput"

df = pd.read_excel("ch2图表.xlsx", sheet_name=0, header=None, 
                   names=[x_name, y_name], skiprows=[0, 1], usecols=[0, 1])
x_line = df[x_name]
y_line = df[y_name]

#%% 绘制图形
style_d = [y_name,]
sns.lineplot(x=x_line, y=y_line, marker="o", color='black', 
             markersize=8, 
             # markerfacecolor='none', markeredgecolor='black', 
             linewidth=1).set(
                 xlabel='Number of QPs', ylabel='Throuthput (Gb/s)')
sns.set_theme(style='ticks', font_scale=1.1)
# sns.set_style('ticks')
# sns.despine()   #移除上、右边框


