import wx

class OptionsScreen(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sizer = wx.BoxSizer(wx.VERTICAL)
        header_font = wx.Font(self.FromDIP(30), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        welcome_text = wx.StaticText(self, label="Options")
        welcome_text.SetFont(header_font)
        sizer.Add(welcome_text, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=self.FromDIP(30))
        self.SetSizer(sizer)