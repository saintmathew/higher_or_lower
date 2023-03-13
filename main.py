from flask import Flask
import random

rand_num = random.randint(1, 9)
print(rand_num)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h2>Welcome to the Higher or Lower Game</h2>"


@app.route("/<int:choice>")
def outcome(choice):
    if choice > rand_num:
        return "<h2>Too high try to go lower</h2>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif choice < rand_num:
        return "<h2>Quite low, try to go higher</h2>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif choice == rand_num:
        return "<h2>You garrit baby!!!!" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
