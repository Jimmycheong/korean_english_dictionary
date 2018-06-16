'''Korean word writer
'''

import re
import csv
import random

from functions.word_functions import extract_korean_words_from_list

INPUT_FILE = "resources/txt/6000koreanwords.txt" # TO BE UPDATED
OUTPUT_FILE = "resources/txt/korean_word_list.txt"

def main():

    # Read korean word file

    print(f"\tReading {INPUT_FILE}\n")

    with open(INPUT_FILE, 'r') as file:
        raw_content = file.readlines()

    all_korean_words = extract_korean_words_from_list(raw_content)

    print("\tFirst 10 words of list: \n", all_korean_words[:10])

    # Write to file
    with open(OUTPUT_FILE, "w") as file:
        for item in all_korean_words:
            file.writelines(item + "\n")

    print(F'''
        Completed writing to {OUTPUT_FILE}
        Total words written to file: {len(all_korean_words)}
         ''')

if __name__ == '__main__':
    main()
