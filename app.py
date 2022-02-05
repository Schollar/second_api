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


@app.get('/employee')
def get_employee():
    try:
        employee_id = request.args['id']
        employee = db.get_employee(employee_id)
        employee_json = json.dumps(employee, default=str)
    except:
        return Response("Something went wrong getting employee from the DB!", mimetype="application/json", status=400)
    if(employee):
        return Response(employee_json, mimetype="application/json", status=200)
    else:
        return Response("Something went wrong getting employee from the DB!", mimetype="application/json", status=400)


@app.post('/item')
def add_item():
    try:
        name = request.json['name']
        description = request.json['description']
        quantity = request.json['quantity']
        new_item = db.add_item(name, description, quantity)
    except:
        return Response('Error adding item to DB', mimetype="plain/text", status=401)
    if(new_item):
        return Response("You have succesfully added this item to the DB!", mimetype="plain/text", status=200)
    else:
        return Response('Error adding item to DB', mimetype="plain/text", status=401)


@app.post('/employee')
def add_employee():
    try:
        name = request.json['name']
        hourly_wage = request.json['hourly_wage']
        new_employee = db.add_employee(name, hourly_wage)
    except:
        return Response('Error adding employee to DB', mimetype="plain/text", status=401)
    if(new_employee):
        return Response("You have succesfully added this employee to the DB!", mimetype="plain/text", status=200)
    else:
        return Response('Error adding employee to DB', mimetype="plain/text", status=401)


@app.patch('/item')
def change_item():
    try:
        item_id = request.json['id']
        new_quantity = request.json['quantity']
        change_item = db.change_item(item_id, new_quantity)
    except:
        return Response('Error adding changing item', mimetype="plain/text", status=401)
    if(change_item):
        return Response("You have succesfully changed this items quantity!", mimetype="plain/text", status=200)
    else:
        return Response('Error adding changing item', mimetype="plain/text", status=401)


app.run(debug=True)
