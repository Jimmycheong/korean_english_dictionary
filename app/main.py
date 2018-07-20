"""main.py

Flask application to serve search engine logic

"""

import sys
sys.path.append("..")

import pickle
from flask import (
    Flask,
    request,
    make_response,
    render_template,
    jsonify
)
from app.trie_builder.trie_functions import (
    look_for_words_beginning_with_prefix,
    look_for_ranked_words_beginning_with_prefix,
    find_definition,
    update_definition
)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

TRIE_FILE = "resources/pickles/korean_pickle.pkl"
NO_OF_AUTOCOMPLETE_SUGGESTIONS = 15

with open(TRIE_FILE, 'rb') as file:
    trie = pickle.load(file)


@app.route("/", methods=['GET'])
def index():
    resp = make_response(render_template('index.html'), 200)
    return resp


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


@app.route("/search/<term>")
def search_for_term(term):
    suggestions = look_for_words_beginning_with_prefix(trie, term)

    top_20_suggestions = suggestions[:15]
    print("Returning: ", top_20_suggestions)

    return jsonify(top_20_suggestions)


@app.route("/ranked_search/<term>")
def ranked_search_for_term(term):
    suggestions = look_for_ranked_words_beginning_with_prefix(trie, term)

    top_suggestions = list(map(lambda x: x[0], suggestions[:NO_OF_AUTOCOMPLETE_SUGGESTIONS]))

    print("Returning ranked suggestions: ", top_suggestions)

    return jsonify(top_suggestions)


@app.route("/definition/<term>")
def find_definition_of_term(term):
    stripped = term.strip()
    definition = find_definition(trie, stripped)

    print(f"Searched for the term: '{term}'\
            Definition: {definition} \
            with strip")

    return jsonify({stripped: definition})


@app.route("/update", methods=['POST'])
def update_definition_of_term():
    term = request.json["term"]
    intended_definition = request.json["new_definition"]

    old_definition = find_definition(trie, term)
    new_trie = update_definition(trie, term, intended_definition)

    # Ideally in the future, this will be a list of recommended terms to be reviewed.
    # Also writing a new trie may be intensive.

    with open(TRIE_FILE, 'wb') as file:
        pickle.dump(new_trie, file)

    response = {
        "term": term,
        "old_definition": old_definition,
        "new_definition": intended_definition
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
