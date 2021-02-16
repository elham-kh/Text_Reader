import ocrmypdf
import os

# change the current directory to the directory where the running script file (.py) exists
os.chdir(os.path.dirname(os.path.abspath(__file__)))



if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
    ocrmypdf.ocr('page2.pdf', 'output.pdf', deskew=True)