
def fetchIngredients(ingredients):
    query = f"""SELECT * FROM Ingredient WHERE ingredient_name in ('{"','".join(ingredients)}');"""
    return query

def fetchRecipes(ids):
    str_ids = [str(i) for i in ids]
    query = f"""SELECT DISTINCT r.recipe_id, r.title 
                FROM 
                Recipes r
                INNER JOIN Qty_Ingredients i
                ON i.recipe_id = r.recipe_id
            WHERE i.ingredient_id IN ({",".join(str_ids)});
            """
    return query