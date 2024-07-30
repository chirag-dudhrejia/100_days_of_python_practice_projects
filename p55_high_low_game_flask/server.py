from flask import Flask
import random

app = Flask(__name__)


@app.route("/<int:user_guess>")
def check(user_guess):
    if user_guess == number:
        return ("<h1>You found me!</h1>"
                "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>")
    elif user_guess > number:
        return ("<h1>Too high, try again!</h1>"
                "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>")
    elif user_guess < number:
        return ("<h1>Too low, try again!</h1>"
                "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>")


@app.route("/")
def guess_number():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src=https://media.giphy.com/media/4QaQ4tA0OUwkkrnG9Z/giphy.gif?cid=790b7611327c7gym5ggdhqxga5j8ck658gmzhtdctpb0nech&ep=v1_gifs_search&rid=giphy.gif&ct=g>')


if __name__ == "__main__":
    number = random.randint(0, 9)
    print(number)
    app.run(debug=True)