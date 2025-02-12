import turtle
import pandas

#Setting up the screen and importing the states map
screen = turtle.Screen()
screen.title("U.S.A. States")
screen.addshape("us_map.gif")
turtle.shape("us_map.gif")

#Setting up a Turtle to write on the screen
turtle_write = turtle.Turtle()
turtle_write.hideturtle()
turtle_write.penup()

#Reading the states_file.csv with pandas and creating a list with state names
data = pandas.read_csv("states_file.csv")
states_list = data.state.to_list()

#Setting up the game variables
score = 0
guessed_states = []

while score < 50:
    #User answer will be title cased
    user_answer = screen.textinput(title=f"{score}/50 States guessed", prompt="What is the state's name?").title()

    #If the user answer is in the states list and not in guessed states list, then it will be writen on the screen
    if user_answer in states_list and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        state_data = data[data.state == user_answer]
        turtle_write.goto(x=state_data.x.item(), y=state_data.y.item())
        turtle_write.write(arg=state_data.state.item(), align="center", font=("Courier", 9, "bold"))
        score += 1