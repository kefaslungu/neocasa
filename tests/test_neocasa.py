import unittest
from src import neocasa
import wx

class TestNeocasaApp(unittest.TestCase):
    def test_frame_creation(self):
        app = wx.App(False)
        try:
            frame = neocasa.Neocasa()
            self.assertIsInstance(frame, wx.Frame)
            frame.Destroy()
        finally:
            app.Destroy()

    def test_on_hover_and_leave(self):
        app = wx.App(False)
        frame = neocasa.Neocasa()
        btn = wx.Button(frame.pnl)
        evt = wx.CommandEvent(wx.EVT_ENTER_WINDOW.typeId, btn.GetId())
        try:
            frame.on_hover(evt)
            frame.on_leave(evt)
        except Exception as e:
            self.fail(f'Exception raised: {e}')
        finally:
            frame.Destroy()
            app.Destroy()

if __name__ == '__main__':
    unittest.main()
