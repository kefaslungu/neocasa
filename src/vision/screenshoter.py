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
    # Create a timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(output_dir, f"full_screenshot_{timestamp}.png")

    with mss.mss() as sct:
        # Capture the full screen
        sct.shot(output=output_file)

    analyze_image(output_file)

def take_active_window_screenshot():
    output_dir = get_screenshot_directory()
    hwnd = win32gui.GetForegroundWindow()
    # Create a timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(output_dir, f"active_window_{timestamp}.png")

    # Get the active window's dimensions
    rect = win32gui.GetWindowRect(hwnd)
    left, top, right, bottom = rect

    with mss.mss() as sct:
        monitor = {"top": top, "left": left, "width": right - left, "height": bottom - top}
        screenshot = sct.grab(monitor)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=output_file)

    analyze_image(output_file)
