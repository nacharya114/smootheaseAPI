#app.py

import os
import json

from db import query_db, getRecipeByIngredient, getRecipeByID,getIngredientsByRecipe

from auth import *

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
        print(req)
        idToken = request.form["id"]
        # realID = getIDfromGoogle(idToken)
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
        #HARDCODING JSON DATA FIX
        data = request.form["ingredients"]
        weightGoals = None
        dietary = None
        if "weightGoals" in request.form.keys():
            weightGoals = request.form["weightGoals"]
        if "dietaryRestrictions" in request.form.keys():
            dietary = request.form["dietaryRestrictions"]
        data = "{" + data[1:-1] + "}"

        ingredients = json.loads(data)
        
        print(ingredients)

        liked = [fruit for fruit, val in ingredients.items() if (val == 1)]
        restricted = [fruit for fruit, val in ingredients.items() if val == -1]
        wanted_recipes = []
        if len(liked):
            wanted_recipes =  getRecipeByIngredient(liked)
        restricted_recipes = []
        if len(restricted):
            restricted_recipes = getRecipeByIngredient(restricted)
        for recipe in restricted_recipes:
            if recipe in wanted_recipes:
                wanted_recipes.remove(recipe)


        # print(ingredients)
        results = {
            "statusCode":200,
            "recipes": wanted_recipes,
            "num_recipes": len(wanted_recipes)
        }
        return json.dumps(results)

@application.route("/recipe/<int:recipe_id>")
def recipeById(recipe_id):
    if request.method == "GET":
        recipe = getRecipeByID(recipe_id)
        result = {
            "statusCode": 200,
            "recipe": recipe
        }
        return json.dumps(result)

@application.route("/cost", methods=["POST"])
def getSpreadsheet():
    if request.method == "POST":
        ids = request.form["recipes"]
        l_ids = json.loads(ids)
        cost_dict = {}
        total = 0.0
        for i in l_ids:
            ing_costs = getIngredientsByRecipe(i)
            for ing in ing_costs:
                if ing["ingredient_name"] not in cost_dict.keys():
                    cost_dict[ing["ingredient_name"]] = 0.0
                cost_dict[ing["ingredient_name"]] += ing['quantity'] * ing['cost']
                total += ing['quantity'] * ing['cost']

        print(cost_dict)
            # return cost_dict
        result = {
            "statusCode": 200,
            "cost": cost_dict,
            "total": total
        }
        return json.dumps(result)


if __name__ == '__main__':
    application.debug = True
    application.run()
