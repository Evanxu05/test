# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:57:01 2019

@author: lenovo
"""

import wx #导入wxPython库
import wx.adv
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

class Panel(wx.Panel):  

    def __init__(self,parent):  

        wx.Panel.__init__(self,parent=parent, id=-1)  

        pass     

class Frame(wx.Frame):   

    def __init__(self):   

        wx.Frame.__init__(self, parent = None, title = u'量化软件', size=(1000,600), style=wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX)   

        self.DispPanel= Panel(self)

        #创建显示区面板

        self.DispPanel = Panel(self)

        
        self.figure = Figure()

        gs = gridspec.GridSpec(4, 1, left=0.05, bottom=0.10, right=0.96, top=0.96, wspace=None, hspace=0.1, height_ratios=[3.5,1,1,1])

        self.am = self.figure.add_subplot(gs[0,:])

        self.vol = self.figure.add_subplot(gs[1,:])

        self.macd = self.figure.add_subplot(gs[2,:])

        self.devol = self.figure.add_subplot(gs[3,:])

        self.FigureCanvas = FigureCanvas(self, -1, self.figure) #figure加到FigureCanvas

        self.TopBoxSizer = wx.BoxSizer(wx.VERTICAL)

        self.TopBoxSizer.Add(self.FigureCanvas,proportion = -1, border = 2,flag = wx.ALL | wx.EXPAND)

        self.SetSizer(self.TopBoxSizer)
        
        
        
        
        #创建参数区面板

        self.ParaPanel = wx.Panel(self,-1)

        paraInput_Box = wx.StaticBox(self.ParaPanel, -1, u'参数输入') 

        paraInput_Sizer = wx.StaticBoxSizer(paraInput_Box, wx.VERTICAL)        

        Stock_Name_ComboBox = ["浙大网新", "高鸿股份", "天威视讯", "北方导航"]

        stockName_CMBO = wx.ComboBox(self.ParaPanel, -1, "浙大网新", choices = Stock_Name_ComboBox, style = wx.CB_READONLY|wx.CB_DROPDOWN) #股票名称

        stockCode_Text = wx.StaticText(self.ParaPanel, -1, u'股票名称')  

        #日历控件选择数据周期

        #self.dpcEndTime = wx.DatePickerCtrl(self.ParaPanel, -1, style = wx.DP_DROPDOWN|wx.DP_ALLOWNONE)#结束时间

        #self.dpcStartTime = wx.DatePickerCtrl(self.ParaPanel, -1, style = wx.DP_DROPDOWN|wx.DP_SHOWCENTURY|wx.DP_ALLOWNONE)#起始时间
        self.dpcEndTime = wx.adv.DatePickerCtrl(self.ParaPanel, -1,style = wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY|wx.adv.DP_ALLOWNONE)#结束时间
        self.dpcStartTime = wx.adv.DatePickerCtrl(self.ParaPanel, -1,style = wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY|wx.adv.DP_ALLOWNONE)#起始时间


        
        
        
        DateTimeNow = wx.DateTime.Now()#wx.DateTime格式"03/03/18 00:00:00"

        self.dpcEndTime.SetValue(DateTimeNow)

        self.dpcStartTime.SetValue(DateTimeNow)

        stockData_Text = wx.StaticText(self.ParaPanel, -1, u'日期(Start-End)')        
        paraInput_Sizer.Add(stockCode_Text,proportion=0,flag=wx.EXPAND|wx.ALL,border=2)

        paraInput_Sizer.Add(stockName_CMBO, 0, wx.EXPAND|wx.ALL|wx.CENTER, 2)
        paraInput_Sizer.Add(stockData_Text,proportion=0,flag=wx.EXPAND|wx.ALL,border=2)
        paraInput_Sizer.Add(self.dpcStartTime, 0, wx.EXPAND|wx.ALL|wx.CENTER, 2) 
        paraInput_Sizer.Add(self.dpcEndTime, 0, wx.EXPAND|wx.ALL|wx.CENTER, 2)         

        RadioList = ["跳空缺口","金叉\死叉", "N日突破", "均线突破"] 

        self.StratInputBox = wx.RadioBox(self.ParaPanel, -1, label=u'策略选取', choices=RadioList,majorDimension = 4, style = wx.RA_SPECIFY_ROWS)  

        self.TextAInput = wx.TextCtrl(self.ParaPanel, -1, "交易信息提示:", style = wx.TE_MULTILINE|wx.TE_READONLY)#多行|只读 

        vboxnetA = wx.BoxSizer(wx.VERTICAL)#纵向box 
        vboxnetA.Add(paraInput_Sizer,proportion=0,flag=wx.EXPAND|wx.BOTTOM,border=2) #proportion参数控制容器尺寸比例
        vboxnetA.Add(self.StratInputBox,proportion=0,flag=wx.EXPAND|wx.BOTTOM,border=2)         
        vboxnetA.Add(self.TextAInput,proportion=1,flag=wx.EXPAND|wx.ALL,border=2) 

        self.ParaPanel.SetSizer(vboxnetA)
        
        
        
        
        #创建Right面板

        self.CtrlPanel = wx.Panel(self,-1) 

        #创建FlexGridSizer布局网格
        self.FlexGridSizer=wx.FlexGridSizer(rows=3, cols=1, vgap=3, hgap=3)          

        #实盘按钮
        self.Firmoffer = wx.Button(self.CtrlPanel,-1,"实盘")

        #选股按钮
        self.Stockpick = wx.Button(self.CtrlPanel,-1,"选股")  

        #回测按钮  
        self.Backtrace = wx.Button(self.CtrlPanel,-1,"回测") 

        #加入Sizer中  
        self.FlexGridSizer.Add(self.Firmoffer,proportion = 1, border = 5,flag = wx.ALL | wx.EXPAND)  

        self.FlexGridSizer.Add(self.Stockpick,proportion = 1, border = 5,flag = wx.ALL | wx.EXPAND)  

        self.FlexGridSizer.Add(self.Backtrace,proportion = 1, border = 5,flag = wx.ALL | wx.EXPAND) 

        self.FlexGridSizer.SetFlexibleDirection(wx.BOTH)  

        self.CtrlPanel.SetSizer(self.FlexGridSizer)  
        
        
        
        self.HBoxPanel = wx.BoxSizer(wx.HORIZONTAL)

        self.HBoxPanel.Add(self.ParaPanel, proportion = 1, border = 2, flag = wx.EXPAND|wx.ALL) 

        self.HBoxPanel.Add(self.DispPanel, proportion = 4, border = 2, flag = wx.EXPAND|wx.ALL)

        self.HBoxPanel.Add(self.CtrlPanel, proportion = 1, border = 2, flag = wx.EXPAND|wx.ALL) 

        self.SetSizer(self.HBoxPanel)   
        
        pass            

class App(wx.App):

    def OnInit(self):

        self.frame = Frame()  

        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True    

if __name__ == '__main__':   

    app = App()

    app.MainLoop() 

