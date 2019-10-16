"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""
    #
    return """
    <!doctype html>
      <html>
        Hi! This is the home page.<br>
      <a href="http://localhost:5000/hello">Hello page</a> 

      </html>
    """


@app.route("/options")
def options():
    """Choose compliment or insult"""

    return """
      <!doctype html>
        <html>
          <head>
            <title>Hey!</title>
          </head>

          <body>
            <h1>Hi There!</h1>
            <h3> Do you want a <a href="http://localhost:5000/compliment">compliment</a> or <a href="http://localhost:5000/diss">diss</a> ?</h3>
             
          </body>
      </html>
      """

@app.route("/compliment")
def compliment():
  """choose a compliment"""
  return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <select name="compliment">
            <option value="Nice">Nice</option>
            <option value="Good">Good</option>
          </select>
          <input type="submit" value="Submit">
        </form>

      
      </body>
    </html>
    """
@app.route("/diss")
def diss():
  """choose a compliment"""
  return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      
      <body>
      <form action="/greet">
          <h1>Hi There!</h1>
          What's your name? <input type="text" name="person">
          <select name="compliment">
            <option value="Bad">Bad</option>
            <option value="Mean">Mean</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """
@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
        <h3> Want a compliment?</h3><br>
          What's your name? <input type="text" name="person">
          <select name="compliment">
            <option value="Nice">Nice</option>
            <option value="Good">Good</option>
          </select>
          <input type="submit" value="Submit">
        </form>

        <form action="/diss">
        <h3> Want a diss?</h3><br>
          What's your name? <input type="text" name="person">
          <select name="diss">
            <option value="Bad">Bad</option>
            <option value="Mean">Mean</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    #y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route("/diss")
def diss_person():
    """Get user by name and diss them"""
    player = request.args.get("person")
    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)

if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
