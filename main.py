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


def _display(table_w, frame):
    print('-' * table_w)
    for i, line in enumerate(frame): 
        spaces = int(table_w - len(line)) - 5
        print('|', 
                ' ' * spaces , 
                line, 
              '|')
    print('-' * table_w)

# Frame
frame = [
    'True?',
    'Small question',
    'Trying bigger question',
    'Is that even a question?'
]

_display(40, frame)



