import os
import re

folder = input("Enter the folder path: ").strip().strip('"')

for filename in os.listdir(folder):
    if not filename.lower().endswith(".mp3"):
        continue

    # Remove only the leading number
    new_filename = re.sub(r"^\d+\s*-\s*", "", filename)

    # Skip if nothing changed
    if new_filename == filename:
        continue

    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_filename)

    try:
        if os.path.exists(new_path):
            print(f"Skipped (already exists): {new_filename}")
        else:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"Error: {e}")

print("Done!")