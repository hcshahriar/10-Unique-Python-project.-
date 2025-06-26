import os
import shutil

def organize_files(directory):
    """Organize files in the directory by their extensions."""
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_ext = filename.split('.')[-1].lower()
            dest_dir = os.path.join(directory, file_ext)
            
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            shutil.move(
                os.path.join(directory, filename),
                os.path.join(dest_dir, filename)
            )
            print(f"Moved {filename} to {file_ext}/")

if __name__ == "__main__":
    target_dir = input("Enter directory path to organize: ").strip()
    if os.path.isdir(target_dir):
        organize_files(target_dir)
        print("Files organized successfully!")
    else:
        print("Invalid directory path.")
