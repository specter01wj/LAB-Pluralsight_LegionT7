import os
import shutil

folder_original = 'D:/My_Learning_Center/Web_Courses/LAB-Pluralsight_LegionT7/Path/Python/Python 3/Entry-Level/Python 3 Fundamentals/python-3-fundamentals/08/mysol_1/test/'
folder_destination = 'D:/My_Learning_Center/Web_Courses/LAB-Pluralsight_LegionT7/Path/Python/Python 3/Entry-Level/Python 3 Fundamentals/python-3-fundamentals/08/mysol_1/test/CleanedUp/'

# Create destination folder if it doesn't exist
os.makedirs(folder_destination, exist_ok=True)

for entry in os.scandir(folder_original):
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(location_original):
        # Check if file already exists in destination
        if os.path.exists(location_destination):
            print(f"⚠️ Skipping: {entry.name} (Already exists in destination)")
            continue

        try:
            shutil.move(location_original, location_destination)
            print(f"✅ Moved: {entry.name}")
        except Exception as e:
            print(f"❌ Error moving {entry.name}: {e}")
