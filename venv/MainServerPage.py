from flask import render_template, Response
from flask import Flask, request, jsonify
import os
import json
import db_connection as dbcon
import Models

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
# This part create an instances of our web application and set path of our SQLite uri.

# Route the user to the homepage
@app.route('/', methods = ['GET'])
def home():
    return "Hi"

# endpoint to create new employee
@app.route("/CreateEmployee", methods=["POST"])
def add_user():
    # print(request.json)
    username = request.form.get("username")
    gender = request.form.get("gender")
    emailid = request.form.get("email")
    con = dbcon.getConnection() #create connection instance

    new_employee = Models.Employee(username,gender, emailid)

    try:
        query = 'insert into tblEmployee(name, gender, email) values (?,?,?)'

        cursor = con.cursor()
        cursor.execute(query, [new_employee.name, new_employee.gender, new_employee.emailid])
        con.commit()
        # print("Data saved successfully")
        execMsg="Data saved successfully"
    except Exception as exp:
        execMsg=exp
    finally:
        con.close()

    return str(execMsg)
    # return json.dumps(new_employee.__dict__)

# endpoint to show all users
@app.route("/AllEmployees", methods=["GET"])
def get_employee():
    con = dbcon.getConnection() #create connection instance
    try:
        query = "select * from tblEmployee"
        cursor = con.cursor()
        cursor.execute(query)
        execMsg = cursor.fetchall()
        # for row in cursor:
        #     execMsg+=row

    except Exception as exp:
        execMsg=exp
    return str(execMsg)


# endpoint to get user detail by id
@app.route("/Employee/<id>", methods=["GET"])
def user_detail(id):
    con = dbcon.getConnection()  # create connection instance
    try:
        query = "select * from tblEmployee where id = (?)"
        cursor = con.cursor()
        cursor.execute(query,[id])
        execMsg = cursor.fetchall()
        # for row in cursor:
        #     execMsg+=row

    except Exception as exp:
        execMsg = exp
    return str(execMsg)


# endpoint to update user
@app.route("/EmployeeUpdate/<id>", methods=["PUT"])
def employee_update(id):
    con = dbcon.getConnection()  # create connection instance
    name = request.json["name"]
    gender = request.json["gender"]
    emailid = request.json["emailid"]
    try:
        query = "select * from tblEmployee where id = (?)"
        cursor = con.cursor()
        cursor.execute(query, [id])
        count = len(cursor.fetchall())
        if (count>0):
            query = "update tblemployee set name =?,gender=?,emailid=? where id= ?"
            cursor = con.cursor()
            cursor.execute(query,[name, gender, emailid, id])
            con.commit()
            execMsg="Data Updated Successfully!!!"
        else:
            execMsg= "No employees found for provided employee id"
    except Exception as exp:
        execMsg=exp
    finally:
        con.close()
    return str(execMsg)

# endpoint to delete user
@app.route("/EmployeeDelete/<id>", methods=["DELETE"])
def user_delete(id):
    con = dbcon.getConnection()  # create connection instance
    try:
        query = "select * from tblEmployee where id = (?)"
        cursor = con.cursor()
        cursor.execute(query,[id])
        count=len(cursor.fetchall())

        if(count>0):
            query = "delete from tblEmployee where id = (?)"
            cursor = con.cursor()
            cursor.execute(query,[id])
            execMsg = 'Employee record got deleted!!!'
            con.commit()
        else:
            execMsg = "No employees found for provided employee id"

    except Exception as exp:
        execMsg = exp
    return str(execMsg)

if __name__ == '__main__':
    app.run(debug=True)

