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
# - improve function logic
# - could _bar and _vertical_bar be the same func?
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

def _vertical_bar_graph(table_w, bar_h, rows):
    frame = []
    # Find the largest label
    l_label = 0
    for row in rows:
        if len(row[1]) > l_label:
            l_label = len(row[1])
    for i, row in enumerate(rows):
        try:
            frame[i] += '#' * row[0]
        except:
            label = row[1] + ' ' * (int(l_label) - int(len(row[1])))
            frame.insert(i, label + ': ' + '#' * row[0])
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

def _function_graph(table_w, scale, function):
    frame = []
    # (0,0) in cartesian plane
    zero = round((scale * 2) / 2)
    # Positive and negative (exmp -> -5 left +5 right)
    # +1 to add 0 position

    # Get function positions (x,y) based on scale
    res_y = []
    for p, _ in enumerate(range((scale * 2) + 1)):
        # Best way but slow
        # Slice string by math operators to get Y afterwards
        #operators = "+-*/"
        #function_slit = ""
        #for i in replace_x:
        #    if i in operators:
        #        function_slit+="@"+i+"@"
        #    else:
        #        function_slit+=i
        #function_slit=function_slit.split("@")
        #print('String broken: ', function_slit) 

        # Faster and Convenient way
        replace_x = str(function.replace('x', str(p)))
        res_y.append(eval(replace_x))
    print('Points: ', res_y)
    # Create y axis
    for y, point in enumerate(range((scale * 2) + 1)):
        frame.append('')      
        # Creates x axis
        for x, pointer in enumerate(range((scale * 2) + 1)):
            if x == zero:
                frame[y] += '|'
            else:
                if y == zero:
                    frame[y] += '-'
                else:
                    frame[y] += ' '
        # Does the function pass thought this point?
        # Else, default values |, -, ' '
        # Replacing vars by scale of the cartesian plane 
        # Using y for the sake of practicality
        # as both y and x are the same there is no problem
        for i in res_y:
            if y == i:
                frame[y] = frame[y][:i] + '@' + frame[y][i:] 
    return frame

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

# EXAMPLE VERTICAL BAR GRAPH
def _exmp_vertical_bar():
    table_w = 40
    rows = [
        (4, 'Russia'),
        (7, 'Ukraine'),
        (4, 'Argentina'),
        (2, 'Japan'),
        (9, 'Canada')
    ]
    frame = _vertical_bar_graph(table_w, 2, rows)
    frame = _align(table_w, frame, 'l')
    _display(table_w, frame)

def _exmp_function():
    table_w = 40
    function = 'x+1'
    # 5 to left, right, top, bottom from 0
    cartesian_plane = 5
    frame = _function_graph(table_w, cartesian_plane, function)
    frame = _align(table_w, frame, 'c')
    _display(table_w, frame)

_exmp_text()
_exmp_bar()
_exmp_pizza()
_exmp_vertical_bar()
_exmp_function()
