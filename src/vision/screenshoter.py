import os
from datetime import datetime
import mss
import mss.tools
import win32gui
from .image_analyzer import analyze_image

def get_screenshot_directory():
    base_dir = os.path.join(os.environ["LOCALAPPDATA"], "neocasa", "screenshots")
    os.makedirs(base_dir, exist_ok=True)  # Create the directory if it doesn't exist
    return base_dir

def take_full_screenshot():
    output_dir = get_screenshot_directory()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(output_dir, f"full_screenshot_{timestamp}.png")

    try:
        with mss.mss() as sct:
            sct.shot(output=output_file)

        return output_file, None  # Return path of the screenshot
    except Exception as e:
        return None, str(e)  # Return error message

def take_active_window_screenshot():
    output_dir = get_screenshot_directory()
    hwnd = win32gui.GetForegroundWindow()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(output_dir, f"active_window_{timestamp}.png")

    try:
        rect = win32gui.GetWindowRect(hwnd)
        left, top, right, bottom = rect

        with mss.mss() as sct:
            monitor = {"top": top, "left": left, "width": right - left, "height": bottom - top}
            screenshot = sct.grab(monitor)
            mss.tools.to_png(screenshot.rgb, screenshot.size, output=output_file)

        return output_file, None  # Return path of the screenshot
    except Exception as e:
        return None, str(e)  # Return error message
