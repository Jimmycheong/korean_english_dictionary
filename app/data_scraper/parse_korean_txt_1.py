'''korean_dict_parser_type_1.py 

Korean dictionary parser for type 1 text files
'''

import json

from word_functions import (
    strip_and_sub_using_regex,
    generate_korean_dictionary_type_1,
)

INPUT_FILE = "../txt/6000_p1.txt"
OUTPUT_FILE = "../json/korean_dict_6000_part_1.json"

def main():
    # Read korean word file

    print(f"Reading {INPUT_FILE}\n")

    with open(INPUT_FILE, 'r') as file:
        raw_content = file.readlines()

    k_dict = generate_korean_dictionary_type_1(raw_content)

    # Write to file
    with open(OUTPUT_FILE, "w") as file:
        json.dump(k_dict, file)

    print(F'''
        Completed writing to {OUTPUT_FILE}
        Total words written to file: {len(k_dict)}
         ''')

if __name__ == '__main__':
    main()
