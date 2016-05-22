# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun  5 2014)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class BaseFrame
###########################################################################


class BaseFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="ParallelHash", pos=wx.DefaultPosition,
                          size=wx.Size(450, 450), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(450, 450), wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Hash file"), wx.VERTICAL)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl_hashfile = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_textCtrl_hashfile, 1, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.TOP, 5)

        self.m_button_findhashfile = wx.Button(
            self, wx.ID_ANY, "...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        bSizer6.Add(self.m_button_findhashfile, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 5)

        sbSizer1.Add(bSizer6, 1, wx.EXPAND, 0)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_radioBtn_hash = wx.RadioButton(self, wx.ID_ANY, "Hash", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        self.m_radioBtn_hash.SetValue(True)
        bSizer7.Add(self.m_radioBtn_hash, 0, wx.ALL, 5)

        self.m_radioBtn_verify = wx.RadioButton(self, wx.ID_ANY, "Verify", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_radioBtn_verify, 0, wx.ALL, 5)

        self.m_radioBtn_compare = wx.RadioButton(self, wx.ID_ANY, "Compare", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_radioBtn_compare, 0, wx.ALL, 5)

        bSizer9.Add(bSizer7, 0, wx.EXPAND, 0)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_radio_md5 = wx.RadioButton(self, wx.ID_ANY, "md5", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        self.m_radio_md5.SetValue(True)
        bSizer8.Add(self.m_radio_md5, 0, wx.ALL, 5)

        self.m_radio_sha1 = wx.RadioButton(self, wx.ID_ANY, "sha1", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_radio_sha1, 0, wx.ALL, 5)

        self.m_radio_sha256 = wx.RadioButton(self, wx.ID_ANY, "sha256", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_radio_sha256, 0, wx.ALL, 5)

        self.m_radio_sha512 = wx.RadioButton(self, wx.ID_ANY, "sha512", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_radio_sha512, 0, wx.ALL, 5)

        bSizer9.Add(bSizer8, 0, wx.EXPAND, 0)

        fgSizer2.Add(bSizer9, 1, wx.EXPAND, 0)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, "Processes", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer12.Add(self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_spinCtrl_processes = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString,
                                                wx.DefaultPosition, wx.Size(50, -1), wx.SP_ARROW_KEYS, 0, 1024, 0)
        bSizer12.Add(self.m_spinCtrl_processes, 0, 0, 5)

        bSizer11.Add(bSizer12, 1, wx.ALIGN_RIGHT, 5)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, "0 = all available", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        self.m_staticText31.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.m_staticText31.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        bSizer11.Add(self.m_staticText31, 0, wx.LEFT | wx.ALIGN_RIGHT, 5)

        fgSizer2.Add(bSizer11, 1, wx.ALL | wx.ALIGN_RIGHT, 5)

        sbSizer1.Add(fgSizer2, 0, wx.EXPAND, 5)

        bSizer2.Add(sbSizer1, 0, wx.EXPAND, 5)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl_folder = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                             wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        bSizer1.Add(self.m_textCtrl_folder, 1, wx.ALL | wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_button_addfile = wx.Button(self, wx.ID_ANY, "File", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        bSizer10.Add(self.m_button_addfile, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.ALL, 5)

        self.m_button_addfolder = wx.Button(self, wx.ID_ANY, "Folder",
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT)
        bSizer10.Add(self.m_button_addfolder, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        bSizer1.Add(bSizer10, 0, 0, 5)

        bSizer2.Add(bSizer1, 0, wx.EXPAND, 5)

        self.m_listCtrl_results = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST)
        bSizer2.Add(self.m_listCtrl_results, 1, wx.ALL | wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_gauge1 = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.m_gauge1.SetValue(0)
        bSizer4.Add(self.m_gauge1, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_button_go = wx.Button(self, wx.ID_ANY, "Go", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button_go, 0, wx.ALL, 5)

        bSizer2.Add(bSizer4, 0, wx.EXPAND, 5)

        self.m_staticText_status = wx.StaticText(self, wx.ID_ANY, "Status:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_status.Wrap(-1)
        self.m_staticText_status.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        bSizer2.Add(self.m_staticText_status, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button_findhashfile.Bind(wx.EVT_BUTTON, self.signal_findhashfile)
        self.m_radioBtn_hash.Bind(wx.EVT_RADIOBUTTON, self.signal_btn_hash)
        self.m_radioBtn_verify.Bind(wx.EVT_RADIOBUTTON, self.signal_btn_verify)
        self.m_radioBtn_compare.Bind(wx.EVT_RADIOBUTTON, self.signal_btn_compare)
        self.m_button_addfile.Bind(wx.EVT_BUTTON, self.signal_addfile)
        self.m_button_addfolder.Bind(wx.EVT_BUTTON, self.signal_addfolder)
        self.m_button_go.Bind(wx.EVT_BUTTON, self.signal_go)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def signal_findhashfile(self, event):
        event.Skip()

    def signal_btn_hash(self, event):
        event.Skip()

    def signal_btn_verify(self, event):
        event.Skip()

    def signal_btn_compare(self, event):
        event.Skip()

    def signal_addfile(self, event):
        event.Skip()

    def signal_addfolder(self, event):
        event.Skip()

    def signal_go(self, event):
        event.Skip()
