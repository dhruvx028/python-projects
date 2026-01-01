"""
Count files by extension inside a directory.

This script scans a directory and counts how many files
exist for each extension type.
"""
import argparse
import os
parser = argparse.ArgumentParser(
    description="Count files by extension inside a directory"
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
txt_count = 0
csv_count = 0
other_count = 0


for file in files:
    source = os.path.join(DIRECTORY, file)
    # Skip directories
    if os.path.isdir(source):
        continue
    elif file.endswith('.txt'):
        txt_count += 1
    elif file.endswith('.csv'):
        csv_count += 1
    else:
        other_count += 1
print(f"Number of .txt files: {txt_count}")
print(f"Number of .csv files: {csv_count}")
print(f"Number of other files: {other_count}")