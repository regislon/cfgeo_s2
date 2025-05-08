from pathlib import Path
import re

BALISE = "</style2>"
IMAGE_FOLDER_NAME = "images_documentation"



def find_markdown_files_to_convert():
    current_file = Path(__file__)
    project_path = current_file.parent.parent
    list_of_files = list(project_path.rglob("*.md"))
    list_of_files = [
        file for file in list_of_files 
        if BALISE in file.read_text(encoding="utf-8", errors="ignore").strip()
    ]
    return list_of_files


def remove_text_from_markdown_files(markdown_files):
    print("Removing text from markdown files...")

    list_images = []




    for file_path in markdown_files:
        print(f"Processing file: {file_path}")
        trigger = False
        list_of_line = []
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for line in content.splitlines():
                if line.strip() == BALISE:
                    trigger = True
                    continue
                if trigger:
                    if line.strip() != "---":
                        match = re.search(r'!\[.*?\]\((.*?)\)', line)
                        if match:
                            line = line.replace("](", f"]({IMAGE_FOLDER_NAME}/")

                            list_images.append(match.group(1))
                        list_of_line.append(line)
   
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in list_of_line:
                file.write(line + '\n')

        parent_folder = file_path.parent
        for image in list_images:
            image_path = parent_folder / image
            if image_path.exists():
                new_image_path = parent_folder / IMAGE_FOLDER_NAME / image
                new_image_path.parent.mkdir(parents=True, exist_ok=True)
                image_path.rename(new_image_path)
                print(f"Moved {image} to {new_image_path}")
            else:
                print(f"Image {image} not found in {parent_folder}")

        
            

    print(list_images)
remove_text_from_markdown_files(find_markdown_files_to_convert())
