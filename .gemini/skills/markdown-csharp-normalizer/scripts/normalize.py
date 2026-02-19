import os
import re
import argparse

def normalize_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Convert CRLF to LF
    content = content.replace('
', '
')
    lines = content.split('
')
    new_lines = []
    in_code_block = False
    code_block_lines = []
    lang_line = ''

    def flush_code_block(lines_list, current_lang_line):
        if not lines_list:
            return [current_lang_line, '```']
        
        # Find minimum non-empty indentation
        min_indent = 999
        for l in lines_list:
            if l.strip():
                indent = len(l) - len(l.lstrip())
                if indent < min_indent:
                    min_indent = indent
        
        if min_indent == 999: min_indent = 0
        
        processed = [current_lang_line]
        for l in lines_list:
            if l.strip():
                processed.append(l[min_indent:])
            else:
                processed.append('')
        processed.append('```')
        return processed

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('```'):
            if in_code_block:
                new_lines.extend(flush_code_block(code_block_lines, lang_line))
                code_block_lines = []
                in_code_block = False
            else:
                in_code_block = True
                # Normalize marker to ```csharp
                m = re.match(r'^\s*```\s*(c#|csharp)?(.*)', line)
                if m:
                    lang = 'csharp'
                    extra = m.group(2).strip()
                    lang_line = f'```{lang}'
                    if extra:
                        lang_line += f' {extra}'
                else:
                    lang_line = '```'
            continue
        
        if in_code_block:
            code_block_lines.append(line)
        else:
            new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8', newline='
') as f:
        f.write('
'.join(new_lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Normalize Markdown C# code blocks.")
    parser.add_argument("paths", nargs='+', help="Files or directories to normalize.")
    args = parser.parse_args()

    for path in args.paths:
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for f in files:
                    if f.endswith('.md'):
                        print(f"Normalizing {f}...")
                        normalize_file(os.path.join(root, f))
        elif os.path.isfile(path):
            print(f"Normalizing {path}...")
            normalize_file(path)
