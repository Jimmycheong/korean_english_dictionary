"""server_setup_functions.py

"""
from typing import List, Dict
import json
import os
import pickle

from console_progressbar import ProgressBar
from app.trie_builder.trie_functions import (
    create_root_node,
    add_word_to_trie
)

from app.data_scraper.word_functions import (
    generate_korean_dictionary_type_1,
    generate_korean_dictionary_type_2,
    generate_korean_dictionary_type_3,
    strip_and_sub_using_regex
)


def build_trie_with_terms_and_definitions(data_path: str, resources_path: str):
    data = read_data_file(f"{resources_path}/json/{data_path}", 'json')

    total = len(data)

    print(f"\n\tSize of word document: {total}\n\n")

    trie = create_root_node()

    pb = ProgressBar(total=total, prefix='Start', suffix='Complete', decimals=2, length=50)

    current = 0
    for word in data:
        add_word_to_trie(trie, word, data[word]['definition'], data[word]['count'])
        current += 1
        pb.print_progress_bar(current)

    print('''\tFinished inserting words into tree \n \
        \tCreating and saving pickle...
        ''')

    output_file = f"{resources_path}/pickles/korean_pickle.pkl"

    with open(f"{output_file}", 'wb') as file:
        pickle.dump(trie, file)

    print("\tDone!\n")


def generate_autocomplete_wordlist(data_resource: str, resources_path: str):
    REGEX = r"[\!…\\a-zA-z\d (),/~\t0-9.?:;’'-_<>\"|`]+"
    data = read_data_file(f"{resources_path}/json/{data_resource}", 'json')

    output_file = f"{resources_path}/txt/autocomplete_word_list.txt"

    with open(output_file, "w", encoding="utf-8") as file:
        for obj in data:
            cleaned = strip_and_sub_using_regex(REGEX, str(obj['word']))
            if cleaned != "":
                file.writelines(cleaned + "\n")

    print(F'''
        Completed writing to {output_file}
        Total words written to file: {len(data)}
         ''')


def dump_data_to_json():
    # TODO: Refactor code to dump data as json files
    pass


def extract_simple_dict_with_definitions(dense_dict_filepath: str, resources_path: str):
    print(f"\tReading {dense_dict_filepath}\n")
    data = read_data_file(f"{resources_path}/json/{dense_dict_filepath}", 'json')

    dict_of_terms = {}
    for obj in data:
        if obj['term'] not in dict_of_terms:
            dict_of_terms[obj["term"]] = {
                "definition": obj["definition"],
                "count": 0
            }

    output_file = "simple_korean_dict.json"
    with open(f"{resources_path}/json/{output_file}", "w", encoding="utf-8") as file:
        json.dump(dict_of_terms, file, ensure_ascii=False)

    print(F'''
        Completed writing to {output_file}
        Total words written to file: {len(dict_of_terms)}
         ''')


def merge_dictionaries(list_of_dicts, resources_path: str):
    """
    Merge json dictionaries together
    """

    merged = []

    for filename in list_of_dicts:
        print(f"\n\tReading {filename}")
        full_path = f"{resources_path}/json/{filename}"
        merged += read_data_file(full_path, 'json')

    with open(f"{resources_path}/json/merged_dictionaries.json", "w", encoding="utf-8") as file:
        json.dump(merged, file, ensure_ascii=True)

    print(F'''
        Completed writing merged_dictionaries.json
        Total objects written to file: {len(merged)}
         ''')


def add_count_to_words_in_dict(simple_dict_file: str, ranked_terms_file: str, resources_path: str):
    """
    Merge json dictionaries together
    """

    simple_dict = read_data_file(f"{resources_path}/json/{simple_dict_file}", "json")
    ranked_terms = read_data_file(f"{resources_path}/json/{ranked_terms_file}", "json")

    all_words_in_dict = simple_dict.keys()

    for term in ranked_terms:
        if term in all_words_in_dict:
            simple_dict[term]["count"] = ranked_terms[term]

    with open(f"{resources_path}/json/simple_korean_dict_with_count.json", "w", encoding="utf-8") as file:
        json.dump(simple_dict, file, ensure_ascii=True)

    print(F'''
        Completed writing merged_dictionaries.json
        Total objects written to file: {len(simple_dict)}
         ''')


def parse_files(list_of_objs: List[Dict], resources_path: str):
    if os.path.isdir(resources_path) != True:
        raise Exception(f"No such directory for resources: {resources_path}")

    for obj in list_of_objs:
        parse_text_file(obj, resources_path)


def parse_text_file(obj: dict, resources_path: str):
    input_file = obj['input_file']
    extension = obj['extension']
    output_file = obj['output_file']
    data_format = obj['data_format']

    input_path = f"{resources_path}/{extension}/{input_file}"
    output_path = f"{resources_path}/json/{output_file}"

    print(f"Reading {input_file}\n")

    raw_content = read_data_file(input_path, extension)

    if data_format == 1:
        k_dict = generate_korean_dictionary_type_1(raw_content)
    elif data_format == 2:
        k_dict = generate_korean_dictionary_type_2(raw_content)
    elif data_format == 3:
        k_dict = generate_korean_dictionary_type_3(raw_content)

    with open(output_path, "w") as file:
        json.dump(k_dict, file)

    print(F'''
        Completed writing to {output_path}
        Total words written to file: {len(k_dict)}
         ''')


def read_data_file(filename, extension):
    print(f"\tReading {filename}\n")

    if extension == 'txt':
        with open(filename, 'r', encoding="utf-8") as file:
            return file.readlines()
    elif extension == 'json':
        with open(filename, encoding="utf-8") as file:
            return json.load(file)
    else:
        raise Exception(f"Unknown extension: {extension}")


def get_config(filename: str) -> dict:
    with open(filename, 'r') as file:
        return json.load(file)
