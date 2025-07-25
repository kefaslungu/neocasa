
#menubar for the application

import wx
#subclass the wx.MenuBar
class Menubar(wx.MenuBar):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.__createMenuItem()


    #methods defined

    #get information about each menu item
    def __menuInfo(self):
        return (
            ('&File', (
                ('&Open Image...\tCtrl+O', self.on_open_image),
                ('&Exit Application\tAlt+F4', self.on_exit),
            )),
            ('&Models', (
                # Placeholder for model-related actions
                ('&Select Model', self.on_select_model),
            )),
            ('&Help', (
                ('&Source Code', self.on_source_code),
            )),
        )

    #create each menu item and add it to the menubar
    def __createMenuItem(self):
        for menuItem,  menuItemInfo in self.__menuInfo():
            menu= wx.Menu()
            for item in menuItemInfo:
                menuChild = menu.Append(wx.ID_ANY, item[0])
                self.parent.Bind(wx.EVT_MENU, item[1], menuChild)
            menu.AppendSeparator()
            self.Append(menu, menuItem)


    #events associated to this class
    #file menu item

    def on_open_image(self, event):
        # Call the parent's open_image method if it exists
        if hasattr(self.parent, 'open_image'):
            self.parent.open_image(event)

    def on_select_model(self, event):
        # Show a dialog for model selection and API key entry
        from vision import description_service
        import auth
        import wx

        class ModelDialog(wx.Dialog):
            def __init__(self, parent):
                super().__init__(parent, title="Model Settings", size=(400, 250))
                panel = wx.Panel(self)
                vbox = wx.BoxSizer(wx.VERTICAL)

                vbox.Add(wx.StaticText(panel, label="Select Model:"), 0, wx.ALL, 5)
                self.model_names = description_service.list_available_model_names()
                self.model_combo = wx.ComboBox(panel, choices=self.model_names, style=wx.CB_READONLY)
                vbox.Add(self.model_combo, 0, wx.EXPAND | wx.ALL, 5)

                vbox.Add(wx.StaticText(panel, label="API Key:"), 0, wx.ALL, 5)
                self.api_key_ctrl = wx.TextCtrl(panel)
                vbox.Add(self.api_key_ctrl, 0, wx.EXPAND | wx.ALL, 5)

                # Load current selection and key
                current_model = auth.get_setting("selected_model", self.model_names[0] if self.model_names else "")
                if current_model in self.model_names:
                    self.model_combo.SetValue(current_model)
                    self.api_key_ctrl.SetValue(auth.get_api_key(current_model) or "")

                def on_model_change(event):
                    model = self.model_combo.GetValue()
                    self.api_key_ctrl.SetValue(auth.get_api_key(model) or "")
                self.model_combo.Bind(wx.EVT_COMBOBOX, on_model_change)

                save_btn = wx.Button(panel, label="Save")
                save_btn.Bind(wx.EVT_BUTTON, self.on_save)
                vbox.Add(save_btn, 0, wx.ALIGN_CENTER | wx.ALL, 10)

                panel.SetSizer(vbox)
                self.Fit()

            def on_save(self, event):
                model = self.model_combo.GetValue()
                key = self.api_key_ctrl.GetValue()
                auth.set_api_key(model, key)
                auth.set_setting("selected_model", model)
                self.EndModal(wx.ID_OK)

        dlg = ModelDialog(self.parent)
        dlg.ShowModal()
        dlg.Destroy()

    def on_source_code(self, event):
        import webbrowser
        webbrowser.open('https://github.com/in/kefaslungu')

    def on_exit(self, event):
        self.parent.Close()

    #for the edit menu item
    def on_copy(self, event):
        pass

    def on_cut(self, event):
        pass

    def on_paste(self, event):
        pass

    def on_undo(self, event):
        pass

    #for the pview/page menu item
    def on_zoomIn(self, event):
        pass

    def on_zoomOut(self, event):
        pass

    def on_goToPage(self, event):
        pass

    def on_adjustFont(self, event):
        pass

    #for the advance menu item
    def on_checkWord(self, event):
        pass

    def on_rke(self, event):
        pass

    def on_downloadBook(self, event):
        pass

    def on_getVoices(self, event):
        pass

    #for the help menu item
    def on_about(self, event):
        pass

    def on_userGuide(self, event):
        pass

    def on_license(self, event):
        pass

    def on_website(self, event):
        pass
