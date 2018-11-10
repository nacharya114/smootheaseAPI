import os
import mysql.connector

from utils import *

# Connect to the database
mydb = mysql.connector.connect(host=os.environ["AWS_HOST"],
                            user=os.environ["AWS_USERNAME"],
                            password=os.environ["AWS_PASSWORD"],
                            db="smoothiesdb",
                            )

###HELPER FUNCTIONS
def query_db(query, args=(), one=False):
    cur = mydb.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    return (r[0] if r else None) if one else r



def getRecipeByIngredient(wanted):
    ing_id_query = fetchIngredients(wanted)
    results = query_db(ing_id_query)
    wanted_ids = [i["ingredient_id"] for i in results]


    recipe_fetch_sql = fetchRecipes(wanted_ids)
    results = query_db(recipe_fetch_sql)

    return results

    # return ing_ids

def getRecipeByID(id):
    query_sql = f"SELECT * FROM Recipes WHERE recipe_id={id}"

    return query_db(query_sql,one=True)