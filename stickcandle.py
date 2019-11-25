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

from WindPy import *
w.start()

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

df_stockload=w.wsd("002283.SZ", "open,high,low,close,volume", "2019-1-1", "2019-11-25")
df_stockload=pd.DataFrame(df_stockload.Data,index=df_stockload.Fields,columns=df_stockload.Times).T

fig = plt.figure(figsize=(8,6),dpi=100,facecolor='white')
fig.subplots_adjust(left=0.09,bottom=0.20, right=0.94,top=0.90, wspace=0.2, hspace=0)
graph_KAV = fig.add_subplot(1,1,1)
mpf.candlestick2_ochl(graph_KAV, df_stockload.OPEN,df_stockload.CLOSE,df_stockload.HIGH,df_stockload.LOW, width=0.5, colorup='r', colordown='g')
graph_KAV.set_title(u"002283 天润曲轴-日K线")
graph_KAV.set_xlabel(u"日期")
graph_KAV.set_ylabel(u"价格")
graph_KAV.set_xlim(0,len(df_stockload.index)) #设置一下x轴的范围
graph_KAV.set_xticks(range(0,len(df_stockload.index),15))#X轴刻度设定，每15天标一个日期
graph_KAV.grid(True,color='k')
graph_KAV.set_xticklabels([df_stockload.index.strftime('%Y-%m-%d')[index] for index in graph_KAV.get_xticks()])#标签设置为日期

#X轴每个ticker标签都向右倾斜45度 
for label in graph_KAV.xaxis.get_ticklabels():   
    label.set_rotation(45)
    label.set_fontsize(10)#设置标签字号    
	
plt.show()