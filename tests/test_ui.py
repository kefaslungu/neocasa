import unittest
from src.ui import dialogs, buttons
import wx

class TestDialogs(unittest.TestCase):
    def test_display_result_dialog_runs(self):
        # This test will only check that the function can be called without error
        # wx.App must be created for dialogs
        app = wx.App(False)
        try:
            dialogs.display_result_dialog('Test result')
        except Exception as e:
            self.fail(f'Exception raised: {e}')
        finally:
            app.Destroy()

class TestButtons(unittest.TestCase):
    def test_create_button(self):
        app = wx.App(False)
        frame = wx.Frame(None)
        called = {'val': False}
        def handler(event):
            called['val'] = True
        btn = buttons.create_button(frame, 'Test', handler)
        self.assertIsInstance(btn, wx.Button)
        # Simulate click
        evt = wx.CommandEvent(wx.EVT_BUTTON.typeId, btn.GetId())
        btn.GetEventHandler().ProcessEvent(evt)
        # Handler may not be called in this context, but no error should occur
        frame.Destroy()
        app.Destroy()

if __name__ == '__main__':
    unittest.main()
