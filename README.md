# Automated Media & File Organizer Utility

A robust command-line Python utility designed to automatically scan directories (like your messy `Downloads` or `Desktop` folders), categorize files based on their extensions, move them into structured subfolders, handle name collisions safely, and maintain a detailed execution log.


## Features

* **Smart Categorization:** Automatically sorts files into specific folders based on their extensions (`Images`, `Documents`, `Videos`, `Audios`, `Archives`, `Code & Data`, `Executables`, and `Others`).
* **Collision Resolution:** Automatically detects if a file with the same name already exists in the destination folder and appends a secure counter (e.g., `file_1.pdf`) to prevent overwriting.
* **CLI Flexibility:** Powered by `argparse`, allowing you to run the script on any custom directory dynamically via the command line.
* **Audit Logging:** Automatically generates a `file_organizer.log` file tracking every successful move and error with timestamps.
* **Safe Handling:** Skips hidden files (`.`) and directories to protect system files.


## Tech Stack & Modules Used

* **Python 3.12.10**
* **`pathlib`** (For modern, object-oriented filesystem paths)
* **`shutil`** (For safe file transfer/moving operations)
* **`logging`** (For background execution auditing)
* **`argparse`** (For command-line argument parsing)

---

## Project Structure

```text
file-organizers/
│
├── organizer.py          # Core automation script
├── file_organizer.log    # Auto-generated activity log file
└── README.md             # Project documentation
```

## How to Run

1. Clone the repository or download the script:

    ```Bash
    git clone https://github.com/Its-SaAdi/files_organizer_py.git
    cd file-organizers
    ```

2. Run the script for the current directory:

    ```Bash
    python organizer.py
    ```

3. Run the script for a specific target folder (e.g., Downloads or Desktop):

    ```Bash
    python organizer.py --path "C:/Users/YourUsername/Downloads"
    ```

## Sample Log Output (file_organizer.log)

```text
2026-11-14 21:46:30,332 - INFO - Moved: ocean_view.jpg -> Images/ocean_view.jpg
2026-11-14 21:46:30,380 - INFO - Moved: Cost_and_Profit_Tracker.xlsx -> Documents/Cost_and_Profit_Tracker.xlsx
2026-11-14 21:46:30,427 - INFO - Moved: index.html -> Code & Data/index.html
2026-11-14 21:46:30,480 - INFO - Moved: Cormen Introduction to Algorithms.pdf -> Documents/Cormen Introduction to Algorithms.pdf
```

## Learning Outcomes
This project was built to master core Python programming concepts including file I/O operations, data structures (dictionaries/lists), exception handling, system path management, and building production-ready CLI tools.

## Author
Saad Jawed

[GitHub Profile]()