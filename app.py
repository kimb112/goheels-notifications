from flask import Flask, render_template, request
from requests.models import Response

import json

# from bs4 import BeautifulSoup

with open('./index.json', 'r') as myfile:
    data = myfile.read()
sports_list: list[dict[str, str]] = json.loads(data)

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', sports=sports_list)

@app.route("/sports", methods=["POST"])
def sports():
    # teams: list[dict[str, str]] = json.loads(sports())
    if request.method == "POST":
        type_of_sports: str = request.form["sports"]
        if type_of_sports == "basketball":
        # if type_of_sports == "basketball":
            return render_template('sports.html', sports=sports_list)
        return render_template('sports.html', sports=sports_list)

if __name__ == '__main__':
    app.run(debug=True)