'''trie_builder.py
'''

import pickle
from functions.trie_functions import (
    create_root_node,
    add_word_to_trie
)

INPUT_FILE = "../resources/korean_word_list.txt"
OUTPUT_FILE = "../resources/korean_pickle.pkl"

def main():

    with open(f"{INPUT_FILE}") as file:
        raw_content = file.readlines()

    print(f"\n\tSize of word document: {len(raw_content)}\n")

    trie = create_root_node()

    for word in raw_content: 
        add_word_to_trie(trie, word)

    print('''\tFinished inserting words into tree \n \
        \tCreating and saving pickle...
        ''')

    with open(f"{OUTPUT_FILE}", 'wb') as file: 
        pickle.dump(trie, file)    

    print("\tDone!\n")

if __name__ == '__main__':
    main()