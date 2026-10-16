
from flask import Flask, jsonify, render_template

@app.route("/")
def home():
    return render_template("index.html")

app = Flask(__name__)

@app.route("/api/square/<int:number>")
def square(number):
    return jsonify({"result": number ** 2})

if __name__ == "__main__":
    calculator()