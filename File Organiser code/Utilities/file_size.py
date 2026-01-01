"""
Calculate total file sizes by extension inside a directory.

This script scans the 'FILES' directory and calculates the total
size of .txt, .csv, and .py files (excluding subdirectories).
"""
import argparse
import os
parser = argparse.ArgumentParser(
    description="Calculate total file sizes by extension in a directory"
)
parser.add_argument(
    "directory",
    help="Path to the directory to scan"
)
args = parser.parse_args()
DIRECTORY = args.directory
if not os.path.isdir(DIRECTORY):
    print(f"Error: '{DIRECTORY}' is not a valid directory")
    exit(1)
files = os.listdir(DIRECTORY)
txt_size = 0
csv_size = 0
py_size = 0

# Iterate through all files in the directory
for name in files:
    source = os.path.join(DIRECTORY, name)
    # Skip directories
    if os.path.isdir(source):
        continue
    elif name.endswith('.txt'):
        size = os.path.getsize(source)
        txt_size += size
    elif name.endswith('.csv'):
        size = os.path.getsize(source)
        csv_size += size
    elif name.endswith('.py'):
        size = os.path.getsize(source)
        py_size += size

print(f'Total size of .txt files: {txt_size} bytes')
print(f'Total size of .csv files: {csv_size} bytes')
print(f'Total size of .py files: {py_size} bytes')