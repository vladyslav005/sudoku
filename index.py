from crypt import methods

from flask import Flask, render_template, request, jsonify

from backtracking import Backtracking
from dfs import DeepFirstSearch
from forward_controll import ForwardControl
from utils import convert_to_2d

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/solve", methods=['POST'])
def calculate():
    print("Form Data:", request.form)
    print("JSON Data:", request.json)


    request_data = request.json
    response = {
        "steps" : 0,
        "time_elapsed" : 0,
        "solvable" : 0,
        "states" : []
    }

    board = convert_to_2d(request_data['values'])
    method = None
    if request_data['method'] == "DFS":
        method = DeepFirstSearch(board)

    elif request_data['method'] == "Backtracking":
        method = Backtracking(board)

    elif request_data['method'] == "Forward control":

        method = ForwardControl(board)
    method.solve()

    response["states"] = method.converted_states
    response["steps"] = method.count_of_steps
    response["time_elapsed"] = method.duration
    response["solvable"] = method.is_solved


    return jsonify(response)