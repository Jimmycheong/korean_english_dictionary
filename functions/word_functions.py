'''korean_word_functions.py


'''

import re
from typing import List

def strip_and_sub_using_regex(word):
    REGEX = r"[\!…\\a-zA-z\d (),/~\t0-9.?:;’'-_<>\"|`]+"
    pattern = re.compile(REGEX)

    cleaned = re.sub(REGEX,"",word).strip()
    return cleaned


def extract_korean_words_from_list(raw_content) -> List[str]:

    '''
    A function used to extract korean words from a list of strings

    Params: 
        raw_content (List[str]): a list of strings 

    Returns:
        all_korean_words (List[str]): a list of strings which only contain  korean words
    '''
    
    new_info = {}

    REGEX = r"[\!…\\a-zA-z\d (),/~\t0-9.?:;’'-_<>\"|`]+"
    pattern = re.compile(REGEX)

    # Find everything that matches the korean words
    counter = 0
    for line in raw_content:
        stripped = str.strip(line)
        subbed = re.sub(REGEX,"",stripped).strip()
        if subbed != "":
            new_info[counter] = subbed
            counter += 1

    # Final cleanising of list to remove ""
    all_korean_words = list(filter(lambda x: x != "" , list(new_info.values())))

    return all_korean_words