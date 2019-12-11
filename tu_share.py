# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:05:39 2019

@author: lenovo
"""

import tushare as ts
ts.set_token('fd5caf31a54962a7509e7d4d7972d235dbbc4f0c583003d0ef22d2cf')
pro = ts.pro_api()

df_stockload = pro.daily(ts_code='600580.SH',start_date='20180101',end_date="20191122")
df = ts.pro_bar(ts_code='600580.SH',start_date='20190701', end_date='20191122', freq="60min",ma=[8, 16, 32])
