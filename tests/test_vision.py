import unittest
import os
import description_service
from src.vision import screenshoter, clipboard, camera

class TestDescriptionService(unittest.TestCase):
    def test_list_available_models(self):
        models = description_service.list_available_models()
        self.assertIsInstance(models, list)

    def test_get_model_by_name(self):
        model = description_service.get_model_by_name("GPT-4 vision")
        self.assertIsNotNone(model)
        self.assertTrue(hasattr(model, 'process'))

    def test_process_image_file_not_found(self):
        model = description_service.get_model_by_name("GPT-4 vision")
        # Should handle file not found gracefully
        with self.assertRaises(Exception):
            model.process('nonexistent.png')

    def test_process_with_mock(self):
        # This test assumes you have a valid image and API key configured for at least one model
        model = description_service.get_model_by_name("GPT-4 vision")
        if not model or not model.is_available:
            self.skipTest("No available model or API key not set.")
        # Use a dummy image path or mock encode_image if needed
        # For now, just check that process raises FileNotFoundError for missing file
        with self.assertRaises(Exception):
            model.process('fake_path.png')

class TestScreenshoter(unittest.TestCase):
    def test_get_screenshot_directory(self):
        path = screenshoter.get_screenshot_directory()
        self.assertTrue(os.path.exists(path))
        self.assertIn('screenshots', path)

    def test_take_full_screenshot_error(self):
        # Simulate error by patching mss
        import builtins
        orig_mss = screenshoter.mss.mss
        screenshoter.mss.mss = lambda: (_ for _ in ()).throw(Exception('fail'))
        file, err = screenshoter.take_full_screenshot()
        self.assertIsNone(file)
        self.assertIsNotNone(err)
        screenshoter.mss.mss = orig_mss

    def test_take_active_window_screenshot_error(self):
        orig_mss = screenshoter.mss.mss
        screenshoter.mss.mss = lambda: (_ for _ in ()).throw(Exception('fail'))
        file, err = screenshoter.take_active_window_screenshot()
        self.assertIsNone(file)
        self.assertIsNotNone(err)
        screenshoter.mss.mss = orig_mss

class TestClipboard(unittest.TestCase):
    def test_get_clipboard_image_no_image(self):
        # This test will pass if clipboard does not contain an image
        file, err = clipboard.get_clipboard_image()
        if file is None:
            self.assertIsNotNone(err)
        else:
            self.assertTrue(os.path.exists(file))

class TestCamera(unittest.TestCase):
    def test_snap_picture_fail(self):
        # Simulate camera not available
        orig_cv2 = camera.cv2.VideoCapture
        camera.cv2.VideoCapture = lambda x: type('FakeCap', (), {'isOpened': lambda s: False, 'release': lambda s: None})()
        file, err = camera.snap_picture()
        self.assertIsNone(file)
        self.assertIsNotNone(err)
        camera.cv2.VideoCapture = orig_cv2

if __name__ == '__main__':
    unittest.main()
