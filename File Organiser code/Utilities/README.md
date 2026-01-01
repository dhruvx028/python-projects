# File Size Analyzer (CLI)

## Description
A Python command-line tool that calculates the total size of files
by extension inside a directory.

## Features
- Calculates total size of `.txt`, `.csv`, and `.py` files
- Ignores subdirectories
- Simple command-line interface (CLI)
- Graceful error handling for invalid paths

## Requirements
- Python 3.x

## Usage
```bash
python file_size.py <directory_path>

# Example:
python file_size.py FILES

# Output:
Total size of .txt files: 2048 bytes
Total size of .csv files: 4096 bytes
Total size of .py files: 1024 bytes


