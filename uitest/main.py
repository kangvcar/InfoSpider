#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)

        panel.SetBackgroundColour('#4f5049')
        vbox = wx.BoxSizer(wx.VERTICAL)

        midPan = wx.Panel(panel)
        midPan.SetBackgroundColour('#ededed')

        vbox.Add(midPan, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(vbox)


def main():

    app = wx.App()
    ex = Example(None, title='Border')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()