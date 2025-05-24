import json
import sys
from lib2to3.pgen2 import driver
from lib2to3.refactor import RefactoringTool, get_fixers_from_package

# Prepare the list of fixers for 2to3
fixers = get_fixers_from_package('lib2to3.fixes')
refactoring_tool = RefactoringTool(fixers)

def apply_2to3(code_string):
    """Applies 2to3 transformations to a Python code string."""
    try:
        tree = driver.parse_string(code_string)
        refactoring_tool.refactor(tree)
        return str(tree)
    except Exception as e:
        # print(f"Error during 2to3 conversion: {e}\nProblematic code:\n{code_string}", file=sys.stderr)
        return code_string

def convert_notebook_format_and_metadata(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    original_nbformat = notebook.get('nbformat', 4) # Default to 4 if not present

    # Update to nbformat 4
    notebook['nbformat'] = 4
    notebook['nbformat_minor'] = 5

    if original_nbformat < 4:
        # For nbformat 3, cells are in worksheets.
        # Also, code cell content is in 'input' field.
        if 'worksheets' in notebook and len(notebook['worksheets']) > 0:
            current_cells = notebook['worksheets'][0].get('cells', [])
            new_cells = []
            for cell_data in current_cells:
                if cell_data.get('cell_type') == 'code':
                    if 'input' in cell_data: # nbformat 3 uses 'input'
                        cell_data['source'] = cell_data.pop('input')
                new_cells.append(cell_data)
            notebook['cells'] = new_cells
            del notebook['worksheets']
        elif 'cells' not in notebook: # Should not happen if worksheets existed
            notebook['cells'] = []
    elif 'cells' not in notebook: # nbformat 4 but no cells array
        notebook['cells'] = []


    if 'metadata' not in notebook:
        notebook['metadata'] = {}
    
    notebook['metadata']['kernelspec'] = {
        "name": "python3",
        "display_name": "Python 3 (ipykernel)",
        "language": "python"
    }
    notebook['metadata']['language_info'] = {
        "name": "python",
        "version": "3.11.12",
        "mimetype": "text/x-python",
        "codemirror_mode": {"name": "ipython", "version": 3},
        "pygments_lexer": "ipython3",
        "nbconvert_exporter": "python",
        "file_extension": ".py"
    }

    for cell in notebook.get('cells', []):
        if 'metadata' not in cell: # Ensure metadata field exists for all cells
            cell['metadata'] = {}
        
        if cell['cell_type'] == 'code':
            cell['outputs'] = [] # Clear outputs
            cell['execution_count'] = None # Clear execution count
            
            source_content = cell.get('source', []) # Now 'source' should exist
            
            if isinstance(source_content, str):
                source_lines = source_content.splitlines(keepends=True)
            else: # It's a list of strings
                source_lines = [line if line.endswith(('\n', '\r\n')) else line + '\n' for line in source_content]

            new_source_lines = []
            pylab_replaced = False
            for line_idx, line in enumerate(source_lines):
                if '%pylab inline' in line or '%matplotlib inline' in line:
                    if not pylab_replaced:
                        new_source_lines.append("import numpy as np\n")
                        new_source_lines.append("import matplotlib.pyplot as plt\n")
                        pylab_replaced = True
                else:
                    new_source_lines.append(line)
            
            code_to_convert = "".join(new_source_lines)
            converted_code = apply_2to3(code_to_convert)
            
            if isinstance(source_content, str):
                cell['source'] = converted_code
            else:
                # Preserve original line endings if possible, or just splitlines
                # This logic attempts to restore list-of-strings format
                converted_lines = converted_code.splitlines(keepends=True)
                if not converted_lines and converted_code: # single line without newline
                    converted_lines = [converted_code]
                
                # Avoid making source ['\n'] if it was originally empty or just whitespace
                if not any(s.strip() for s in source_content) and \
                   (not converted_lines or (len(converted_lines) == 1 and converted_lines[0].isspace())):
                    cell['source'] = []
                else:
                    cell['source'] = converted_lines


    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
        f.write('\n')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        notebook_file_path = sys.argv[1]
        convert_notebook_format_and_metadata(notebook_file_path)
        print(f"Notebook '{notebook_file_path}' updated successfully.")
    else:
        print("Usage: python update_notebook.py <path_to_notebook.ipynb>")
