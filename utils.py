
def fetchIngredients(ingredients):
    query = f"""SELECT * FROM Ingredient WHERE ingredient_name in ('{"','".join(ingredients)}');"""
    return query

def fetchRecipes(wanted):
    wanted_str = [str(i) for i in wanted]
    query = f"""SELECT DISTINCT r.recipe_id, r.title 
                FROM 
                Recipes r
                INNER JOIN Qty_Ingredients i
                ON i.recipe_id = r.recipe_id
            WHERE i.ingredient_id IN ({",".join(wanted_str)});
            """
    return query