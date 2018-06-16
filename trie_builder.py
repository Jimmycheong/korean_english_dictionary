'''trie_builder.py
'''

import pickle
import json

from functions.trie_functions import (
    create_root_node,
    add_word_to_trie
)

from console_progressbar import ProgressBar

INPUT_FILE = "resources/korean_dict.json"
OUTPUT_FILE = "resources/korean_pickle.pkl"

def main():

    with open(INPUT_FILE) as file:
        data = json.load(file)

    total = len(data)
    
    print(f"\n\tSize of word document: {total}\n\n")

    trie = create_root_node()
    
    pb = ProgressBar(total=total,prefix='Start', suffix='Complete', decimals=2, length=50)

    current = 0
    for word in data: 
        add_word_to_trie(trie, word, data[word])
        current +=1
        pb.print_progress_bar(current)

    print('''\tFinished inserting words into tree \n \
        \tCreating and saving pickle...
        ''')

    with open(f"{OUTPUT_FILE}", 'wb') as file: 
        pickle.dump(trie, file)    

    print("\tDone!\n")

if __name__ == '__main__':
    main()