import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
turtle.tracer(0)

data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
state_list = data['state'].to_list()
xcor_list = data['x'].to_list()
ycor_list = data['y'].to_list()

game_on = True

guess_list = []

while game_on:

    answer_state = screen.textinput(title=f"Correct {len(guess_list)}/50", prompt="What's another state's name?")
    answer_state_cap = answer_state.title()

    if answer_state_cap == "Exit":
        break

    if answer_state_cap in state_list:
        state_index = state_list.index(answer_state_cap)
        state_xcor = xcor_list[state_index]
        state_ycor = ycor_list[state_index]

        if answer_state_cap not in guess_list:

            guess_list.append(answer_state_cap)
            turtle.goto(x=state_xcor, y=state_ycor)
            turtle.write(answer_state_cap)
            turtle.home()
            turtle.update()

    if len(guess_list) == 50:
        game_on = False



for state in guess_list:
    if state in state_list:
        state_list.remove(state)

df = pandas.DataFrame(state_list, columns=["States to Learn"])
df.to_csv("states_to_learn.csv")