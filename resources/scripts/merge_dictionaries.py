'''Korean dictionary merger
'''

import json

LIST_OF_DICTIONARIES = [
    '../json/korean_dict_6000_part_1.json',
    '../json/korean_dict_6000_part_2.json',
    '../json/korean_dict_6000_part_3.json',
]

OUTPUT_FILE = "../json/merged_dictionaries.json"

def main():
    # Read korean word file
    merged = []

    for filename in LIST_OF_DICTIONARIES:
        print(f"\n\tReading {filename}")
        with open(filename) as file:
            merged += json.load(file)

    # # Write to file
    with open(OUTPUT_FILE, "w") as file:
        json.dump(merged, file, ensure_ascii=True)

    print(F'''
        Completed writing to {OUTPUT_FILE}
        Total objects written to file: {len(merged)}
         ''')

if __name__ == '__main__':
    main()
