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

# TODO
# - improve bar graph legend logic
# - improve pizza graph logic
# - add function_graph
# - func names
# - interactive shell
# - multiple screens
# - change func in the interactive shell

def _display(table_w, frame):
    print('-' * table_w)
    for line in frame:
        print('|' + line + '|')
    print('-' * table_w)

def _bar_graph(table_w, bar_w, columns):
    frame = []
    for column in columns:
        for line in range(column[0]):
            try:
                frame[line] += ' ' + '#' * bar_w
            except:
                frame.insert(line, ' ' + '#' * bar_w)
    for c, column in enumerate(columns):
        try:
            if c == 0:
                frame[:0] = ' ' 
                frame[0] = ' ' + column[1]
            else:
                frame[0] += ' ' + column[1]
        except:
            frame.insert(0, ' ' + column[1])
    # Reverse frame as array starts from top and frames and graphs from bottom
    return frame[::-1]

def _pizza_graph(table_w, table_h, slices):
    frame = []
    reverse = False
    for slice in slices:
        # Create circle
        for c, line in enumerate(range(table_h)):
            if c == table_h/2:
                reverse = True
            if reverse == True:
                c = table_h - c
            try:
                frame[line] += '@'
            except:
                frame.insert(line, '@' * (2 * c))
    return frame

def _function_graph():
    pass

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

# EXAMPLE DISPLAY TEXT
def _exmp_text():
    # Set table (display) size as a var for convenience
    table_w = 40
    # Display anything you want
    frame = [
        'True?',
        'Small question',
        'Trying bigger question',
        'Is that even a question?'
    ]
    # Align text to R, L, C
    frame = _align(table_w, frame, 'r')
    # Pass desired frame and table (display) size
    _display(table_w, frame)

# EXAMPLE BAR GRAPH
def _exmp_bar():
    # Set bar graph columns as tuple matrixes 
    table_w = 40
    columns = [
        (4, 'Russia'),
        (7, 'Ukraine'),
        (4, 'Argentina'),
        (2, 'Japan'),
        (9, 'Canada')
    ]
    frame = _bar_graph(table_w, 4, columns)
    frame = _align(table_w, frame, 'l')
    _display(table_w, frame)

# EXAMPLE PIZZA GRAPH
def _exmp_pizza():
    table_w = 40
    table_h = 10
    slices = [
        (20, 'New Zeland'),
        (50, 'Australia'),
        (10, 'China'),
        (80, 'Mongolia'),
        (60, 'Germany'),
        (50, 'Poland')
    ]
    frame = _pizza_graph(table_w, table_h, slices)
    frame = _align(table_w, frame, 'c')
    _display(table_w, frame)

_exmp_text()
_exmp_bar()
_exmp_pizza()
