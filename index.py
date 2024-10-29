from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/solve", methods=['POST'])
def calculate():
    print("Form Data:", request.form)
    print("JSON Data:", request.json)


    return jsonify({"status": "ok"})