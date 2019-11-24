# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from WindPy import *
import pandas as pd
w.start()

df_stockload=w.wsd('000016.SH','open,high,low,close,pre_close,volume','2017-1-1','2019-11-22')
df_stockload=pd.DataFrame(df_stockload.Data,index=df_stockload.Fields,columns=df_stockload.Times).T

df_stockload.CLOSE.plot(c='b')
df_stockload.CLOSE.rolling(window=30).mean().plot(c='r')
df_stockload.CLOSE.rolling(window=60).mean().plot(c='g')
plot.show()
