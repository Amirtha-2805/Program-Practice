from flask import Flask,render_template,request
app=Flask(__name__)
student_details=[{"id":1,"name":"Amirtha","place":"Nagercoil","email":"amirthanatarajan14@gmail.com","phone_no":6385811613,"password":"1234nm"},
                 {"id":2,"name":"Aiswarya","place":"Meenakshipuram","email":"aishuvenkat14@gmail.com","phone_no":9385811793,"password":"7855sd"},
                 {"id":3,"name":"Jayasree","place":"Trivandrum","email":"jayasreenatarajan14@gmail.com","phone_no":8220072429,"password":"849@ba"}]

@app.route("/home",methods=["GET"])
def datas():
    return render_template ("home.html",student_details=student_details)


@app.route("/details/<int:student_id>",methods=["GET","POST"])
def address(student_id):
    for i in student_details:
        if i["id"]==student_id:
            return i
    return "There is no student with the id which you entered" 

@app.route("/delete/<int:student_id>",methods=["GET","POST"])
def del_detail(student_id):
    student_details.remove(student_details[student_id])

    return render_template ("home.html",student_details=student_details)
    # return "There is no data to be deleted" 


@app.route("/new_detail",methods=["GET","POST"])
def add_new():
    if request.method=="POST":
        new_value={"id":len(student_details)+1,
               "name":request.form("s_name"),
               "place":request.form("location"),
               "email":request.form("mail_id"),
               "phone_no":request.form("contact_no")}
        student_details.append(new_value)
        return student_details
    else:
        return render_template("sample.html")
    
@app.route("/update/<int:updatedvalue>",methods=["GET","POST","PUT"])
def update_data(updatedvalue):
    if request.method=="POST":
        
        update_value={"id":int(request.form["s_id"]),
                            "name":request.form["s_name"],
                            "place":request.form["location"],
                            "email":request.form["mail_id"],
                            "phone_no":request.form["contact_no"]}
        student_details[updatedvalue]=update_value
        return render_template("home.html", student_details=student_details)
    else:
        value=student_details[updatedvalue]
        return render_template("update.html",values=value)

@app.route("/", methods=["GET","POST"])
def password():
    if request.method=="POST":
         for j in student_details:
             if (j["password"]==request.form["security_pin"]) and (j["email"]==request.form["mail_id"]):
                return render_template("home.html",student_details=student_details)
             else:
                 return "Incorrect password"
    else:
        return render_template("test.html") 
    
@app.route("/",methods=["GET","POST"])
def out():
    if request.method=="GET":
        return render_template("home.html")            
   
    

if __name__=="__main__":
    app.run(debug=True)
