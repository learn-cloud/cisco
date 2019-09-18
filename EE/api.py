from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
     return '''
	    <!Doctype html>
		<html>
		<head>
			<h1> Home Page </h1>
		</head>
		<body> 
		<h2> this is the Home page body section </h2>
		</body>
		</html>
	     '''

@app.route('/about')
def about():
    return "<h1> About Page </h1>"
if __name__ == '__main__':
	app.run(debug=True)
