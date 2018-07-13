'''term_ranking_scraper.py

The following file is used to scrap all words from a transcript of an episode of Goblin (도깨비) to find the most common words used to later rank a list of suggested words.

'''
import json
import re
from collections import Counter

INPUT_FILE_TEMPLATE = 'goblin_dialogs/도깨비 Episode_{}.txt'
REGEX = r"[\!…\\a-zA-z\d (),/~\t0-9.?:;’'-_<>\"|`★]+"
NUMBER_OF_FILES = 16
OUTPUT_FILE = "korean_term_ranking.json"

def main():

    korean_counter = Counter()

    for n in range(1,NUMBER_OF_FILES+1):
        print_file_name(n)
        
        with open(INPUT_FILE_TEMPLATE.format(n), 'r') as file:
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

def print_file_name(n):
    print("Extracting words from: " + INPUT_FILE_TEMPLATE.format(n))

if __name__ == '__main__':
    main()