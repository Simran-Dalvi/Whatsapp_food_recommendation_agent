from pathlib import Path

folders = [
    "app",
    "app/data"
]

for folder in folders:
    path = Path(folder)

    if not path.exists():
        path.mkdir(parents=True)
        print(f"Created folder: {folder}")
    else:
        print(f"Folder already exists: {folder}")

files = [
    "app/main.py",
    "app/recommendation.py",
    "app/data/menu.csv",
    "app/data/metadata.md",
    "requirements.txt",
    ".env"
]

for file in files:
    path = Path(file)

    if not path.exists():
        path.touch()
        print(f"Created file: {file}")
    else:
        print(f"File already exists: {file}")

print("\nProject structure ready.")