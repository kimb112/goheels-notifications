from flask import Flask, render_template, request
from requests.models import Response

import json

# from bs4 import BeautifulSoup

with open('./basketball.json', 'r') as myfile:
    basketball = myfile.read()
basketball_list: list[dict[str, str]] = json.loads(basketball)

with open('./football.json', 'r') as myfile:
    football = myfile.read()
football_list: list[dict[str, str]] = json.loads(football)

with open('./soccer.json', 'r') as myfile:
    soccer = myfile.read()
soccer_list: list[dict[str, str]] = json.loads(soccer)

app: Flask = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        type_of_sports: str = request.form["sports"]
        if type_of_sports == "basketball":
            return render_template('index.html', sports=basketball_list)
        if type_of_sports == "football":
            return render_template('index.html', sports=football_list)
        if type_of_sports == "soccer":
            return render_template('index.html', sports=soccer_list)
        return render_template('index.html')
    else:
        return render_template('index.html')

# @app.route("/sports", methods=["POST"])
# def sports():
#     if request.method == "POST":
#         type_of_sports: str = request.form["sports"]
#         if type_of_sports == "basketball":
#             return render_template('sports.html', sports=basketball_list)
#         if type_of_sports == "football":
#             return render_template('sports.html', sports=football_list)
#         if type_of_sports == "soccer":
#             return render_template('sports.html', sports=soccer_list)
#         return render_template('sports.html', sports=basketball_list)

if __name__ == '__main__':
    app.run(debug=True)