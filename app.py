from flask import Flask,jsonify,request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/status",methods=['GET'])
def statuscheck():
    return "Status is working"


if __name__=="__main__":
    app.run(port=5000,debug=True)