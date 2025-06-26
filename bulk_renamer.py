import os

def bulk_rename(directory, prefix="", suffix=""):
    """Rename files in a directory with a prefix/suffix."""
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}{name}{suffix}{ext}"
            os.rename(
                os.path.join(directory, filename),
                os.path.join(directory, new_name)
            )
            print(f"Renamed {filename} to {new_name}")

if __name__ == "__main__":
    directory = input("Enter directory path: ").strip()
    prefix = input("Enter prefix (leave empty if none): ").strip()
    suffix = input("Enter suffix (leave empty if none): ").strip()
    
    if os.path.isdir(directory):
        bulk_rename(directory, prefix, suffix)
        print("Renaming complete!")
    else:
        print("Invalid directory path.")
