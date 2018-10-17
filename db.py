import os
import mysql.connector



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



def getRecipeByIngredient(ingredients):
    pass
