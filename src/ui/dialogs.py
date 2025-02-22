import sys
import os
from threading import Thread as t
import wx

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import speech
from .buttons import create_button

def display_result_dialog(result):
    """Creates and displays a dialog with the result, including read aloud, copy to clipboard, and close functionality."""

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
        dialog.Destroy()

    # Create the dialog
    dialog = wx.Dialog(None, wx.ID_ANY, title="Image Description", size=(500, 350), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
    pnl = wx.Panel(dialog)

    # Set font for better readability
    font = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
    
    # Add a TextCtrl to display the result
    text_ctrl = wx.TextCtrl(pnl, value=result, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.BORDER_SIMPLE, size=(460, 220))
    text_ctrl.SetFont(font)
    text_ctrl.SetBackgroundColour(wx.Colour(30, 30, 30))  # Dark background
    text_ctrl.SetForegroundColour(wx.Colour(255, 255, 255))  # White text

    # Layout configuration
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(text_ctrl, 1, flag=wx.EXPAND | wx.ALL, border=10)

    # Button section
    btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
    btn_sizer.Add(create_button(pnl, "Read Aloud", read_aloud), 1, flag=wx.EXPAND | wx.ALL, border=5)
    btn_sizer.Add(create_button(pnl, "Copy", copy_result), 1, flag=wx.EXPAND | wx.ALL, border=5)
    btn_sizer.Add(create_button(pnl, "Close", close), 1, flag=wx.EXPAND | wx.ALL, border=5)

    sizer.Add(btn_sizer, 0, flag=wx.CENTER | wx.ALL, border=10)
    pnl.SetSizer(sizer)

    # Show the dialog
    dialog.ShowModal()
    dialog.Destroy()
    return
