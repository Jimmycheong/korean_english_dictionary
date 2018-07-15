'''korean_dict_parser_type_1.py 

Korean dictionary parser for type 1 text files
'''

import json
from word_functions import generate_korean_dictionary_type_3

INPUT_FILE = "../json/final_dump.json"
OUTPUT_FILE = "../json/korean_dict_6000_part_3.json"


def main():
    # Read korean word file

    print(f"Reading {INPUT_FILE}\n")

    with open(INPUT_FILE) as file:
        file_data = json.load(file)

    list_of_dicts = generate_korean_dictionary_type_3(file_data)

    # Write to file
    with open(OUTPUT_FILE, "w") as file:
        json.dump(list_of_dicts, file)

    print(F'''
        Completed writing to {OUTPUT_FILE}
        Total words written to file: {len(list_of_dicts)}
         ''')


if __name__ == '__main__':
    main()
