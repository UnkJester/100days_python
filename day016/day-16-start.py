import turtle

toby = turtle.Turtle()
my_screen = turtle.Screen()
toby.showturtle()
toby.color('red','chartreuse4')
toby.shape('turtle')
toby.resizemode('user')
toby.turtlesize(5,5,2)
toby.forward(100)

my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column('Type', ['Electric', 'Water', 'Fire'])
# table.align = 'l' # NOTE: align has to come after the columns, otherwise it wont affect it
# table.add_column('Type again', ['Electric', 'Water', 'Fire'])
# print(table)
