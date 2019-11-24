#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:42:29 2019

@author: xuyuanwu
"""
import pandas_datareader.data as web
from datetime import datetime
start=datetime(year=2017,
               month=1,
               day=1)

today= datetime.now()

df_stockload = web.DataReader('000001.SS','yahoo',start,today)

df_stockload.Close.plot(c='b')
df_stockload.Close.rolling(window=30).mean().plot(c='g')
df_stockload.Close.rolling(window=60).mean().plot(c='r')
plot.show()