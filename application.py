#app.py

import os
import json
# import mysql.connector

from flask import Flask
application = app = Flask(__name__)

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



@app.route("/")
def hello():

    # get_all_sql = "SELECT * FROM Recipes;"

    # result = query_db(get_all_sql, (), False)

    # json_out = json.dumps(result)

    return "Hello World."





if __name__ == '__main__':
    app.run(host='0.0.0.0')
