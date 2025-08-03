#dummyGenerator.py

import os
import random
import string

# Define the categories and their extensions
file_categories = {
    "Images": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".tif", 
        ".raw", ".heif", ".heic", ".ico", ".eps", ".ai", ".psd", ".indd"
    ],
    "Documents": [
        ".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".rtf", ".odt", ".csv", 
        ".epub", ".md", ".tex", ".xls", ".ods", ".ppt", ".pages", ".wpd", ".ps", ".latex", ".srt", 
        ".mobi", ".azw3"
    ],
    "Audio": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".alac", ".aiff", ".opus", 
        ".mka", ".amr", ".midi", ".mid", ".caf", ".pcm", ".aif", ".ra", ".rm", ".wv", ".dts"
    ],
    "Videos": [
        ".mp4", ".mkv", ".mov", ".avi", ".webm", ".flv", ".m4v", ".mpeg", ".mpg", ".wmv", 
        ".3gp", ".rmvb", ".ts", ".vob", ".ogv", ".swf", ".f4v", ".m2ts", ".divx", ".xvid", ".h264"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".tar.gz", ".tar.bz2", ".tar.xz", ".gzip", ".bzip2", 
        ".xz", ".lzma", ".ace", ".z", ".tar.lz", ".arj", ".cab", ".iso", ".img", ".dmg", ".udf"
    ],
    "Scripts": [
        ".py", ".js", ".html", ".css", ".sh", ".bat", ".php", ".ts", ".pl", ".rb", ".cpp", 
        ".c", ".h", ".java", ".swift", ".go", ".tsv", ".xml", ".json", ".yaml", ".ini", ".conf", 
        ".bash", ".sql", ".vbs", ".tcl", ".ps1", ".fsh", ".scala", ".clj", ".r", ".lua", ".as", ".dart"
    ],
    "Executables": [
        ".exe", ".msi", ".apk", ".jar", ".dmg", ".pkg", ".bat", ".app", ".appimage", ".deb", 
        ".rpm", ".bin", ".run", ".wsf", ".vbe", ".scr", ".sys", ".gadget", ".xpi", ".cmd"
    ],
    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2", ".eot", ".svg", ".fnt", ".fon", ".pfb", ".afm"
    ],
    "Spreadsheets": [
        ".ods", ".xls", ".xlsx", ".csv", ".tsv", ".xlsm", ".xltx", ".xltm", ".ods", ".numbers"
    ],
    "Presentations": [
        ".ppt", ".pptx", ".odp", ".key", ".potx", ".potm", ".ppsx"
    ],
    "Databases": [
        ".sql", ".sqlite", ".db", ".mdb", ".accdb", ".dbf", ".csv"
    ],
    "Miscellaneous": [
        ".json", ".xml", ".log", ".yml", ".yaml", ".md", ".txt", ".csv", ".ini", ".toml", ".nfo",
        ".torrent", ".vtt", ".srt", ".xls", ".xlsx", ".bson"
    ],
    "Web Files": [
        ".html", ".css", ".js", ".php", ".json", ".xml", ".asp", ".jsp", ".cgi", ".svg", ".ejs", 
        ".less", ".scss", ".ts", ".twig", ".handlebars", ".hbs", ".yaml", ".yml"
    ]
}

# Function to create dummy content for files
def create_dummy_content(extension):
    content = ''
    if extension in [".txt", ".docx", ".pdf", ".rtf", ".md", ".tex", ".csv", ".xls", ".xlsx"]:
        content = "This is a dummy text-based file."
    elif extension in [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"]:
        content = "This is a dummy audio file (won't play audio)."
    elif extension in [".mp4", ".mkv", ".mov", ".avi", ".webm", ".flv"]:
        content = "This is a dummy video file (won't play video)."
    elif extension in [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"]:
        content = "This is a dummy image file (not a real image)."
    elif extension in [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"]:
        content = "This is a dummy archive file."
    elif extension in [".py", ".js", ".html", ".css", ".sh", ".bat", ".php"]:
        content = f"// Dummy {extension} file"
    elif extension in [".exe", ".msi", ".apk"]:
        content = "This is a dummy executable file (won't execute)."
    elif extension in [".ttf", ".otf", ".woff", ".woff2"]:
        content = "This is a dummy font file."
    elif extension in [".sql", ".sqlite", ".db", ".mdb", ".accdb"]:
        content = "This is a dummy database file."
    elif extension in [".json", ".xml", ".log", ".yml", ".yaml"]:
        content = "{}"  # Empty JSON as a placeholder
    else:
        content = "This is a dummy file for other file types."
    
    return content

# Function to create dummy files in a single folder
def create_dummy_files(base_directory):
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)

    # Create one dummy file for each extension
    for category, extensions in file_categories.items():
        for ext in extensions:
            file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + ext
            file_path = os.path.join(base_directory, file_name)

            # Create and write dummy content to the file
            with open(file_path, 'w') as file:
                content = create_dummy_content(ext)
                file.write(content)
            print(f"Created dummy file: {file_path}")

if __name__ == "__main__":
    # Ask the user for the base directory
    base_directory = input("Please enter the path to the destination directory: ")
    
    # Ensure the input path is valid
    if not base_directory:
        print("Error: Please provide a valid directory path.")
    else:
        create_dummy_files(base_directory)
