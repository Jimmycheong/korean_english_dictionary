"""term_ranking_scraper.py

The following file is used to scrap all words from the transcripts from episodes 
of Goblin (도깨비) to find the most common words used to later rank a list of 
suggested words.

"""
from collections import Counter
import json
import re
import os
import sys

REGEX = r"[\!…\\a-zA-z\d (),/~\t0-9.?:;’'-_<>\"|`★]+"
OUTPUT_FILE = "../resources/json/korean_term_ranking.json"

def main(input_dir):
    korean_counter = Counter()

    for filename in os.listdir(input_dir):
        print("Extracting words from: " + filename)

        with open(input_dir + filename, 'r') as file:
            raw_content = file.readlines()

        for sentence in raw_content:
            korean_words = re.sub(REGEX, " ", sentence).strip().split()

            if len(korean_words) == 0:
                continue
            else:
                for word in korean_words:
                    korean_counter[word] += 1

    korean_term_ranking = dict(korean_counter)

    with open(OUTPUT_FILE, "w") as file:
        json.dump(korean_term_ranking, file, ensure_ascii=False)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        raise IOError("Please enter a directory containing txt files")
    
    input_dir = sys.argv[1]

    main(input_dir)
