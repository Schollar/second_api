from inspect import trace
from flask import Flask, request, Response
import json
import dbhandler as dbh
import traceback
app = Flask(__name__)

# GET endpoint that returns the items in the DB


@app.get('/item')
def get_items():
    item_list = []
    items_json = None
    limit = None
    try:
        limit = request.args.get('limit')
        item_list = dbh.get_items(limit)
        items_json = json.dumps(item_list, default=str)
    except:
        traceback.print_exc()
        return Response("Something went wrong getting items from the DB!", mimetype="application/json", status=400)
    if(item_list):
        return Response(items_json, mimetype="application/json", status=200)
    else:
        return Response("Something went wrong getting items from the DB!", mimetype="application/json", status=400)

# GET endpoint that takes in user input and returns the employee in the DB


@app.get('/employee')
def get_employee():
    employee = None
    employee_id = None
    employee_json = None
    try:
        employee_id = request.args['id']
        employee = dbh.get_employee(employee_id)
        employee_json = json.dumps(employee, default=str)
    except:
        return Response("Something went wrong getting employee from the DB!", mimetype="application/json", status=400)
    if(employee):
        return Response(employee_json, mimetype="application/json", status=200)
    else:
        return Response("Something went wrong getting employee from the DB!", mimetype="application/json", status=400)

# POST endpoint that takes in user input and adds an  item to the DB


@app.post('/item')
def add_item():
    name = None
    description = None
    quantity = None
    new_item = None
    try:
        name = request.json['name']
        description = request.json['description']
        quantity = request.json['quantity']
        new_item = dbh.add_item(name, description, quantity)
    except:
        return Response('Error adding item to DB', mimetype="plain/text", status=401)
    if(new_item):
        return Response("You have succesfully added this item to the DB!", mimetype="plain/text", status=200)
    else:
        return Response('Error adding item to DB', mimetype="plain/text", status=401)

# POST endpoint that takes in user input and adds an employee in the DB


@app.post('/employee')
def add_employee():
    name = None
    hourly_wage = None
    new_employee = None
    try:
        name = request.json['name']
        hourly_wage = request.json['hourly_wage']
        new_employee = dbh.add_employee(name, hourly_wage)
    except:
        return Response('Error adding employee to DB', mimetype="plain/text", status=401)
    if(new_employee):
        return Response("You have succesfully added this employee to the DB!", mimetype="plain/text", status=200)
    else:
        return Response('Error adding employee to DB', mimetype="plain/text", status=401)

# PATCH endpoint that takes in user input and changes an item's quantity in the DB


@app.patch('/item')
def change_item():
    item_id = None
    new_quantity = None
    change_item = None
    try:
        item_id = request.json['id']
        new_quantity = request.json['quantity']
        change_item = dbh.change_item(item_id, new_quantity)
    except:
        return Response('Error adding changing item', mimetype="plain/text", status=401)
    if(change_item):
        return Response("You have succesfully changed this items quantity!", mimetype="plain/text", status=200)
    else:
        return Response('Error adding changing item', mimetype="plain/text", status=401)

# PATCH endpoint that takes in user input and changes employee wage


@app.patch('/employee')
def change_employee():
    employee_id = None
    new_wage = None
    change_employee = None
    try:
        employee_id = request.json['id']
        new_wage = request.json['hourly_wage']
        change_employee = dbh.change_employee(employee_id, new_wage)
    except:
        return Response('Error adding changing employee', mimetype="plain/text", status=401)
    if(change_employee):
        return Response("You have succesfully changed this employee's wage!", mimetype="plain/text", status=200)
    else:
        return Response('Error adding changing employee', mimetype="plain/text", status=401)

# DELETE endpoint that takes in user input and deletes employee from DB


@app.delete('/employee')
def delete_employee():
    employee_id = None
    delete_employee = None
    try:
        employee_id = request.json['id']
        delete_employee = dbh.delete_employee(employee_id)
    except:
        return Response('Error deleting employee', mimetype="plain/text", status=401)
    if(delete_employee):
        return Response("You have succesfully fired this employee!", mimetype="plain/text", status=200)
    else:
        return Response('Error deleting employee', mimetype="plain/text", status=401)

# DELETE endpoint that takes in user input and deletes an item from DB


@app.delete('/item')
def delete_item():
    item_id = None
    delete_item = None
    try:
        item_id = request.json['id']
        delete_item = dbh.delete_item(item_id)
    except:
        return Response('Error deleting item', mimetype="plain/text", status=401)
    if(delete_item):
        return Response("You have succesfully deleted this item!", mimetype="plain/text", status=200)
    else:
        return Response('Error deleting item', mimetype="plain/text", status=401)


app.run(debug=True)
