import os
import sys
import threading
import wx
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import speech
import ui
import vision

class Neocasa(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title="Neocasa", size=(400, 300))
        self.pnl = wx.Panel(self)  # Create the panel
        ui.create_button(self.pnl, "Open an image", self.open_image)

        self.threads = []  # Keep track of threads

        # Bind the close event
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def open_image(self, event):
        """Handle image file opening."""
        with wx.FileDialog(
            self,
            "Open an image file",
            wildcard="Image files (*.jpg;*.jpeg;*.png)|*.jpg;*.jpeg;*.png",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        ) as file_dialog:

            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return  # User canceled the dialog

            # Get the selected file path
            image_path = file_dialog.GetPath()

        # Start a new thread to analyze the image
        thread = threading.Thread(target=self.analyze_and_update_ui, args=(image_path,), daemon=True)
        self.threads.append(thread)
        thread.start()

    def analyze_and_update_ui(self, image_path):
        """Perform image analysis in a separate thread and update the UI."""
        # Perform the image analysis (non-blocking)
        vision.image_analyzer.analyze_image(image_path)

        # Once the result is ready, update the UI on the main thread
        if vision.image_analyzer.result:
            wx.CallAfter(ui.display_result, vision.image_analyzer.image_result)

    def on_close(self, event):
        """Ensure all threads are properly finished before closing the app."""
        # Wait for threads to finish
        for thread in self.threads:
            thread.join(timeout=1)  # Wait up to 1 second for thread to finish

        self.Destroy()  # Close the window

if __name__ == "__main__":
    app = wx.App()
    neocasa = Neocasa()
    neocasa.Show()
    app.MainLoop()
