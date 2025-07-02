import pyautogui
import pytesseract
from PIL import Image
import time
import tkinter as tk
import pyperclip # Import pyperclip
import os # New import
import sys # New import

# Function to get the path to resources, whether running as script or bundled executable
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# IMPORTANT:
# If you installed Tesseract in a different location, you will need to
# change the following line to point to your Tesseract installation.
# For example: pytesseract.pytesseract.tesseract_cmd = r'C:\Users\YourUser\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Dynamically set Tesseract command path
# When bundled, Tesseract-OCR will be a folder next to the executable
# When running as script, it will use the default system path or the one specified below
if getattr(sys, 'frozen', False): # Check if running as a PyInstaller executable
    # Assuming Tesseract-OCR folder is placed next to the executable
    tesseract_exe_path = resource_path(os.path.join('Tesseract-OCR', 'tesseract.exe'))
    pytesseract.pytesseract.tesseract_cmd = tesseract_exe_path
else:
    # Fallback for development environment
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class SelectionWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.withdraw() # Hide the main window
        self.attributes('-fullscreen', True)
        self.attributes('-alpha', 0.3) # Make it transparent
        self.canvas = tk.Canvas(self, cursor="cross", bg="gray10")
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

        self.start_x = None
        self.start_y = None
        self.rect_id = None
        self.selected_region = None # (x, y, width, height)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.update_idletasks()
        self.deiconify() # Show the window

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if self.rect_id:
            self.canvas.delete(self.rect_id)
        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red', width=2)

    def on_mouse_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x = self.canvas.canvasx(event.x)
        end_y = self.canvas.canvasy(event.y)

        # Ensure coordinates are positive and represent top-left, width, height
        x1, y1 = min(self.start_x, end_x), min(self.start_y, end_y)
        x2, y2 = max(self.start_x, end_x), max(self.start_y, end_y)

        width = x2 - x1
        height = y2 - y1

        self.selected_region = (int(x1), int(y1), int(width), int(height))
        self.destroy() # Close the selection window

def screenshot_to_text_interactive():
    """
    Allows interactive selection of a screen region, then extracts text using OCR.
    """
    root = tk.Tk()
    root.withdraw() # Hide the main Tkinter window

    selection_window = SelectionWindow(root)
    root.wait_window(selection_window) # Wait for the selection window to close

    selected_region = selection_window.selected_region

    if selected_region and selected_region[2] > 0 and selected_region[3] > 0: # Check if a valid region was selected
        print(f"Capturing region: {selected_region}")
        try:
            # Take a screenshot of the selected region
            screenshot = pyautogui.screenshot(region=selected_region)
            print("Region screenshot taken.")

            # Use Tesseract to do OCR on the image
            print("Extracting text from the screenshot...")
            text = pytesseract.image_to_string(screenshot)

            if text.strip():
                print("\n--- Extracted Text ---")
                print(text)
                print("----------------------")
                pyperclip.copy(text) # Copy text to clipboard
                print("Text copied to clipboard!")
            else:
                print("\nNo text found in the selected region.")

        except FileNotFoundError:
            print("\nERROR: Tesseract not found.")
            print("Please make sure Tesseract is installed and the path in this script is correct.")
            print("Default path is: C:\\Program Files\\Tesseract-OCR\\tesseract.exe")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("No region selected or invalid region. Exiting.")

    root.destroy()

if __name__ == "__main__":
    screenshot_to_text_interactive()