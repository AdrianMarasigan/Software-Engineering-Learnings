from flask import Flask, request

app = Flask(__name__)

# In-memory datastore for storing programming language information
in_memory_datastore = {
    "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
    # ... (other programming languages)
}

# Route for listing and creating programming languages


@app.route('/programming_languages', methods=['GET', 'POST'])
def programming_languages_route():
    if request.method == 'GET':
        return list_programming_languages()
    elif request.method == "POST":
        return create_programming_language(request.get_json(force=True))

# Function to list programming languages based on publication year range


def list_programming_languages():
    before_year = request.args.get('before_year') or '30000'
    after_year = request.args.get('after_year') or '0'
    qualifying_data = list(
        filter(
            lambda pl: int(before_year) > pl['publication_year'] > int(
                after_year),
            in_memory_datastore.values()
        )
    )
    return {"programming_languages": qualifying_data}

# Function to create a new programming language


def create_programming_language(new_lang):
    language_name = new_lang['name']
    in_memory_datastore[language_name] = new_lang
    return new_lang

# Route for getting, updating, and deleting a specific programming language


@app.route('/programming_languages/<programming_language_name>', methods=['GET', 'PUT', 'DELETE'])
def programming_language_route(programming_language_name):
    if request.method == 'GET':
        return get_programming_language(programming_language_name)
    elif request.method == "PUT":
        return update_programming_language(programming_language_name, request.get_json(force=True))
    elif request.method == "DELETE":
        return delete_programming_language(programming_language_name)

# Function to get details of a specific programming language


def get_programming_language(programming_language_name):
    return in_memory_datastore[programming_language_name]

# Function to update details of a specific programming language


def update_programming_language(lang_name, new_lang_attributes):
    lang_getting_update = in_memory_datastore[lang_name]
    lang_getting_update.update(new_lang_attributes)
    return lang_getting_update

# Function to delete a specific programming language


def delete_programming_language(lang_name):
    deleting_lang = in_memory_datastore[lang_name]
    del in_memory_datastore[lang_name]
    return deleting_lang
