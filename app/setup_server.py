"""setup_server.py

The following script sets up the API service by generate the rich data to serve.

"""
import sys
sys.path.append("..")

from app.constants import ROOT_DIR
from app.server_setup.server_setup_functions import (
    add_count_to_words_in_dict,
    build_trie_with_terms_and_definitions,
    extract_simple_dict_with_definitions,
    generate_autocomplete_wordlist,
    get_config,
    merge_dictionaries,
    parse_files,
)


def main():
    config = get_config(f"{ROOT_DIR}/server_setup/server_config.json")
    resources_path = config["resources_path"]
    input_data = config['input_data']

    parse_files(input_data, resources_path)

    list_of_dicts = list(map(lambda obj: obj['output_file'], input_data))

    merge_dictionaries(list_of_dicts, resources_path)

    extract_simple_dict_with_definitions('merged_dictionaries.json', resources_path)

    add_count_to_words_in_dict("simple_korean_dict.json", "korean_term_ranking.json", resources_path)

    build_trie_with_terms_and_definitions('simple_korean_dict_with_count.json', resources_path)

    generate_autocomplete_wordlist('final_dump.json', resources_path)

    print("\tComplete setting up server data")


if __name__ == "__main__":
    main()
