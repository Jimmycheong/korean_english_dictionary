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
import json

from functions.trie_functions import (
    look_for_words_beginning_with,
    find_definition
)


app = Flask(__name__)

with open("resources/korean_pickle.pkl", 'rb') as file:
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
