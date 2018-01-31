from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/test', methods=["POST"])
def test():
    """Takes in two numbers as arguments and returns the sum in JSON format"""

    json_request = request.get_json()

    x = json_request.get("x")
    y = json_request.get("y")

    sum_nums = {"sum": x + y}

    return jsonify(sum_nums)

if __name__ == "__main__":
    app.run(debug=True)