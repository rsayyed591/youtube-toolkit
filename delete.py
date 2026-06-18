import os
import hashlib

# CHANGE THIS
folder = input("Enter the folder path: ").strip().strip('"')

hashes = {}
deleted = 0

for filename in os.listdir(folder):
    if not filename.lower().endswith(".mp3"):
        continue

    path = os.path.join(folder, filename)

    # Calculate SHA-256 hash
    sha = hashlib.sha256()

    with open(path, "rb") as f:
        while True:
            chunk = f.read(1024 * 1024)  # Read 1 MB at a time
            if not chunk:
                break
            sha.update(chunk)

    file_hash = sha.hexdigest()

    if file_hash in hashes:
        print(f"Deleting duplicate:")
        print(f"  {filename}")
        print(f"  Duplicate of: {hashes[file_hash]}")
        os.remove(path)
        deleted += 1
    else:
        hashes[file_hash] = filename

print(f"\nFinished!")
print(f"Deleted {deleted} duplicate files.")
print(f"Remaining unique songs: {len(hashes)}")