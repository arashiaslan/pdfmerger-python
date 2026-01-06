# PDF Merger Tool
## A simple and efficient Python script to merge multiple PDF files located in separate folders into single, consolidated PDF documents.

🌟 Features
Batch Processing: Automatically scans all subfolders in the input directory and merges them individually.
Alphabetical Ordering: Sorts PDF files alphabetically before merging to ensure the correct page sequence.
Organized Output: Saves merged files into a dedicated output folder, named after their original subfolder.
Error Handling: Intelligently skips empty folders and logs progress to the console.
📋 Prerequisites
Python 3.6 or higher
🚀 Installation
Clone or download this repository.
Install the required pypdf library using pip:
pip install pypdf
📂 How to Use
Create a folder named pdfs in the same directory as the script (if it doesn't exist).
Inside pdfs, create subfolders for each PDF set you want to merge. The name of the subfolder will become the filename of the merged PDF.
Example Directory Structure:

text

/pdf-merger-tool
├── main.py
├── pdfs/
│   ├── Project_A/
│   │   ├── file1.pdf
│   │   └── file2.pdf
│   └── Project_B/
│       └── document.pdf
Run the script:
bash

python main.py
Find your merged PDFs in the output folder.
📝 Example Output
The script provides console feedback in Indonesian:

text

✅ Berhasil gabung: output/Project_A.pdf
⚠️ Project_B kosong, dilewati
✅ Berhasil gabung: output/Reports.pdf
⚙️ Configuration
You can modify the directory paths at the top of the main.py file:

python

INPUT_DIR = "pdfs"    # Folder containing subfolders of PDFs
OUTPUT_DIR = "output" # Folder where merged PDFs will be saved
📄 License
This project is open source and available for personal and commercial use.
