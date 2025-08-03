# Dummy File Generator & Folder Organizer



## 📁 Project Structure

```
📦 FolderOrganizer
├── dummyGenerator.py          # Dummy file creator
├── FolderOrganizer.exe        # Portable executable
├── gui.py                     # GUI frontend for the organizer
├── organizer.py               # Folder organizer
└── README.md                  # Project documentation
```


This project contains three Python scripts to help with file organization, testing folder structures, and running the tool with a graphical interface:

* `dummyGenerator.py`: A utility to generate a wide variety of dummy files across multiple categories (Images, Documents, Audio, etc.)
* `organizer.py`: A powerful folder organizer that automatically sorts files into categorized folders based on file extensions.
* `gui.py`: A graphical interface for launching and using the organizer functionality.

A **portable executable** (`FolderOrganizer.exe`) is also included for quick use without needing Python installed.

---

## 📁 `dummyGenerator.py` – Dummy File Generator

Generates a comprehensive dataset of files for testing file organizers or backup tools.

### ✅ Features:

* Generates dummy files for the following categories:

  * Images, Documents, Audio, Videos, Archives
  * Scripts, Executables, Fonts, Spreadsheets
  * Presentations, Databases, Web Files, Miscellaneous
* Each file contains placeholder content matching its type.
* Random file names are used for realism.
* Output files are stored in a user-specified directory.

### 📦 How to Use:

```bash
python dummyGenerator.py
```

* You’ll be prompted to enter the destination folder path.

---

## 🗂️ `organizer.py` – Smart Folder Organizer

Organizes cluttered directories by sorting files into folders based on file types and extensions.

### ✅ Features:

* Automatically organizes all files in the selected folder.
* Files are sorted into meaningful folders such as:

  * `Images`, `Documents`, `Videos`, `Scripts`, `Archives`, etc.
* **Execution Queue**:

  * Automatically logs all operations.
  * Keeps an execution history for transparency.
* **Skips Special Folder**:

  * Ignores any folder named `nodottouch`, leaving its contents untouched.
* Supports wide range of file extensions, including obscure or advanced types.
* Can be run via Python or as a **portable executable** (`organizer.exe`) for non-Python users.
* Robust error handling for read-only or locked files.



---

## 🖼️ `gui.py` – Graphical Interface (GUI)

A simple graphical interface built using `tkinter` for easier interaction with the organizer.

### ✅ Features:

* Allows users to browse and select a folder using a file dialog.
* Provides buttons to trigger folder organization.
* Displays status messages or alerts.
* Runs the same organizing logic behind the scenes using `organizer.py`.

### 📦 How to Use:

```bash
python gui.py
```

* A window will appear where you can select a folder and click to organize it.

---






---

## 🧳 `FolderOrganizer.exe` – Portable Executable

A no-installation, click-to-run version of the folder organizer for quick use on any Windows machine.

### ✅ Why Use the `.exe` Version?

* **Zero setup**: No need to install Python or dependencies.
* **Plug & play**: Run directly from a USB or external drive.
* **Identical logic**: Performs exactly like `organizer.py`.
* **Ideal for non-developers**: Simple double-click operation.

### 💡 Features:

* Organizes cluttered folders by file type (Images, Documents, Videos, Archives, Scripts, etc.).
* Automatically creates subfolders and moves files accordingly.
* Skips any folder named `DoNotTouch` to avoid touching sensitive contents.
* Logs execution details for transparency.
* Handles common issues like locked or read-only files gracefully.
* Recognizes a wide range of common and uncommon file extensions.

### 🚀 How to Use:

1. **Locate** the `FolderOrganizer.exe` file in the root of the project.
2. **Double-click** to launch it.
3. A prompt will appear asking for the path to the folder you want to organize.
4. The tool will sort files into structured folders within the selected directory.

> 💼 *Great for QA testers, IT staff, or students needing fast and repeatable file cleanup without coding!*

---


## 💼 Use Cases

* Preparing test environments
* Cleaning download folders
* Organizing project directories
* Demoing file sorters or automation tools


---

## 📝 Notes

* No sensitive data is included in generated or organized files.
* Feel free to contribute by suggesting new file types or improving sorting logic.

---

## 📜 License

MIT License – Free to use and modify.

---

## 🙌 Author

Built with ❤️ to help QA testers, developers, and students automate boring file tasks.



































