
def fetchIngredients(ingredients):
    fixed = [i.lower() for i in ingredients]
    print(fixed)
    query = f"""SELECT * FROM Ingredient WHERE ingredient_name in ('{"','".join(fixed)}');"""
    return query

def fetchRecipes(wanted):
    wanted_str = [str(i).lower() for i in wanted]
    query = f"""SELECT DISTINCT r.recipe_id, r.title 
                FROM 
                Recipes r
                INNER JOIN Qty_Ingredients i
                ON i.recipe_id = r.recipe_id
            WHERE i.ingredient_id IN ({",".join(wanted_str)});
            """
    return query