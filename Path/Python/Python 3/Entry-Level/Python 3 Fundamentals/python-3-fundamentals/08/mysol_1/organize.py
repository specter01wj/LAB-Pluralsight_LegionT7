import os
import shutil

# Set the root folder path (Your Custom Folder)
root_folder = "D:/My_Learning_Center/Web_Courses/LAB-Pluralsight_LegionT7/Path/Python/Python 3/Entry-Level/Python 3 Fundamentals/python-3-fundamentals/08/mysol_1/organize/"

# Ensure the root folder exists
if not os.path.exists(root_folder):
    print(f"❌ Root folder '{root_folder}' does not exist.")
    exit()

# Dictionary containing folder names and corresponding file extensions
folders = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".doc", ".docx", ".pdf", ".txt", ".pptx", ".xlsx"],
    "Archives": [".zip", ".rar", ".tar.gz", ".7z"]
}

# Create the subfolders if they don't exist
for folder_name in folders:
    folder_path = os.path.join(root_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Move files to the corresponding subfolder
for file_name in os.listdir(root_folder):
    original_file_path = os.path.join(root_folder, file_name)

    if os.path.isfile(original_file_path):  # Ensure it's a file, not a folder
        for folder_name, extensions in folders.items():
            if any(file_name.lower().endswith(ext) for ext in extensions):  # Case-insensitive match
                destination_folder = os.path.join(root_folder, folder_name)
                destination_file_path = os.path.join(destination_folder, file_name)

                # Avoid overwriting existing files by renaming if necessary
                counter = 1
                while os.path.exists(destination_file_path):
                    name, ext = os.path.splitext(file_name)
                    destination_file_path = os.path.join(destination_folder, f"{name}_{counter}{ext}")
                    counter += 1

                shutil.move(original_file_path, destination_file_path)
                print(f"✅ Moved: {file_name} ➡ {destination_folder}")
                break  # Stop checking other folders once moved

print("🎉 File organization completed!")
