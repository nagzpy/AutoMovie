import wx
from OptionsScreen import OptionsScreen

class App(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, size=(800, 600))
        self.book = wx.Simplebook(self)
        panel = wx.Panel(self.book)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        self.book.AddPage(panel, "Home")
        self.options_screen = OptionsScreen(self.book)
        self.book.AddPage(self.options_screen, "Options")
        header_font = wx.Font(panel.FromDIP(30), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        welcome_text = wx.StaticText(panel, label="To begin import your photos")
        welcome_text.SetFont(header_font)
        sizer.Add(welcome_text, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=panel.FromDIP(30))
        upload_icon = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, size=(100, 100))
        upload_button = wx.BitmapButton(panel, bitmap=upload_icon)
        sizer.Add(upload_button, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=panel.FromDIP(50))
        upload_button.Bind(wx.EVT_BUTTON, self.upload_button_clicked)

    def upload_button_clicked(self, event):
        wildcard = "Select only image files (.jpg, .jpeg, .heic, .png)|*.jpg;*.jpeg;*.heic;*.png"
        with wx.FileDialog(self, "Upload Files",
                            wildcard=wildcard,
                           style=wx.FD_FILE_MUST_EXIST | wx.FD_OPEN | wx.FD_MULTIPLE) as file_dialog:
            file_dialog.ShowModal()
            self.paths = file_dialog.GetPaths()
            file_dialog.Destroy()
        self.book.ChangeSelection(self.book.FindPage(self.options_screen))

app = wx.App()
fr = App(parent=None, title="AutoMovie")
fr.Show()
app.MainLoop()
