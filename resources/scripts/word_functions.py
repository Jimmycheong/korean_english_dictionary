'''korean_word_functions.py

'''

import re
from typing import List, Dict
from console_progressbar import ProgressBar

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
        subbed = re.sub(REGEX, "", stripped).strip()
        if subbed != "":
            new_info[counter] = subbed
            counter += 1

    # Final cleanising of list to remove ""
    all_korean_words = list(filter(lambda x: x != "", list(new_info.values())))

    return all_korean_words

def strip_and_sub_using_regex(regex, word):
    pattern = re.compile(regex)
    cleaned = re.sub(regex, "", word).strip()
    return cleaned

def generate_korean_dictionary_type_1(list_: List[str]) -> List[Dict[str, str]]: 

    REGEX = r"[()/~\t.?:;’'_<>\"|`]+"
    
    # Remove all unnecessary characters
    cleaned = [strip_and_sub_using_regex(REGEX, string) for string in list_]

    # Filter all "" from list
    filtered = list(filter(lambda x: x != "", cleaned))

    counter = 0 
    list_of_dicts = [] 

    while (counter < len(filtered)): 
        new_dict = {
            "wordNumber": int(filtered[counter]),
            "term": filtered[counter + 1].strip(),
            "definition": filtered[counter + 2].strip() 
        }
        list_of_dicts.append(new_dict)
        counter += 3

    return list_of_dicts

def generate_korean_dictionary_type_2(list_: List[str]) -> List[Dict[str, str]]: 
    
    list_of_dicts = [] 
    for line in list_:
        content = line.split("\t")
        try:
            new_dict = {
                "wordNumber": int(content[0]),
                "term": content[1].strip(),
                "definition": content[2].strip()
            }
            list_of_dicts.append(new_dict)
        except: 
            print("Failed at content: ", content)

    return list_of_dicts

def generate_korean_dictionary_type_3(list_of_objs) -> List[Dict[str, str]]: 

    list_of_dicts = []
    pb = ProgressBar(total=len(list_of_objs), prefix='Start',
                     suffix='Complete', decimals=2, length=50)

    counter = 0
    for obj in list_of_objs:

        new_dict = {
            "wordNumber": int(obj["wordid"]),
            "term": str.strip(str(obj["word"])),
            "definition": str.strip(str(obj["def"]))
        }
        list_of_dicts.append(new_dict)
        pb.print_progress_bar(counter)
        counter += 1

    pb.print_progress_bar(counter)

    return list_of_dicts
