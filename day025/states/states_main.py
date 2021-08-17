import turtle
import pandas

IMAGE = 'blank_states_img.gif'
CSV_INPUT = '50_states.csv'

s = turtle.Screen()
s.title('U.S. States Game')
s.addshape(IMAGE)
turtle.shape(IMAGE)
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed('fastest')

## Discover where the mouse is clicking
# def get_mouse_click_coord(x, y):
#     print(x, y)
# s.onscreenclick(get_mouse_click_coord)
states_csv = pandas.read_csv(CSV_INPUT)

answer_list = []
while len(answer_list) < 50:
    s.update()
    answer_state = s.textinput(title=f"{len(answer_list)}/50 states guessed", prompt='Please guess another state').title()
    if answer_state == 'Exit':
        missing = []
        for state in states_csv['state'].to_list():
            if state not in answer_list:
                missing.append(state)
        output = pandas.DataFrame(missing)
        output.columns = ['state']
        output.to_csv('./missed_states.py')
        break
    if answer_state in states_csv['state'].to_list() and answer_state not in answer_list:
        next_loc = states_csv[states_csv['state'] == answer_state]
        t.goto(int(next_loc.x), int(next_loc.y))
        t.write(arg=answer_state, align='center', font=("Arial", 8, "normal"))
        answer_list.append(answer_state)
s.exitonclick()
