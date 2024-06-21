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


print("hello world!")