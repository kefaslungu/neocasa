import os
from datetime import datetime
import win32clipboard
import win32con
from PIL import Image
import io

import os
import win32clipboard
import io
from datetime import datetime
from PIL import Image
from threading import Thread
import win32con

def get_clipboard_image():
    """Gets clipboard image, saves it, and returns the file path or an error message."""
    
    win32clipboard.OpenClipboard()
    try:
        # Case 1: If clipboard contains a file (CF_HDROP)
        if win32clipboard.IsClipboardFormatAvailable(win32con.CF_HDROP):
            file_paths = win32clipboard.GetClipboardData(win32con.CF_HDROP)
            if file_paths and file_paths[0].lower().endswith((".png", ".jpg", ".jpeg")):
                return file_paths[0], None  # Return file path directly
        
        # Case 2: If clipboard contains a **file path as text**
        elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_UNICODETEXT):
            text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT).strip()
            if text.startswith('"') and text.endswith('"'):
                text = text[1:-1]  # Remove surrounding quotes

            if os.path.exists(text) and text.lower().endswith((".png", ".jpg", ".jpeg")):
                return text, None  # Return file path directly
        
        # Case 3: If clipboard contains raw image data (CF_DIB)
        elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
            data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
            
            # BMP files in clipboard start after 14 bytes (BMP header), remove them
            bmp_header_size = 14  
            img_data = data[bmp_header_size:]

            image = Image.open(io.BytesIO(img_data))

            # Ensure correct format
            img_format = image.format or "PNG"  # Default to PNG if unknown

            # Define save location
            save_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'neocasa', 'clipboard_images')
            os.makedirs(save_dir, exist_ok=True)  

            filename = f"clipboard_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.{img_format.lower()}"
            save_path = os.path.join(save_dir, filename)

            # Save in correct format
            image.save(save_path, format=img_format)
            return save_path, None

        else:
            return None, "Clipboard does not contain a valid image or file path."

    finally:
        win32clipboard.CloseClipboard()

    return None, "Unknown error occurred."
