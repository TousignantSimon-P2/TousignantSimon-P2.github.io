import os
import argparse

def enforce_linebreaks_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('
')
    new_lines = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()
        
        # Détection des blocs de code
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
        
        # On ne modifie pas les lignes dans un bloc de code, 
        # les tableaux (commencent par |), les en-têtes (commencent par #)
        # ou les lignes déjà vides.
        if in_code_block or stripped.startswith('|') or stripped.startswith('#') or not stripped:
            new_lines.append(line)
        else:
            # On retire les espaces de fin existants et on en ajoute 2
            new_lines.append(line.rstrip() + "  ")

    with open(file_path, 'w', encoding='utf-8', newline='
') as f:
        f.write('
'.join(new_lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enforce two spaces before line breaks in Markdown.")
    parser.add_argument("paths", nargs='+', help="Files or directories to process.")
    args = parser.parse_args()

    for path in args.paths:
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for f in files:
                    if f.endswith('.md'):
                        print(f"Processing {f}...")
                        enforce_linebreaks_file(os.path.join(root, f))
        elif os.path.isfile(path):
            print(f"Processing {path}...")
            enforce_linebreaks_file(path)
