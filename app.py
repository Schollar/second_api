from flask import Flask, request, Response
import json
import dbhandler as dbh
app = Flask(__name__)
db = dbh.dbInteraction()


@app.get('/item')
def get_items():
    try:
        item_list = db.get_items()
        items_json = json.dumps(item_list, default=str)
    except:
        return Response("Something went wrong getting items from the DB!", mimetype="application/json", status=400)
    if(item_list):
        return Response(items_json, mimetype="application/json", status=200)
    else:
        return Response("Something went wrong getting items from the DB!", mimetype="application/json", status=400)


app.run(debug=True)
