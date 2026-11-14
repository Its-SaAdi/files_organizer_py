import logging
from pathlib import Path
import shutil
import argparse

FILE_CATEGORIES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp', '.tiff', '.ico', '.heic', '.raw'],
    "Documents": ['.txt', '.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.csv', '.md', '.rtf', '.odt', '.epub'],
    "Videos": ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.3gp'],
    "Audios": ['.mp3', '.m4a', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4b'],
    "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.iso'],
    "Code & Data": ['.html', '.css', '.js', '.jsx', '.ts', '.tsx', '.py', '.java', '.c', '.cpp', '.h', '.json', '.xml', '.sql', '.sh', '.bat', '.yaml', '.yml'],
    "Executables & Installers": ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm'],
    "Fonts": ['.ttf', '.otf', '.woff', '.woff2']
}

logging.basicConfig(
    filename= 'file_organizer.log',
    level= logging.INFO,
    format= '%(asctime)s - %(levelname)s - %(message)s'
)

def get_category(file_extension):
    for key, value in FILE_CATEGORIES.items():
        if file_extension.lower() in value:
            return key

    return 'Others'

def get_unique_path(dest_folder_path, file_item):
    destination_path = dest_folder_path / file_item.name

    if not destination_path.exists():
        return destination_path

    counter = 1

    while True:
        new_file_name = f"{file_item.stem}_{counter}{file_item.suffix}"
        new_path = dest_folder_path / new_file_name

        if not new_path.exists():
            return new_path

        counter += 1


def scan_directory(targer_dir_path):
    try:
        path = Path(targer_dir_path)
        if not path.exists():
            raise Exception("Invalid path")

        for item in path.iterdir():
            if item.is_dir() or item.name.startswith("."):
                continue

            category_name = get_category(item.suffix)
            # if not Path(f"{targer_dir_path}/{category_name}").exists():
            #     Path(f"{targer_dir_path}/{category_name}").mkdir(parents=True, exist_ok=True)

            category_folder = path / category_name
            category_folder.mkdir(parents=True, exist_ok=True)

            dest_file_path = get_unique_path(category_folder, item)

            shutil.move(str(item), str(dest_file_path))

            log_msg = f"Moved: {item.name} -> {category_name}/{dest_file_path.name}"
            print(log_msg)
            logging.info(log_msg)

    except Exception as e:
        print("An error occured:", e)
        logging.error(f"An error occured: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Files Organizer Utility")

    parser.add_argument(
        "--path",
        type=str,
        default='.',
        help="Path of the directory to organize (defaults to current directory)"
    )

    args = parser.parse_args()
    scan_directory(args.path)