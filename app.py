from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    print("entered route")
    # TODO: Extract query term from url
    search_term = request.args.get('search_term')
    # TODO: Make 'params' dict with query term and API key
    params = {"q": search_term, "key": "FSRGXSUXH8KT", "limit":10}
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/search", params=params)
    gif_json = r.json()
    print(gif_json)
    # TODO: Get the first 10 results from the search results
    gif_json = gif_json["results"]
    # TODO: Render the 'index.html' template, passing the gifs as a named parameter


    return render_template(
        'index.html',
        gif_list = gif_json)

if __name__ == '__main__':
    app.run(debug=True)
