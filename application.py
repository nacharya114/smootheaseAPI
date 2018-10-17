#app.py

import os
import json

from db import query_db

from flask import Flask
from flask import request
application = Flask(__name__)



@application.route("/")
def hello():

    return "Hello World I am Joey."

@application.route("/all")
def get_all():
    
    get_all_sql = "SELECT * FROM Recipes;"

    result = query_db(get_all_sql, (), False)

    json_out = json.dumps(result)
    return json_out

@application.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        print("Request form info: ")
        print(request.form)
        req = request.get_json()
        print("JSON form:")
        print(req)
        result = {
            "username": request.form["username"],
            "status": 200
        }
        return json.dumps(result)
    else:
        return "Sign up page."

@application.route("/ingredients", methods=["POST"])
def ingredientSearch():
    if request.method == "POST":
        print("Ingredient list received:")
        print(request.form.ingredients)
        results = {
            "statusCode":200
        }
        return json.dumps(results)



if __name__ == '__main__':
    application.debug = True
    application.run()
