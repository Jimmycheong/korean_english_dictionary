'''Korean word writer
'''

import json

INPUT_FILE = "resources/final_dump.json"
OUTPUT_FILE = "resources/korean_dict.json"

def main():

    # Read korean word file

    print(f"\tReading {INPUT_FILE}\n")

    with open(INPUT_FILE) as file:
        data = json.load(file)

    dict_ = {}

    for obj in data:
        dict_[obj["word"]] = obj["def"]

    print("FINAL DICT: ", dict_)

    with open(OUTPUT_FILE, "w") as file:
        json.dump(dict_, file, ensure_ascii=False)

    print(F'''
        Completed writing to {OUTPUT_FILE}
        Total words written to file: {len(dict_)}
         ''')

if __name__ == '__main__':
    main()
