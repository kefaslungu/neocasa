# create a function that creates buttons everywhere we need it.
# originally written for system inspect https://github.com/kefaslungu/systeminspect
# Since I need the same thing, I'll use it in neocasa again. Cheers!
import wx
def create_button(parent, label, handler):
    """Creates a button and binds it to the specified event handler."""
    btn = wx.Button(parent, label=label)
    btn.Bind(wx.EVT_BUTTON, handler)
    return btn


