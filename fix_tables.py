#!/usr/bin/env python3
"""
Script to process code inside markdown tables.
Replaces spaces with non-breaking spaces, except space before '#' in comments.
Spaces in comments (after '#') are also replaced with non-breaking spaces.
"""

import sys
import re


def process_code_in_table(code_content):
    """
    Process code content: replace spaces with NBSP, except space before '#'.
    Also replaces spaces in comments (after '#') with NBSP.
    
    Args:
        code_content: String containing code (without backticks)
    
    Returns:
        Processed string with spaces replaced by NBSP (except before '#')
    """
    # If code contains '#', handle the space before it specially
    if '#' in code_content:
        # Find the position of '#'
        hash_pos = code_content.find('#')
        # Check if there's a space immediately before '#'
        if hash_pos > 0 and code_content[hash_pos - 1] == ' ':
            # Process part before the space: replace all spaces with NBSP
            before_space = code_content[:hash_pos - 1].replace(' ', '\u00A0')
            # Keep the space before '#' as regular space
            # Process comment part (after '#') with NBSP
            comment_part = code_content[hash_pos:].replace(' ', '\u00A0')
            return before_space + ' ' + comment_part
        else:
            # No space before '#', process everything before '#' with NBSP
            before_hash = code_content[:hash_pos].replace(' ', '\u00A0')
            # Process comment part (after '#') with NBSP
            comment_part = code_content[hash_pos:].replace(' ', '\u00A0')
            return before_hash + comment_part
    else:
        # No '#', replace all spaces with NBSP
        return code_content.replace(' ', '\u00A0')


def process_table_line(line):
    """
    Process a single table line, finding and processing code inside backticks.
    
    Args:
        line: A line from markdown table
    
    Returns:
        Processed line with code spaces replaced
    """
    # Pattern to match code inside backticks: `...`
    # This regex finds backtick-enclosed content
    pattern = r'`([^`]+)`'
    
    def replace_code(match):
        code_content = match.group(1)
        processed_code = process_code_in_table(code_content)
        return f'`{processed_code}`'
    
    # Replace all code blocks in the line
    processed_line = re.sub(pattern, replace_code, line)
    return processed_line


def process_markdown_file(filename):
    """
    Process markdown file, fixing code in tables.
    
    Args:
        filename: Path to markdown file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{filename}': {e}", file=sys.stderr)
        sys.exit(1)
    
    processed_lines = []
    in_table = False
    
    for line in lines:
        # Check if this is a table line (starts with '|')
        if line.strip().startswith('|'):
            in_table = True
            processed_line = process_table_line(line)
            processed_lines.append(processed_line)
        else:
            # Not a table line, keep as is
            processed_lines.append(line)
            if in_table and line.strip() == '':
                # Empty line after table, reset flag
                in_table = False
    
    # Write processed content back to file
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(processed_lines)
        print(f"Successfully processed '{filename}'")
    except Exception as e:
        print(f"Error writing file '{filename}': {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) != 2:
        print("Usage: python fix_tables.py <markdown_file>", file=sys.stderr)
        sys.exit(1)
    
    filename = sys.argv[1]
    process_markdown_file(filename)


if __name__ == '__main__':
    main()

