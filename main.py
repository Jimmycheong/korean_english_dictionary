'''main.py

Flask application to serve search engine logic

'''
import pickle
import sys

from flask import (
    Flask,
    request,
    url_for,
    make_response,
    render_template,
    jsonify
)

from functions.trie_functions import (
    look_for_words_beginning_with,
    find_definition,
    update_definition
)


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

TRIE_FILE = "resources/korean_pickle.pkl"

with open(TRIE_FILE, 'rb') as file:
    trie = pickle.load(file)


@app.route("/",  methods=['GET'])
def index():
    resp = make_response(render_template('index.html'), 200)
    return resp


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


@app.route("/search/<term>")
def search_for_term(term):
    suggestions = look_for_words_beginning_with(trie, term)

    top_20_suggestions = suggestions[:15]

    return jsonify(top_20_suggestions)


@app.route("/meaning/<term>")
def find_definition_of_term(term):

    definition = find_definition(trie, term)

    print(f"Searched for the term: {term}\
            Definition: {definition}")

    return jsonify({term: definition})


@app.route("/update", methods=['POST'])
def update_definition_of_term():

    term = request.json["term"]
    intended_definition = request.json["new_definition"]

    old_definition = find_definition(trie, term)
    new_trie = update_definition(trie, term, intended_definition)

    # Idealy in the future, this will be a list of recommended terms to be reviewed. also writing a new trie may be intensive.

    with open(TRIE_FILE, 'wb') as file:
        pickle.dump(new_trie, file)

    response = {
        "term": term,
        "old_definition": old_definition,
        "new_definition": intended_definition
    }

    return jsonify(response)
