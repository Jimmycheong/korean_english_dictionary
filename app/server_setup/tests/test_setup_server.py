"""test_setup_server.py

A test for server setup functions

"""

import os
from grappa import should
from pathlib import Path
import pytest

from app.constants import ROOT_DIR
from app.server_setup.server_setup_functions import (
    get_config,
    parse_text_file,
    parse_files,
    merge_dictionaries,
    read_data_file,
    extract_simple_dict_with_definitions,
    generate_autocomplete_wordlist,
    build_trie_with_terms_and_definitions,
    add_count_to_words_in_dict
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
        }, {
            "input_file": 'word_data_format_2.txt',
            "extension": 'txt',
            "data_format": 2,
            "output_file": "test_data_format_2.json"
        }, {
            "input_file": 'word_data_format_3.json',
            "extension": 'json',
            "data_format": 3,
            "output_file": "test_data_format_3.json"
        }]
    return config


'''
TESTS
'''

TEST_RESOURCES_PATH = f"{ROOT_DIR}/server_setup/tests/resources"
SERVER_CONFIG = "server_config.json"


def test_get_config():

    config = get_config(f"{ROOT_DIR}/server_setup/{SERVER_CONFIG}")

    expected_keys = [
        'final_dump_url',
        'resources_path',
        'merged_file_name',
        'simple_korean_dict',
        'input_data'
    ]

    list(config.keys()) | should.be.equal.to(expected_keys)
    config['final_dump_url'] | should.be.equal.to("http://benhumphreys.ca/kdict/kdict_dump.json")


def test_parse_text_file_for_data_format_1(config_fixture):
    print(f"TEST RESOURCES PATH: {TEST_RESOURCES_PATH}")

    obj = config_fixture[0]

    output_path = create_path_obj_for_json(obj['output_file'])

    parse_text_file(obj, TEST_RESOURCES_PATH)

    output_path.exists() | should.be.true

    os.remove(output_path)


def test_parse_text_file_for_data_format_2(config_fixture):
    obj = config_fixture[1]

    output_path = create_path_obj_for_json(obj['output_file'])

    parse_text_file(obj, TEST_RESOURCES_PATH)

    output_path.exists() | should.be.true

    os.remove(output_path)


def test_parse_text_file_for_data_format_3(config_fixture):
    obj = config_fixture[2]

    output_path = create_path_obj_for_json(obj['output_file'])

    parse_text_file(obj, TEST_RESOURCES_PATH)
    output_path.exists() | should.be.true

    os.remove(output_path)


def test_parse_files(config_fixture):
    input_files = config_fixture
    output_files = list(map(lambda obj: obj['output_file'], config_fixture))

    parse_files(input_files, TEST_RESOURCES_PATH)

    for filepath in output_files:
        output_path = create_path_obj_for_json(filepath)
        output_path.exists() | should.be.true


@pytest.mark.run(after='test_parse_files')
def test_merge_dictionaries(config_fixture):
    list_of_dicts = list(map(lambda obj: obj['output_file'], config_fixture))

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


@pytest.mark.run(after='test_extract_simple_dict_with_definitions')
def test_add_count_to_words_in_dict(config_fixture):
    simple_korean_dict_name = "simple_korean_dict.json"
    ranked_words = "korean_term_ranking.json"

    add_count_to_words_in_dict(simple_korean_dict_name, ranked_words, TEST_RESOURCES_PATH)

    simple_dict_path = create_path_obj_for_json('simple_korean_dict_with_count.json', )

    simple_dict_path.exists() | should.be.true


@pytest.mark.run(after='test_add_count_to_words_in_dict')
def test_generate_autocomplete_wordlist(config_fixture):
    data_format_3_file = config_fixture[2]['input_file']

    data_format_3 = read_data_file(f"{TEST_RESOURCES_PATH}/json/{data_format_3_file}", 'json')

    generate_autocomplete_wordlist(data_format_3_file, TEST_RESOURCES_PATH)

    autocomplete_words_filepath = create_path_obj_for_txt("autocomplete_word_list.txt")

    autocomplete_words_filepath.exists() | should.be.true

    num_lines_in_created_file = sum(
        1 for line in open(f"{TEST_RESOURCES_PATH}/txt/autocomplete_word_list.txt", encoding="utf-8"))

    num_lines_in_created_file | should.be.equal(len(data_format_3))


@pytest.mark.run(after='test_generate_autocomplete_wordlist')
def test_build_trie_with_terms_and_definitions():
    data_file = "simple_korean_dict_with_count.json"

    build_trie_with_terms_and_definitions(data_file, TEST_RESOURCES_PATH)

    pickle_path = create_path_obj_for_pickle("korean_pickle.pkl")
    pickle_path.exists() | should.be.true


@pytest.mark.run(after='test_build_trie_with_terms_and_definitions')
def test_clean_up_generated_files():
    files_to_remove = [
        'test_data_format_1.json',
        'test_data_format_2.json',
        'test_data_format_3.json',
        'merged_dictionaries.json',
        'simple_korean_dict.json',
        'simple_korean_dict_with_count.json'

    ]

    fullpaths_to_remove = map(lambda s: create_path_obj_for_json(s), files_to_remove)

    for file in fullpaths_to_remove:
        os.remove(file)


'''
TEST HELPER METHODS
'''


def create_path_obj_for_json(file: str):
    return Path(f"{TEST_RESOURCES_PATH}/json/{file}")


def create_path_obj_for_txt(file: str):
    return Path(f"{TEST_RESOURCES_PATH}/txt/{file}")


def create_path_obj_for_pickle(file: str):
    return Path(f"{TEST_RESOURCES_PATH}/pickles/{file}")
