#app.py

import os
import json

from db import query_db, getRecipeByIngredient, getRecipeByID

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
    print("Fetching all.")

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
        ingredients = json.loads(request.form["ingredients"])
        
        print(ingredients)

        liked = [fruit for fruit, val in ingredients.items() if (val == 1)]
        restricted = [fruit for fruit, val in ingredients.items() if val == -1]
        wanted_recipes = getRecipeByIngredient(liked)
        restricted_recipes = getRecipeByIngredient(restricted)
        for recipe in restricted_recipes:
            if recipe in wanted_recipes:
                wanted_recipes.remove(recipe)

        # print(ingredients)
        results = {
            "statusCode":200,
            "recipes": wanted_recipes
        }
        return json.dumps(results)

@application.route("/recipe/<int:recipe_id>")
def recpieById(recipe_id):
    if request.method == "GET":
        recipe = getRecipeByID(recipe_id)
        result = {
            "statusCode": 200,
            "recipe": recipe
        }
        return json.dumps(result)




if __name__ == '__main__':
    application.debug = True
    application.run()
