import os
import yaml
import requests

# Directories
script_dir = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(script_dir, 'config.yaml')
website_dir = os.path.join(script_dir, '../website/src/content/docs/printers')

# Make sure the website directory exists
os.makedirs(website_dir, exist_ok=True)

# Function to download a markdown file and create metadata within the file
def download_and_create_metadata(url, title, description, project_name, file_name):
    # If file_name is provided in the config, use it; otherwise, use the basename of the URL
    if file_name:
        filename = file_name
    else:
        filename = os.path.basename(url)

    file_path = os.path.join(website_dir, filename)

    # Download the markdown file
    print(f"Downloading {filename} from {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        # Create metadata to prepend to the file
        metadata = f"""---
title: "{title}"
description: "{description}"
project_name: "{project_name}"
repository: "{url}"
---
"""

        # Write metadata + markdown content to the file
        with open(file_path, 'wb') as f:
            f.write(metadata.encode('utf-8'))  # Write metadata first
            f.write(response.content)  # Then write the markdown content
        print(f"Downloaded {filename} to {file_path} with metadata")

    else:
        print(f"Failed to download {filename} from {url}. Status code: {response.status_code}")

# Parse the config.yaml file
def parse_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    # Iterate over each project in the YAML file
    for project_name, project_info in config.items():
        title = project_info.get('title')
        description = project_info.get('description')
        repository = project_info.get('repository')
        file_name = project_info.get('file_name', None)  # Default to None if not provided

        if not file_name.endswith('.md'):
            print(f"Skipping project {project_name} due to invalid file name")
            continue
        if title and description and repository:
            download_and_create_metadata(repository, title, description, project_name, file_name)
        else:
            print(f"Skipping project {project_name} due to missing required fields")

# Main function to execute the script
def main():
    if not os.path.isfile(config_file):
        print(f"Error: {config_file} not found.")
        return
    
    parse_config(config_file)
    print("Finished processing printer files.")

if __name__ == '__main__':
    main()
