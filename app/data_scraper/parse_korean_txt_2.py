'''korean_dict_parser_type_1.py 

Korean dictionary parser for type 2 text files
'''

import json

from word_functions import generate_korean_dictionary_type_2

INPUT_FILE = "../txt/6000_p2.txt"
OUTPUT_FILE = "../json/korean_dict_6000_part_2.json"

def main():
    # Read korean word file

    print(f"Reading {INPUT_FILE}\n")

    with open(INPUT_FILE, 'r') as file:
        raw_content_2 = file.readlines()

    k_dict = generate_korean_dictionary_type_2(raw_content_2)

    # # Write to file
    with open(OUTPUT_FILE, "w") as file:
        json.dump(k_dict, file, ensure_ascii=False)

    print(F'''
        Completed writing to {OUTPUT_FILE}
        Total words written to file: {len(k_dict)}
         ''')


if __name__ == '__main__':
    main()
