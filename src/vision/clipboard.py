import os
import win32clipboard
import io
from datetime import datetime
from PIL import Image
import wx
from threading import Thread
import win32con

def get_clipboard_image():
    """Gets clipboard image, saves it, and returns the file path or an error message."""
    
    win32clipboard.OpenClipboard()
    try:
        # Handle clipboard file paths
        if win32clipboard.IsClipboardFormatAvailable(win32con.CF_HDROP):
            file_paths = win32clipboard.GetClipboardData(win32con.CF_HDROP)
            if file_paths and file_paths[0].lower().endswith((".png", ".jpg", ".jpeg")):
                return file_paths[0], None  # Return file path directly
        
        # Handle text containing a file path
        elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_UNICODETEXT):
            text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT).strip()
            if text.startswith('"') and text.endswith('"'):
                text = text[1:-1]  # Remove surrounding quotes

            if os.path.exists(text) and text.lower().endswith((".png", ".jpg", ".jpeg")):
                return text, None  # Return file path directly
        
        # Handle raw image data
        elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
            data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
            bmp_header_size = 14  # Skip BMP header
            img_data = data[bmp_header_size:]

            image = Image.open(io.BytesIO(img_data))

            # Ensure correct format
            img_format = image.format or "PNG"

            # Save directory
            save_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'neocasa', 'clipboard_images')
            os.makedirs(save_dir, exist_ok=True)  

            filename = f"clipboard_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.{img_format.lower()}"
            save_path = os.path.join(save_dir, filename)

            image.save(save_path, format=img_format)
            return save_path, None

        return None, "Clipboard does not contain a valid image or file path."
    
    except Exception as e:
        return None, str(e)  # Return the exact error

    finally:
        win32clipboard.CloseClipboard()
