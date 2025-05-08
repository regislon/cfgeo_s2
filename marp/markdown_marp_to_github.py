from pathlib import Path

BALISE = "</style2>"



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
                    list_of_line.append(line)
   
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in list_of_line:
                file.write(line + '\n')
            


remove_text_from_markdown_files(find_markdown_files_to_convert())
