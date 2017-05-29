# ------Flask Hello World ----- #
# import the Flask class from the flask package
from flask import Flask

#create the application project

app = Flask(__name__)

#use the decorator pattern to link the view function to a url
@app.route("/")
@app.route("/route")

# dfine the view using a function, which retursn a string

def hello_world():
	return "Hell, World!"

#start the dvelopment server using the run() method
if __name__ =="__main__":
	app.run()

