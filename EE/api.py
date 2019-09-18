from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!. This is Flask Test Part"

if __name__ == "__main__":
    job_id = 1234
    app.run(host= '0.0.0.0')
