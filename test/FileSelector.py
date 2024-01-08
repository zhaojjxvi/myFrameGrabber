import tkinter as tk
from tkinter import filedialog


def file_selector():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Picture files", "*.jpg"),
                                                      ("Video files", ".mp4 .avi .mov .wmv"),
                                                      ("All files", "*.*")])
    print(file_path)
    print(file_path == '')
    return file_path


if __name__ == '__main__':
    file_selector()
