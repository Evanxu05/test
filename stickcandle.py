# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mpl_finance as mpf
from datetime import datetime
import pandas as pd

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
font = FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')



df_stockload = ts.pro_bar(ts_code='600580.SH',start_date='20191025', end_date='20191122', freq="5min",ma=[5, 10, 24,48,120,240])
df_stockload = df_stockload.sort_index(ascending=False)

fig = plt.figure(figsize=(8,6),dpi=100,facecolor='white')
fig.subplots_adjust(left=0.09,bottom=0.20, right=0.94,top=0.90, wspace=0.2, hspace=0)
graph_KAV = fig.add_subplot(1,1,1)
mpf.candlestick2_ochl(graph_KAV, df_stockload.open,df_stockload.close,df_stockload.high,df_stockload.low, width=0.5, colorup='r', colordown='g')
graph_KAV.set_title("600580 卧龙电驱-5M线")
graph_KAV.set_xlabel("日期")
graph_KAV.set_ylabel("价格")
graph_KAV.set_xlim(0,len(df_stockload.index)) #设置一下x轴的范围
graph_KAV.set_xticks(range(0,len(df_stockload.index),45))#X轴刻度设定，每15天标一个日期

graph_KAV.set_xticklabels([df_stockload.index.strftime('%Y-%m-%d')[index] for index in graph_KAV.get_xticks()])#标签设置为日期

#X轴每个ticker标签都向右倾斜45度 
for label in graph_KAV.xaxis.get_ticklabels():   
    label.set_rotation(45)
    label.set_fontsize(10)#设置标签字号    
	
plt.show()