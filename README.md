
# Flask "Hello, World!" Demo App

## Overview

This demo app demonstrates basic HTTP operations using Flask. You’ll be able to interact with it via the browser or using `curl` commands from the terminal.

### Key Features:
- A basic route that returns "Hello, World!"
- A route that greets the user based on a query parameter (`name`)
- A route that echoes a message sent in a JSON body using a POST request.

### Learning Objectives
- Set up and run a Flask application
- Understand how API endpoints work in practice
- Experience different methods of interacting with endpoints (browser, curl)

### Prior Knowledge:
- Command line usage (Git, Python, curl)
- Basic knowledge of HTTP requests and REST APIs

### Time Estimate: 10 minutes


## Prerequisites

Before running the app, you need to have the following installed:

- **Python 3** (3.6 or later)
- **Flask**: A Python web framework.

To install Flask, run:

```bash
pip install flask
```

## Running the Demo App

### 1. Clone this repo

### 2. Start the Flask Application

Open a terminal and navigate to the folder where `app.py` is located. Then, run the following command to start the Flask server:

```bash
python app.py
```

You should see output like this:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

This indicates that the app is running locally at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## Accessing the App in Your Browser

Once the Flask app is running, you can access the routes in your web browser by navigating to the following URLs:

1. **Hello World Route**:  
   Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  
   You should see the message: `Hello, World!`

2. **Greet Route** (with query parameter):  
   Visit: [http://127.0.0.1:5000/greet?name=Alice](http://127.0.0.1:5000/greet?name=Alice)  
   You should see a greeting message: `Hello, Alice!`

   Without a query parameter (defaults to "Guest"):  
   Visit: [http://127.0.0.1:5000/greet](http://127.0.0.1:5000/greet)  
   You should see: `Hello, Guest!`

3. **Echo Route** (POST request with JSON body):  
   You can test this using `curl` (explained below).  


## Testing the App with `curl`

You can test the app's routes using the `curl` command in your terminal. Below are the commands to test each route.

### **1. Test the Basic Route (GET)**
```bash
curl -X GET http://127.0.0.1:5000/
```
- Expected response: `"Hello, World!"`

### **2. Test the Route with Query Parameters (GET)**
#### Without Query Parameter (defaults to "Guest"):
```bash
curl -X GET http://127.0.0.1:5000/greet
```
- Expected response: `{"message": "Hello, Guest!"}`

#### With Query Parameter (`name=Alice`):
```bash
curl -X GET "http://127.0.0.1:5000/greet?name=Alice"
```
- Expected response: `{"message": "Hello, Alice!"}`

### **3. Test the Route with a JSON Body (POST)**
#### Success Case:
```bash
curl -X POST http://127.0.0.1:5000/echo -H "Content-Type: application/json" -d '{"message": "This is a test"}'
```
- Expected response: `{"echo": "You said: This is a test"}`

#### Error Case (missing `message` field):
```bash
curl -X POST http://127.0.0.1:5000/echo -H "Content-Type: application/json" -d '{}'
```
- Expected response: `{"error": "Missing 'message' in request body"}`


## Completion Proof

Try the query parameter endpoint with your name, whether in the browser or through curl. Take a screenshot and upload to the specified in-class activity on brightspace.
