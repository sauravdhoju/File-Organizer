import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_photos(directory_path):
    # Create a 'photos' directory if it doesn't exist
    photos_dir = os.path.join(directory_path, 'photos')
    if not os.path.exists(photos_dir):
        os.mkdir(photos_dir)

    # Get a list of all files in the directory
    all_files = os.listdir(directory_path)

    # Define photo extensions
    photo_extensions = ['.png', '.jpeg', '.jpg', '.heic']

    # Iterate over each file
    for file_name in all_files:
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(file_name)
            file_extension = file_extension.lower()

            # Check if the file is a photo
            if file_extension in photo_extensions:
                # Create a subdirectory for the photo extension
                sub_dir = os.path.join(photos_dir, file_extension[1:])
                if not os.path.exists(sub_dir):
                    os.mkdir(sub_dir)

                # Move the file to the appropriate subdirectory
                new_file_path = os.path.join(sub_dir, file_name)
                shutil.move(file_path, new_file_path)
                print(f"Moved {file_name} to {sub_dir}")

def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        organize_photos(directory_path)
        print("Photos organized successfully!")

# Create a stylish tkinter GUI
root = tk.Tk()
root.title("Photo Organizer")
root.configure(bg="#f0f0f0")  # Set background color

label = tk.Label(root, text="Select a directory containing photos", font=("Helvetica", 14), bg="#f0f0f0")
label.pack(pady=10)

browse_button = tk.Button(root, text="Browse", font=("Helvetica", 12), command=browse_directory, bg="#007acc", fg="white")
browse_button.pack(pady=10)

root.mainloop()
