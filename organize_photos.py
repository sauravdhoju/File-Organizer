import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_photos(directory_path):
    photo_extensions = ['.png', '.jpeg', '.jpg', '.heic']
    photos_dir = os.path.join(directory_path, 'photos')
    os.makedirs(photos_dir, exist_ok=True)

    for file_name in os.listdir(directory_path):
        if file_name.lower().endswith(tuple(photo_extensions)):
            shutil.move(os.path.join(directory_path, file_name), 
                        os.path.join(photos_dir, os.path.splitext(file_name)[1][1:]))
            print(f"Moved {file_name} to {photos_dir}")

def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        organize_photos(directory_path)
        print("Photos organized successfully!")

root = tk.Tk()
root.title("Photo Organizer")

tk.Label(root, text="Select a directory containing photos").pack(pady=10)
tk.Button(root, text="Browse", command=browse_directory).pack(pady=10)

root.mainloop()
