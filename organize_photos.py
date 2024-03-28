import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_files(directory_path):
    file_types = {
        "Photos": ['.png', '.jpeg', '.jpg', '.heic'],
        "PDFs": ['.pdf'],
        "Documents": ['.docx', '.xlsx', '.pptx', '.txt', '.rtf'],
        "Executables": ['.exe'],
        "Videos": ['.mov', '.mp4', '.avi', '.mkv'],
        "Others": []
    }

    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_types.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    category_dir = os.path.join(directory_path, category)
                    os.makedirs(category_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_dir, file_name))
                    print(f"Moved {file_name} to {category_dir}")
                    moved = True
                    break
            if not moved:
                other_dir = os.path.join(directory_path, "Others")
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(other_dir, file_name))
                print(f"Moved {file_name} to {other_dir}")

def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        organize_files(directory_path)
        print("Files organized successfully!")

root = tk.Tk()
root.title("File Organizer")

tk.Label(root, text="Select a directory containing files").pack(pady=10)
tk.Button(root, text="Browse", command=browse_directory).pack(pady=10)

root.mainloop()
