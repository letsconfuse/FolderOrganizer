#organizer.py

import shutil
from pathlib import Path

# Define categories (same as your original code)
FILE_CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".tif", 
               ".raw", ".heif", ".heic", ".ico", ".eps", ".ai", ".psd", ".indd"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".rtf", ".odt", ".csv", 
                  ".epub", ".md", ".tex", ".xls", ".ods", ".ppt", ".pages", ".wpd", ".ps", ".latex", ".srt", 
                  ".mobi", ".azw3"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".alac", ".aiff", ".opus", 
              ".mka", ".amr", ".midi", ".mid", ".caf", ".pcm", ".aif", ".ra", ".rm", ".wv", ".dts"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm", ".flv", ".m4v", ".mpeg", ".mpg", ".wmv", 
               ".3gp", ".rmvb", ".ts", ".vob", ".ogv", ".swf", ".f4v", ".m2ts", ".divx", ".xvid", ".h264"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".tar.gz", ".tar.bz2", ".tar.xz", ".gzip", ".bzip2", 
                 ".xz", ".lzma", ".ace", ".z", ".tar.lz", ".arj", ".cab", ".iso", ".img", ".dmg", ".udf"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh", ".bat", ".php", ".ts", ".pl", ".rb", ".cpp", 
                ".c", ".h", ".java", ".swift", ".go", ".tsv", ".xml", ".json", ".yaml", ".ini", ".conf", 
                ".bash", ".sql", ".vbs", ".tcl", ".ps1", ".fsh", ".scala", ".clj", ".r", ".lua", ".as", ".dart"],
    "Executables": [".exe", ".msi", ".apk", ".jar", ".dmg", ".pkg", ".bat", ".app", ".appimage", ".deb", 
                    ".rpm", ".bin", ".run", ".wsf", ".vbe", ".scr", ".sys", ".gadget", ".xpi", ".cmd"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot", ".svg", ".fnt", ".fon", ".pfb", ".afm"],
    "Spreadsheets": [".ods", ".xls", ".xlsx", ".csv", ".tsv", ".xlsm", ".xltx", ".xltm", ".ods", ".numbers"],
    "Presentations": [".ppt", ".pptx", ".odp", ".key", ".potx", ".potm", ".ppsx"],
    "Databases": [".sql", ".sqlite", ".db", ".mdb", ".accdb", ".dbf", ".csv"],
    "Miscellaneous": [".json", ".xml", ".log", ".yml", ".yaml", ".md", ".txt", ".csv", ".ini", ".toml", ".nfo",
                      ".torrent", ".vtt", ".srt", ".xls", ".xlsx", ".bson"],
    "Web Files": [".html", ".css", ".js", ".php", ".json", ".xml", ".asp", ".jsp", ".cgi", ".svg", ".ejs", 
                  ".less", ".scss", ".ts", ".twig", ".handlebars", ".hbs", ".yaml", ".yml"]
}

IGNORE_FOLDER_NAME = "DoNotTouch"  # Folder to ignore during organization

def organize_folder(folder_path, ignore_paths):
    folder = Path(folder_path)
    ignore_folder = folder / IGNORE_FOLDER_NAME

    if not folder.exists():
        return "❌ Path does not exist."
    
    if not any(folder.iterdir()):
        return "📁 Folder is empty."

    # Normalize ignore paths into Path objects
    ignore_paths = [Path(path) for path in ignore_paths]

    for item in folder.iterdir():
        if item.is_file():
            if item in ignore_paths or is_in_ignore_folder(item, folder):
                continue  # Skip files inside the ignore folder or user-specified files
            move_file(item, get_target_folder(item, folder))
        elif item.is_dir() and item.name == IGNORE_FOLDER_NAME:
            continue  # Skip the ignore folder
    
    return "✅ Done!"

def is_in_ignore_folder(file_path, base_folder):
    ignore_folder = base_folder / IGNORE_FOLDER_NAME
    return ignore_folder in file_path.parents

# Keep other functions the same (get_target_folder, move_file, etc.)



def get_target_folder(file_path, base_folder):
    # Determine the target folder based on file extension
    for category, extensions in FILE_CATEGORIES.items():
        if file_path.suffix.lower() in extensions:
            return base_folder / category
    return base_folder / "Others"

def move_file(file_path, target_folder):
    target_folder.mkdir(exist_ok=True)
    destination = target_folder / file_path.name
    if destination.exists():
        destination = target_folder / f"{file_path.stem}_copy{file_path.suffix}"
    try:
        shutil.move(str(file_path), str(destination))
        print(f"Moved: {file_path.name} → {target_folder.name}")
    except Exception as e:
        print(f"❌ Failed to move {file_path.name}: {e}")
