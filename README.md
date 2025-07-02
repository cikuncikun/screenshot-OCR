1 # Screenshot OCR Note-Taker
    2
    3 ## Overview
    4 This is a simple yet powerful desktop application designed to streamline
      note-taking from presentations, documents, or any on-screen content. It allows
      you to quickly capture a specific region of your screen, extract the text from
      it using Optical Character Recognition (OCR), and automatically copy that text
      to your clipboard.
    5
    6 ## Features
    7 *   **Interactive Region Selection:** Just like a snipping tool, you can click
      and drag to select the exact area of the screen you want to capture.
    8 *   **Instant Text Extraction:** Utilizes advanced OCR technology to convert
      images of text into editable digital text.
    9 *   **Automatic Clipboard Copy:** The extracted text is immediately copied to
      your clipboard, ready to be pasted into your notes, documents, or any text
      editor.
   10 *   **Background Operation:** Runs silently without a distracting terminal
      window popping up, ensuring a smooth workflow.
   11 *   **Standalone Executable:** Packaged as a single `.exe` file for Windows,
      making it portable and easy to run on any compatible machine without needing a
      Python installation.
   12 *   **Bundled Tesseract:** The Tesseract OCR engine is included within the
      executable, so you don't need to install it separately on other computers.
   13
   14 ## How to Use (Standalone Executable)
   15 1.  **Download:** Get the `screenshot_to_text.exe` file from the `dist` folder
      in this repository.
   16 2.  **Run:** Double-click the `screenshot_to_text.exe` file.
   17 3.  **Select Area:** Your screen will dim slightly. Click and drag your mouse
      to select the region containing the text you want to capture.
   18 4.  **Paste:** Once you release the mouse, the extracted text will be
      automatically copied to your clipboard. You can now paste it into your favorite
      note-taking app (e.g., Notepad, Word, OneNote, Obsidian).
   19
   20 ## Technologies Used
   21 *   **Python:** The core programming language.
   22 *   **`pyautogui`:** For taking screenshots of specific regions.
   23 *   **`pytesseract`:** A Python wrapper for the Tesseract OCR engine.
   24 *   **`Pillow` (PIL Fork):** For image processing.
   25 *   **`pyperclip`:** For cross-platform clipboard operations.
   26 *   **`tkinter`:** Python's standard GUI library, used for the interactive
      selection window.
   27 *   **`PyInstaller`:** Used to package the Python script and its dependencies
      into a standalone executable.
   28 *   **Tesseract OCR:** The powerful open-source OCR engine by Google.
   29
   30 ## Setup for Development (Optional)
   31 If you wish to run or modify the script from source:
   32 1.  **Install Python:** Ensure Python 3.x is installed on your system.
   33 2.  **Install Tesseract OCR:** Download and install the Tesseract OCR engine
      (e.g., from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)). Make
      sure to add it to your system's PATH.
   34 3.  **Install Python Libraries:**

      pip install pyautogui pytesseract Pillow pyperclip

   1 4.  **Run the script:**

      python screenshot_to_text.py


   ... first 13 lines hidden ...

   1
   2 ## Contributing
   3 Feel free to fork this repository, open issues, or submit pull requests if you
     have ideas for improvements or bug fixes!
   4
   5 ---
   6 *Made with ❤️ by V.M.B 
