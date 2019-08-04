import db_connection as dbcon
import Models



name = 'mickey'
gender = 'male'
emailid = 'm@gmail.com'
con = dbcon.getConnection() #create connection instance
# new_employee = Models.Employee(username,gender, emailid)

# try:
#     query = 'insert into tblEmployee(name, gender, email) values (?,?,?)'
#     cursor = con.cursor()
#     cursor.execute(query, [new_employee.name, new_employee.gender, new_employee.emailid])
#     con.commit()
#     print("Data saved successfully")
#
# except Exception as exp:
#         print(exp)
# finally:
#         con.close()

    # name = request.json["name"]
    # gender = request.json["gender"]
    # emailid = request.json["emailid"]
id=24
try:
        query = "update tblemployee set name =?,gender=?,email=? where id= ?"
        cursor = con.cursor()
        cursor.execute(query,[name, gender, emailid, id])
        con.commit()
        execMsg="Data Updated Successfully!!!"
except Exception as exp:
        execMsg=exp
finally:
        con.close()

print (execMsg)