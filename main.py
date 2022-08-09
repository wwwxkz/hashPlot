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
    for line in frame:
        print('|' + line + '|')
    print('-' * table_w)

def _bar_graph(table_w, bar_w, columns):
    frame = []
    for i, column in enumerate(columns):
        for line in range(column[0]):
            try:
                frame[line] += ' ' + '#' * bar_w
            except:
                frame.insert(line, ' ' + '#' * bar_w)
    # Reverse frame as array starts from top and frames and graphs from bottom
    return frame[::-1]

#def _pizza_graph()
#def _function()

def _align(table_w, frame, direction):
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

# Set table (display) size as a var for convenience
table_w = 40

# Display anything you want
#frame = [
#    'True?',
#    'Small question',
#    'Trying bigger question',
#    'Is that even a question?'
#]


# Set bar graph columns as tuple matrixes 
columns = [
    (4, 'Russia'),
    (7, 'Ukraine'),
    (4, 'Argentina'),
    (2, 'Japan'),
    (9, 'Canada')
]

# This time no need to align
frame = _bar_graph(table_w, 4, columns)

# Align text to R, L, C
frame = _align(table_w, frame, 'l')

# Pass desired frame and table (display) size
_display(table_w, frame)
