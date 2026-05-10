import os

base_path = "."

folders = [
    "train/ok_front",
    "train/def_front",
    "test/ok_front",
    "test/def_front"
]

for folder in folders:
    path = os.path.join(base_path, folder)
    count = len(os.listdir(path))
    print(f"{folder}: {count} images")
