import wx 

class App(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, size=(800,600))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        header_font = wx.Font(panel.FromDIP(30), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        welcome_text = wx.StaticText(panel, label="To begin import your photos")
        welcome_text.SetFont(header_font)
        sizer.Add(welcome_text, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=panel.FromDIP(30))
        upload_icon = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, size=(100,100))
        upload_button = wx.BitmapButton(panel, bitmap=upload_icon)
        sizer.Add(upload_button, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=panel.FromDIP(50))
        self.Bind(wx.EVT_BUTTON, self.upload_button_clicked, upload_button)
    def upload_button_clicked(self, event):
        with wx.FileDialog(self, "Upload Files",style=wx.FD_FILE_MUST_EXIST | wx.FD_OPEN | wx.FD_MULTIPLE) as file_dialog:
            file_dialog.ShowModal()
            print(file_dialog.GetPaths())
            file_dialog.Destroy()
app = wx.App()
fr = App(parent=None, title="AutoMovie")
fr.Show()
app.MainLoop()