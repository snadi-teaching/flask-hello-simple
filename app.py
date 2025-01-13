from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)


# Simple route for "Hello, World!"
@app.route("/")
def hello_world():
    return "Hello, World!\n"


# Route that demonstrates a GET request with a query parameter
@app.route("/greet", methods=["GET"])
def greet_user():
    # Get the 'name' query parameter (default to 'Guest' if not provided)
    name = request.args.get("name", "Guest")
    return jsonify(message=f"Hello, {name}!")


# Route that demonstrates a POST request with a JSON body
# Note that this doesn't actually save any data and is just for demo
# purposes to show how to accept and handle JSON data in a request
@app.route("/echo", methods=["POST"])
def echo_message():
    # Parse the JSON body of the request
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify(error="Missing 'message' in request body"), 400

    message = data["message"]
    return jsonify(echo=f"You said: {message}")


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
