# Copyright is waived. No warranty is provided. Unrestricted use and modification is permitted.

import sys

PURPOSE = """\
Search for a string in a binary file

search-binary.py <input_path> <string>
"""


if __name__ == '__main__':

    if len(sys.argv) < 3:
        sys.exit(PURPOSE)
    input_path = sys.argv[1]
    search_string = sys.argv[2].encode('latin-1')

    with open(input_path, 'rb') as f:
        file_data = f.read()

    search_range = len(file_data) - len(search_string)
    for i in range(search_range):
        if file_data[i:i+len(search_string)] == search_string:
            print ('found at offset {0}'.format(i))
