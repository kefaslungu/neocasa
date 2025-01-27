
import sys
import os
from threading import Thread as t
import wx
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import speech
from .buttons import create_button

def display_result_dialog(result):
    """Creates and displays a dialog with the result, read aloud, copy to clipboard, and close functionality."""
    
    def read_aloud(event):
        t(target=speech.speak, args=(result,)).start()

    def copy_result(event):
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(result))
            wx.TheClipboard.Close()
            wx.MessageBox("Result copied to clipboard!", "Info", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Unable to access the clipboard.", "Error", wx.OK | wx.ICON_ERROR)

    def close(event):
        dialog.EndModal(wx.ID_CANCEL)

    # Create the dialog
    app = wx.App(False)
    dialog = wx.Dialog(None, wx.ID_ANY, title="Image result", size=(400, 300))
    pnl = wx.Panel(dialog)

    # Add a TextCtrl to display the result
    text_ctrl = wx.TextCtrl(pnl, value=result, style=wx.TE_READONLY | wx.TE_MULTILINE, size=(380, 200))

    # Layout configuration
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(text_ctrl, 1, flag=wx.EXPAND | wx.ALL, border=10)

    # Add buttons
    btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
    btn_sizer.Add(create_button(pnl, "Read Aloud", read_aloud), 1, flag=wx.EXPAND | wx.ALL, border=5)
    btn_sizer.Add(create_button(pnl, "Copy to Clipboard", copy_result), 1, flag=wx.EXPAND | wx.ALL, border=5)
    btn_sizer.Add(create_button(pnl, "Close", close), 1, flag=wx.EXPAND | wx.ALL, border=5)

    sizer.Add(btn_sizer, 0, flag=wx.CENTER | wx.ALL, border=10)
    pnl.SetSizer(sizer)

    # Show the dialog
    dialog.ShowModal()
    dialog.Destroy()
    app.MainLoop()

# Example usage
if __name__ == "__main__":
    result = "Seen an image of a computer Text: Microsoft teams meeting."
    display_result_dialog(result)
