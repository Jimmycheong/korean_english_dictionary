"""Korean word writer
"""

import json

INPUT_FILE = "../json/merged_dictionaries.json"
OUTPUT_FILE = "../json/korean_dict.json"


def main():
    # Read korean word file

    print(f"\tReading {INPUT_FILE}\n")

    with open(INPUT_FILE) as file:
        data = json.load(file)

    dict_ = {}

    for obj in data:
        if obj["term"] not in dict_:
            dict_[obj["term"]] = obj["definition"]

    with open(OUTPUT_FILE, "w") as file:
        json.dump(dict_, file, ensure_ascii=False)

    print(F'''
        Completed writing to {OUTPUT_FILE}
        Total words written to file: {len(dict_)}
         ''')


if __name__ == '__main__':
    main()
