import os
import sys
import winsound
import wx
from threading import Thread as t
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import sounds
import speech
import ui
import vision


class Neocasa(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title="Neocasa", size=(400, 300))
        self.pnl = wx.Panel(self)  # Create the panel
        self.Bind(wx.EVT_CLOSE, self.close)
        # we need to create the buttons that will be on the panel one by one.
        ui.create_button(self.pnl, "Open an image", self.open_image)# a function to open an image some where on your computer, then describe it. Tipical ctrl+O
        ui.create_button(self.pnl, "Take a picture using Built-in camera", self.snap)# takes a picture using your built-in camera to describe it. 

    # define the function to snap the picture.
    def snap(self, event=None):
        def capture_and_notify():
            image_path, error = vision.snap_picture()
    
            if error:
                wx.CallAfter(wx.MessageBox, error, "Error", wx.OK | wx.ICON_ERROR)
            else:
                sounds.waiting()
                t(target=self.analyze_image, args=(image_path,)).start()
        
        t(target=capture_and_notify).start()
    
    # Tipical Ctrl+O...
    def open_image(self, event):
        """Handle image file opening."""
        with wx.FileDialog(
            self,
            "Open an image file",
            wildcard="Image files (*.jpg;*.jpeg;*.png)|*.jpg;*.jpeg;*.png",# only these file extentions will show, we don't need any thing else.
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        ) as file_dialog:

            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return  # User canceled the dialog

            # Get the selected file path
            image_path = file_dialog.GetPath()
        # Start the image analysis in a separate thread to avoid freezing of the UI.
        t(target=self.analyze_image, args=(image_path,)).start()
        sounds.waiting()
    # A different function to analyze the image to avoid stories that touches the heart.
    def analyze_image(self, image_path):
        """Analyze the image and update the UI with the result."""
        # Perform image analysis
        vision.image_analyzer.analyze_image(image_path)

        # Use wx.CallAfter to safely update the UI from the thread
        wx.CallAfter(self.display_result)

    def display_result(self):
        """Display the result of the image analysis."""
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
