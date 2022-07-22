from flask import Flask, jsonify, request
from statistics import mean, median, mode


app = Flask(__name__)

@app.route("/calculate", methods=['POST'])

def calculate():
    data = request.get_json()

    function = data['operation'].lower()
    list_vals = data['operands']

    if function == 'sum':
        return jsonify({"answer":sum(list_vals)})

    elif ((function == 'average') | (function == 'avg') | (function == 'mean')):
        return jsonify({"answer":mean(list_vals)})

    elif (function == 'median'):
        return jsonify({"answer":median(list_vals)})

    elif (function == 'mode'):
        return jsonify({"answer":mode(list_vals)})
    
    else:
        return "Operation not available"

  

if __name__ == "__main__":
    app.run(debug=True)
