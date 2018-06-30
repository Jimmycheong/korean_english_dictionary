'''test_setup_server.py

A test for server setup functions

'''
import os
from grappa import should
from pathlib import Path
import pytest
import json
from typing import List, Dict

from setup_server import (
    get_config,
    parse_text_file,
    parse_files,
    merge_dictionaries,
    read_data_file,
    extract_simple_dict_with_definitions,
    generate_autocomplete_wordlist,
    build_trie_with_terms_and_definitions
)

'''
Fixtures
'''

@pytest.fixture
def config_fixture():
    config = [
        {
            "input_file": 'word_data_format_1.txt',
            "extension": 'txt',
            "data_format": 1,
            "output_file": "test_data_format_1.json"
        },{
            "input_file": 'word_data_format_2.txt',
            "extension": 'txt',
            "data_format": 2,
            "output_file": "test_data_format_2.json"
        },{
            "input_file": 'word_data_format_3.json',
            "extension": 'json',
            "data_format": 3,
            "output_file": "test_data_format_3.json"
        }]
    return config

'''
TESTS
'''

TEST_RESOURCES_PATH = "tests/resources"

def test_get_config():

    config = get_config("config.json")

    expected_keys = [
        'final_dump_url', 
        'merged_file_name', 
        'simple_korean_dict',
        'input_data'
    ]

    list(config.keys()) | should.be.equal.to(expected_keys)
    config['final_dump_url'] | should.be.equal.to("http://benhumphreys.ca/kdict/kdict_dump.json")

def test_parse_text_file_for_data_format_1(config_fixture):

    obj = config_fixture[0]

    output_path = create_path_obj_for_json(obj['output_file'])

    parse_text_file(obj, TEST_RESOURCES_PATH)

    output_path.exists() | should.be.true

    os.remove(output_path)
    # TODO: remember to use test files and delete them!

def test_parse_text_file_for_data_format_2(config_fixture):

    obj = config_fixture[1]

    output_path = create_path_obj_for_json(obj['output_file'])

    parse_text_file(obj, TEST_RESOURCES_PATH)

    output_path.exists() | should.be.true

    os.remove(output_path)

    # TODO: remember to use test files and delete them!

def test_parse_text_file_for_data_format_3(config_fixture):

    obj = config_fixture[2]

    output_path = create_path_obj_for_json(obj['output_file'])

    parse_text_file(obj, TEST_RESOURCES_PATH)
    output_path.exists() | should.be.true

    os.remove(output_path)
    # TODO: remember to use test files and delete them!

def test_parse_files(config_fixture):
    
    input_files = config_fixture
    output_files = list(map(lambda obj: obj['output_file'],config_fixture))

    parse_files(input_files, TEST_RESOURCES_PATH)

    for filepath in output_files: 
        output_path = create_path_obj_for_json(filepath)
        output_path.exists() | should.be.true
        # os.remove(output_path)

@pytest.mark.run(after='test_parse_files')
def test_merge_dictionaries(config_fixture):

    list_of_dicts = list(map(lambda obj: obj['output_file'],config_fixture))

    merge_dictionaries(list_of_dicts, TEST_RESOURCES_PATH)

    merged_dict_path = create_path_obj_for_json('merged_dictionaries.json')
    merged_dict_path.exists() | should.be.true

def test_read_data_file(config_fixture):

    output_file = config_fixture[0]['output_file']
    full_path = f"{TEST_RESOURCES_PATH}/json/{output_file}"

    json_data = read_data_file(full_path, 'json') 

    assert type(json_data) == list
    assert type(json_data[0]) == dict

@pytest.mark.run(after='test_merge_dictionaries')
def test_extract_simple_dict_with_definitions(config_fixture):

    merged_dictionaries = "merged_dictionaries.json"
    simple_korean_dict_name = "simple_korean_dict.json"

    extract_simple_dict_with_definitions(merged_dictionaries, TEST_RESOURCES_PATH)

    simple_dict_path = create_path_obj_for_json('simple_korean_dict.json')

    simple_dict_path.exists() | should.be.true


def test_generate_autocomplete_wordlist(config_fixture):

    data_format_3_file = config_fixture[2]['input_file']

    data_format_3 = read_data_file(f"{TEST_RESOURCES_PATH}/json/{data_format_3_file}", 'json')

    generate_autocomplete_wordlist(data_format_3_file, TEST_RESOURCES_PATH)
    
    autocomplete_words_filepath = create_path_obj_for_txt("autocomplete_word_list.txt")

    autocomplete_words_filepath.exists() | should.be.true
    
    num_lines_in_created_file = sum(1 for line in open(f"{TEST_RESOURCES_PATH}/txt/autocomplete_word_list.txt"))

    num_lines_in_created_file | should.be.equal(len(data_format_3))


def test_build_trie_with_terms_and_definitions():

    data_file = "simple_korean_dict.json"

    build_trie_with_terms_and_definitions(data_file, TEST_RESOURCES_PATH)

    pickle_path = create_path_obj_for_pickle("korean_pickle.pkl")
    pickle_path.exists() | should.be.true


'''
TEST HELPER METHODS
'''

def create_path_obj_for_json(file: str):
    return Path(f"{TEST_RESOURCES_PATH}/json/{file}")

def create_path_obj_for_txt(file: str):
    return Path(f"{TEST_RESOURCES_PATH}/txt/{file}")

def create_path_obj_for_pickle(file: str):
    return Path(f"{TEST_RESOURCES_PATH}/pickles/{file}")













