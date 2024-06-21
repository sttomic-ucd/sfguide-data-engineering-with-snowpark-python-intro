import sys
import os
import yaml

ignore_folders = ['.git', '__pycache__', '.ipynb_checkpoints']
snowflake_project_config_filename = 'snowflake.yml'

if len(sys.argv) != 2:
    print("Root directory is required")
    exit()

root_directory = sys.argv[1]
print(f"Deploying all Snowpark apps in root directory {root_directory}")

# Walk the entire directory structure recursively
for (directory_path, directory_names, file_names) in os.walk(root_directory):
    # Get just the last/final folder name in the directory path
    base_name = os.path.basename(directory_path)

    # Skip any folders we want to ignore
    if base_name in ignore_folders:
#        print(f"Skipping ignored folder {directory_path}")
        continue

    # An snowflake.yml file in the folder is our indication that this folder contains
    # a Snow CLI project
    if not snowflake_project_config_filename in file_names:
#        print(f"Skipping non-app folder {directory_path}")
        continue
    print(f"Found Snowflake project in folder {directory_path}")

print("hello world!")