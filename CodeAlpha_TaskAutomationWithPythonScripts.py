import os
import shutil

# Task: Move all .jpg files from one folder to another
def move_jpg_files(source_folder, destination_folder):
    # Create destination folder if it doesn’t exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through files in source folder
    for file in os.listdir(source_folder):
        if file.endswith(".jpg"):
            src = os.path.join(source_folder, file)
            dst = os.path.join(destination_folder, file)
            shutil.move(src, dst)
            print(f"Moved: {file}")

# Example usage
move_jpg_files(r"C:\Users\HP\Desktop\source", r"C:\Users\HP\Desktop\Destination")
print("All JPG files moved successfully!")