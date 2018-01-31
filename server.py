from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=["POST", "GET"])
def test():
    """Takes in two numbers as arguments and returns the sum in JSON format"""

    if request.method == "POST":
        json_request = request.get_json()

        x = json_request.get("x")
        y = json_request.get("y")

        response = {"sum": x + y}

    else:
        response = {"message": "The method is not allowed for the requested URL."}

    return jsonify(response)

@app.errorhandler(400)
def handle_invalid_usage(error):
    """If there is a bad request, returns error message in JSON format"""

    response = {"message": "The browser (or proxy) sent a request that this server could not understand."}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')