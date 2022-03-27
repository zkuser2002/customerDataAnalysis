from flask import Flask


app=Flask(__name__)
@app.route('/')
def home():
	return "this is a test for herkou"


if __name__=='__main__':
	import os
	PORT=os.getenv("PORT",5000)
	app.run("0.0.0.0",PORT)