# Hash Plot
# by wwwxkz
# github.com/wwwxkz 
# gitlab.com/wwwxkz
# linkedin.com/wwwxkz

# Programming with no goal, thought about making an program to
# state questions (situations) and options to adress those like
# like an notepad, but "funnier" 

# It was a cool, but as I began I tought that making a geogebra
# in the console would be even better

# In python just because it is easy, and I was playing around with
# the interactive shell 


def _display(frame, table_w):
    print('-' * table_w)
    for line in frame:
        print('|' + line + '|')
    print('-' * table_w)

#def _bar_graph()
#def _pizza_graph()
#def _function()

def _align(frame, table_w, direction):
    for i, line in enumerate(frame):
        spaces = int(table_w - len(line)) - 2
        if direction == 'r':
            frame[i] = ' ' * spaces + line
        elif direction == 'l':
            frame[i] = line + ' ' * spaces
        elif direction ==  'c':
            frame[i] = ' ' * int(spaces/2) + line + ' ' * int(spaces/2)
        else:
            print('Invalid direction')
    return frame

# Frame
frame = [
    'True?',
    'Small question',
    'Trying bigger question',
    'Is that even a question?'
]

frame = _align(frame, 40, 'c')
_display(frame, 40)



