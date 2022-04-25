#!/usr/bin/env python
import wx, wx.adv

class mainWindow(wx.Frame):

    def __init__(self, *args, **kw):
        super(mainWindow, self).__init__(*args, **kw)
        self.SetTitle("RW modmaker!")
        self.SetName("MainWindow")
        self.SetSize(800, 600)
        self.Centre()
        
        self.LoadToolbar()
        self.Show()
        
        self.LoadUi()

    def LoadToolbar(self):
        self.menubar = wx.MenuBar()
        self.menus = {
            'project': wx.Menu(),
            'about': wx.Menu(),
            'func': {}
        }
        def newMenu(name: str='', size:wx.Size = wx.Size(120,60)):
            menu = wx.Dialog(self, -1, name, wx.DefaultPosition, wx.Size(400,400), 0, name)
            menu.pnl = wx.Panel(menu)
            menu.pnl.SetSize(menu.Size)
            # menu.box = wx.BoxSizer(wx.HORIZONTAL)
            # menu.box.Add(wx.StaticText(menu, -1, "New Project...", wx.DefaultPosition, wx.Size(size.x, size.y)), 0, 0, 0)
            # menu.box.Add(wx.Button(menu.box, wx.ID_OK, 'Submit'))
            menu.submit = wx.Button(menu.pnl, wx.ID_OK, 'submit', wx.Point(0,0), wx.Size(80, 20))

            if menu.ShowWindowModal() == wx.ID_OK:
                del menu
            else:
                del menu
        def openFileMenu(name: str=''):
            with wx.FileDialog(self, name, wildcard="README.*",
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return     # the user changed their mind

                # Proceed loading the file chosen by the user
                pathname = fileDialog.GetPath()
                try:
                    with open(pathname, 'r') as file:
                        self.doLoadDataOrWhatever(file)
                except IOError:
                    wx.LogError("Cannot open file '%s'.")

        self.menus['project'].Append(10, 'New', "Create new mod!",kind=wx.ITEM_NORMAL)
        self.menus['func'][10] = lambda: newMenu("ModInfo")
        self.menus['project'].Append(11, 'Open', "Open a existing mod!")
        self.menus['func'][11] = lambda: openFileMenu('Open')
        self.menus['project'].Append(12, 'Quit\tCTRL+Q',kind=wx.ITEM_NORMAL)
        self.menus['func'][12] = lambda: self.Close()

        self.menus['about'].Append(13, 'Info', "Information about the modmaker!",kind=wx.ITEM_NORMAL)
        self.menus['func'][13] = lambda: newMenu('Info')
        self.menus['about'].Append(14, 'QA', "Information about question!",kind=wx.ITEM_NORMAL)
        self.menus['func'][14] = lambda: newMenu('QA')

        self.menubar.Append(self.menus['project'], 'Project')
        self.menubar.Append(self.menus['about'], 'About')

        for x in self.menus['project'].GetMenuItems():
            self.Bind(wx.EVT_MENU, lambda evt: self.menus['func'][evt.GetId()](), x)

        self.SetMenuBar(self.menubar)

    def LoadUi(self):
        self.pnl = wx.Panel(self)
        self.pnl.SetSize(self.Size)
        wx.StaticText(self.pnl, label ="Rusted warfare mod maker!",name="WelcomeMessage", size = wx.DefaultSize).SetFont(wx.Font(18,wx.DECORATIVE, wx.SLANT, wx.BOLD))
        self.pnl.FindWindowByName("WelcomeMessage").SetForegroundColour(wx.Colour(199, 197, 195))
        self.pnl.FindWindowByName("WelcomeMessage").Centre()
        self.Bind(wx.EVT_SIZE, lambda _: {self.pnl.SetSize(self.Size), self.pnl.FindWindowByName("WelcomeMessage").Centre()})

if __name__ == '__main__':
    app = wx.App()
    mainwin = mainWindow(None)
    
    app.MainLoop()
    print("Quit....")