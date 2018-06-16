'''Korean word writer
'''

import json
from functions.word_functions import strip_and_sub_using_regex

INPUT_FILE = "resources/final_dump.json"
OUTPUT_FILE = "resources/big_korean_word_list.txt"

def main():

    # Read korean word file

    print(f"\tReading {INPUT_FILE}\n")

    with open(INPUT_FILE) as file:
        data = json.load(file)

    # Write to file
    with open(OUTPUT_FILE, "w") as file:
        for obj in data:

            cleaned = strip_and_sub_using_regex(str(obj['word']))
            if cleaned != "":
                file.writelines(cleaned+"\n")

    print(F'''
        Completed writing to {OUTPUT_FILE}
        Total words written to file: {len(data)}
         ''')

if __name__ == '__main__':
    main()
