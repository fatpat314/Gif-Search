from flask import Flask, render_template, request
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

TENOR_API_KEY = os.getenv("TENOR_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    print("entered route")
    # TODO: Extract query term from url
    search_term = request.args.get("search")
    # TODO: Make 'params' dict with query term and API key
    params = {"q": search_term, "key": TENOR_API_KEY, "limit":12}
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/search", params=params)
    gif_json = r.json()["results"]

    #print(gif_json)
    # TODO: Get the first 10 results from the search results
    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template('index.html', gif_list = gif_json, search_term = search_term)

if __name__ == '__main__':
    app.run(debug=True)

# For some reason the background image does not show up in Chrome or Safari.
# Works fine in Firefox
