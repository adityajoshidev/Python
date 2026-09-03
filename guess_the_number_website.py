import random

from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExazJ1aDhkMDhtN3BkbnMwMmd5MWg5djlqMWV3OXB6YjBjNnlza3BqZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1ojn1S7BTXUry8elNi/giphy.gif">')

random_number=random.randint(0,9)

@app.route('/<int:user_choice_number>')
def user_choice(user_choice_number):
    if user_choice_number<random_number:
        return ('<h1 style="color:red;">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    elif user_choice_number>random_number:
        return ('<h1 style="color:purple;">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    else:
        return ('<h1 style="color:green;">You found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')



if __name__=='__main__':
    app.run(debug=True)
