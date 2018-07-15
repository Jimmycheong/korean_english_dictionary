"""Korean word writer
"""

import json

from word_functions import strip_and_sub_using_regex

INPUT_FILE = "../json/final_dump.json"
OUTPUT_FILE = "../txt/autocomplete_word_list.txt"

REGEX = r"[\!…\\a-zA-z\d (),/~\t0-9.?:;’'-_<>\"|`]+"


def main():
    # Read korean word file

    print(f"\tReading {INPUT_FILE}\n")

    with open(INPUT_FILE) as file:
        data = json.load(file)

    # Write to file
    with open(OUTPUT_FILE, "w") as file:
        for obj in data:

            cleaned = strip_and_sub_using_regex(REGEX, str(obj['word']))
            if cleaned != "":
                file.writelines(cleaned + "\n")

    print(F'''
        Completed writing to {OUTPUT_FILE}
        Total words written to file: {len(data)}
         ''')


if __name__ == '__main__':
    main()
