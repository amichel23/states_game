#TODO 1. Convert the guess to title Case
#TODO 2. Check if the guess is among the 50 states
#TODO 3. Write the correct guesses onto the map
#TODO 4. Use a loop to allow the user to keep guessing
#TODO 5. Record the correct guess in a list
#TODO 6. Keep track of the score

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S.A. States Game')
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)
turtle.penup()

states = pd.read_csv('50_states.csv')
states_list = states.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                    prompt="What's Another State's Name")
    if answer_state == 'Exit':
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    guessed_states.append(answer_state)
    x = answer_state.title()
    if x in states_list:
        guessed_states.append(x)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == x]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(x)

turtle.mainloop()




