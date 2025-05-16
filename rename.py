import os

# Define the folder path
folder_path = r"D:\NGO1\charityworks-master\assets\img\disha"

# List of valid image extensions
valid_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")

# Get all files in the folder
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) 
         and f.lower().endswith(valid_extensions)]

# Sort files to ensure consistent renaming order
files.sort()

# Rename files sequentially
for i, filename in enumerate(files, 1):
    # Get the file extension
    file_ext = os.path.splitext(filename)[1].lower()
    
    # Define new filename (e.g., 1.jpg, 2.jpg)
    new_filename = f"{i}{file_ext}"
    
    # Define full paths for old and new filenames
    old_file = os.path.join(folder_path, filename)
    new_file = os.path.join(folder_path, new_filename)
    
    # Check if new filename already exists to avoid overwriting
    if os.path.exists(new_file):
        print(f"Warning: {new_filename} already exists, skipping {filename}")
        continue
    
    # Rename the file
    try:
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"Error renaming {filename}: {e}")

print("Renaming complete!")