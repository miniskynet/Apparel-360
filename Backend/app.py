import email
import flask
import requests
from flask import Flask,request,jsonify,render_template
from flask_cors import CORS,cross_origin
import pymongo

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True
myclient = pymongo.MongoClient("mongodb+srv://admin:MCf5wrQMjCfpbTNN@cluster0.6ndwb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
print(myclient.list_database_names())

mydb = myclient["Apparel_360"]

@app.route('/SignUp', methods = ['POST'])
@cross_origin()
def SignUp():
    if request.method == 'POST':

        request_json = request.get_json()
        username = request_json.get('username')
        password = request_json.get('password')
        fname = request_json.get('fname')
        lname = request_json.get('lname')
        comname = request_json.get('comname')
        comdetail = request_json.get('comdetail')
        email = request_json.get('email')

        mycol = mydb["user_records"]

        mydict = {"User_Name": username,
                "Password": password,
                "First_Name": fname,
                "Last_Name": lname,
                "Company": comname,
                "Company_Detail":comdetail,
                "Email":email
                }

        x = mycol.insert_one(mydict)

        print(x.inserted_id)

        reponse_content = {}
        response_content = {
            "message" : "Connection Successful. User Data added to Database."
        }

        return jsonify(response_content)

@app.route('/LogIn', methods = ['POST'])
@cross_origin()
def LogIn():
    myclient = pymongo.MongoClient("mongodb+srv://admin:MCf5wrQMjCfpbTNN@cluster0.6ndwb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    mydb = myclient["Apparel_360"]
    if request.method == 'POST':

        request_json = request.get_json()
        username = request_json.get('username')
        password = request_json.get('password')



    mycol = mydb["user_records"]
    
    mydict = {"User_Name": username,
              "Password": password}

    x = mycol.find_one(mydict)
    print(x)
    reponse_content = {}
    response_content = {
            "message" : "User Login Approved"
        }

    return jsonify(response_content)
app.run()