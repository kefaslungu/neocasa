# neocasa
import os
import sys
import winsound
import wx
from threading import Thread as t

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import sounds
import ui
import vision


class Neocasa(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title="Neocasa", size=(500, 400))
        icon = wx.Icon("images/neocasa_logo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        # Set background color and font
        self.pnl = wx.Panel(self)
        self.pnl.SetBackgroundColour("#2C2F33")  # Dark gray background

        font = wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        vbox = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self.pnl, label="Neocasa")
        title.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        title.SetForegroundColour("#FFFFFF")  # White text
        vbox.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 15)

        # Button styling
        button_labels = [
            ("Open an Image from file explorer", self.open_image),
            ("Take a picture using Built-in Camera", self.snap),
            ("Describe Clipboard Image", self.clipboard_photo),
            ("Describe Current Window", self.window_screenshot),
            ("Take a Full Screenshot and describe it", self.full_screenshot),
        ]

        for label, handler in button_labels:
            btn = wx.Button(self.pnl, label=label, size=(250, 40))
            btn.SetFont(font)
            btn.SetBackgroundColour("#7289DA")  # Soft blue
            btn.SetForegroundColour("#FFFFFF")  # White text
            btn.SetWindowStyle(wx.BORDER_NONE)  # Remove borders
            btn.Bind(wx.EVT_ENTER_WINDOW, self.on_hover)
            btn.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave)
            btn.Bind(wx.EVT_BUTTON, handler)
            vbox.Add(btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.pnl.SetSizer(vbox)
        self.Bind(wx.EVT_CLOSE, self.close)

    def on_hover(self, event):
        event.GetEventObject().SetBackgroundColour("#677BC4")  # Darker blue on hover
        event.GetEventObject().Refresh()

    def on_leave(self, event):
        event.GetEventObject().SetBackgroundColour("#7289DA")  # Original color
        event.GetEventObject().Refresh()

    def full_screenshot(self, event=None):
        def capture_and_notify():
            image_path, error = vision.take_full_screenshot()
            if error:
                wx.CallAfter(wx.MessageBox, f"Error: {error}", "Error", wx.OK | wx.ICON_ERROR)
            else:
                sounds.screenshot()
                t(target=self.analyze_image, args=(image_path,)).start()

        t(target=capture_and_notify).start()

    def window_screenshot(self, event=None):
        def capture_and_notify():
            image_path, error = vision.take_active_window_screenshot()
            if error:
                wx.CallAfter(wx.MessageBox, f"Error: {error}", "Error", wx.OK | wx.ICON_ERROR)
            else:
                sounds.screenshot()
                t(target=self.analyze_image, args=(image_path,)).start()

        t(target=capture_and_notify).start()

    def clipboard_photo(self, event=None):
        t(target=self.capture_and_notify, daemon=True).start()

    def capture_and_notify(self):
        image_path, error = vision.get_clipboard_image()
        if error:
            wx.CallAfter(wx.MessageBox, f"Error: {error}", "Error", wx.OK | wx.ICON_ERROR)
        else:
            t(target=self.analyze_image, args=(image_path,)).start()

    def snap(self, event=None):
        def capture_and_notify():
            image_path, error = vision.snap_picture()
            if error:
                wx.CallAfter(wx.MessageBox, error, "Error", wx.OK | wx.ICON_ERROR)
            else:
                sounds.snap()
                t(target=self.analyze_image, args=(image_path,)).start()

        t(target=capture_and_notify).start()

    def open_image(self, event):
        with wx.FileDialog(
            self,
            "Open an image file",
            wildcard="Image files (*.jpg;*.jpeg;*.png)|*.jpg;*.jpeg;*.png",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return

            image_path = file_dialog.GetPath()

        t(target=self.analyze_image, args=(image_path,)).start()

    def analyze_image(self, image_path):
        sounds.waiting()
        vision.image_analyzer.analyze_image(image_path)
        wx.CallAfter(self.display_result)

    def display_result(self):
        if vision.image_analyzer.result:
            winsound.PlaySound(None, winsound.SND_PURGE)
            ui.display_result(vision.image_analyzer.image_result)

    def close(self, event):
        event.Skip()


if __name__ == "__main__":
    app = wx.App()
    neocasa = Neocasa()
    neocasa.Show()
    app.MainLoop()
