#!/bin/bash

# Target directory to start from, defaults to current directory if not specified
TARGET_DIR="${1:-.}"

# Function to rename files with spaces in their names
rename_files() {
    find "$1" -type f -name "* *" | while read -r file; do
        # Use 'mv' to rename the file
        mv "$file" "$(echo $file | tr ' ' '_')"
    done
}

# Export the function so it's available to the subshell spawned by find
export -f rename_files

# Recursively find all directories and apply the rename_files function
find "$TARGET_DIR" -type d -exec bash -c 'rename_files "$0"' {} \;

echo "Renaming complete."
