import os
import hashlib

folder = input("Enter the folder path: ").strip().strip('"')

hashes = {}

for filename in os.listdir(folder):
    if not filename.lower().endswith(".mp3"):
        continue

    path = os.path.join(folder, filename)

    sha = hashlib.sha256()

    with open(path, "rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            sha.update(chunk)

    file_hash = sha.hexdigest()

    if file_hash in hashes:
        print(f"Duplicate:")
        print(f"  {filename}")
        print(f"  Same as: {hashes[file_hash]}\n")
    else:
        hashes[file_hash] = filename

print(f"Unique files: {len(hashes)}")