import pandas

RED = 'Cinnamon'
GREY = 'Gray'
BLACK = 'Black'
COLOR = 'Primary Fur Color'

squirrels = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')


def get_count(color):
    return len(squirrels[squirrels[COLOR] == color])


data = {'Fur Color': [GREY, RED, BLACK], 'Count': [get_count(GREY), get_count(RED), get_count(BLACK)]}

pandas.DataFrame(data).to_csv('squirrel_count.csv')
