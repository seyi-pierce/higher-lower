from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home_route_display():
    return "<b><h1>Guess a number between 0 and 9</h1></b><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC" \
           "/giphy.gif'>"


number = random.randint(0, 9)
@app.route("/<int:num>")
def check_num(num):
    global number
    if num == number:
        return "<h1 style='color: green'>You found me.</h1><p><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></p>"
    elif num < number:
        return "<h1 style='color: purple'>Too low! Try again</h1><p><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></p>"
    elif num >number:
        return "<h1 style='color: red'>Too high! Try again.<h1><p><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></p>"


if __name__ == "__main__":
    app.run(debug=True)
