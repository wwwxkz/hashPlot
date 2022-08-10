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
# - add bar height to vertical bar
# - improve function logic
# - improve bar label logic
# - improve pizza logic

class Plotter:
    def display(self, table_width, frame):
        print('-' * table_width)
        for line in frame:
            print('|' + line + '|')
        print('-' * table_width)

    def align(self, table_width, frame, direction):
        for i, line in enumerate(frame):
            spaces = int(table_width - len(line)) - 2
            if direction == 'r':
                frame[i] = ' ' * spaces + line
            elif direction == 'l':
                frame[i] = line + ' ' * spaces
            elif direction == 'c':
                frame[i] = ' ' * int(spaces/2) + line + ' ' * int(spaces/2)
            else:
                print('Invalid direction')
        return frame

    def horizontal_bar(self, bar_w, columns):
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

    def vertical_bar(self, rows):
        frame = []
        # Find the largest label
        largest_label = 0
        for row in rows:
            if len(row[1]) > largest_label:
                largest_label = len(row[1])
        for i, row in enumerate(rows):
            try:
                frame[i] += '#' * row[0]
            except:
                label = row[1] + ' ' * (int(largest_label) - int(len(row[1])))
                frame.insert(i, label + ': ' + '#' * row[0])
        return frame[::-1]

    def pizza(self, table_height, slices):
        frame = []
        reverse = False
        for slice in slices:
            # Create circle
            for c, line in enumerate(range(table_height)):
                if c == table_height/2:
                    reverse = True
                if reverse == True:
                    c = table_height - c
                try:
                    frame[line] += '@'
                except:
                    frame.insert(line, '@' * (2 * c))
        return frame

    def function(self, scale, function):
        frame = []
        # (0,0) in cartesian plane
        zero = round((scale * 2) / 2)
        # Get function positions (x,y) based on scale
        res_y = []
        # Positive and negative (exmp -> -5 left +5 right)
        # +1 to add 0 position
        for p, _ in enumerate(range((scale * 2) + 1)):
            # Replacing x by scale of the cartesian plane
            # Using y for the sake of practicality
            # as both y and x are the same there is no problem
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
            for i in res_y:
                if y == i:
                    frame[y] = frame[y][:i] + '@' + frame[y][i:]
                    frame[y] = frame[y].replace('@ ', '@')
                    # Are we at the center?
                    if y == zero:
                        frame[y] = frame[y].replace('@|', '@')
        return frame

    def example_text(self):
        # Set table (display) size as a var for convenience
        table_width = 40
        # Display anything you want
        frame = [
            'True?',
            'Small question',
            'Trying bigger question',
            'Is that even a question?'
        ]
        # Align text to R, L, C
        frame = self.align(table_width, frame, 'r')
        # Pass desired frame and table (display) size
        self.display(table_width, frame)

    def example_horizontal_bar(self):
        # Set bar graph columns as tuple matrixes
        table_width = 40
        columns = [
            (4, 'Russia'),
            (7, 'Ukraine'),
            (4, 'Argentina'),
            (2, 'Japan'),
            (9, 'Canada')
        ]
        frame = self.horizontal_bar(4, columns)
        frame = self.align(table_width, frame, 'l')
        self.display(table_width, frame)

    def example_pizza(self):
        table_width = 40
        table_height = 10
        slices = [
            (20, 'New Zeland'),
            (50, 'Australia'),
            (10, 'China'),
            (80, 'Mongolia'),
            (60, 'Germany'),
            (50, 'Poland')
        ]
        frame = self.pizza(table_height, slices)
        frame = self.align(table_width, frame, 'c')
        self.display(table_width, frame)

    def example_vertical_bar(self):
        table_width = 40
        rows = [
            (4, 'Russia'),
            (7, 'Ukraine'),
            (4, 'Argentina'),
            (2, 'Japan'),
            (9, 'Canada')
        ]
        frame = self.vertical_bar(rows)
        frame = self.align(table_width, frame, 'l')
        self.display(table_width, frame)

    def example_function(self):
        table_width = 40
        function = 'x+x'
        # 5 to left, right, top, bottom from 0
        cartesian_plane = 5
        frame = self.function(cartesian_plane, function)
        frame = self.align(table_width, frame, 'c')
        self.display(table_width, frame)
        # Another function
        function = 'x+1'
        frame = self.function(cartesian_plane, function)
        frame = self.align(table_width, frame, 'c')
        self.display(table_width, frame)
        # One more
        function = '2'
        frame = self.function(cartesian_plane, function)
        frame = self.align(table_width, frame, 'c')
        self.display(table_width, frame)
        # Last one I promise
        function = 'x - x * 2'
        frame = self.function(cartesian_plane, function)
        frame = self.align(table_width, frame, 'c')
        self.display(table_width, frame)

    def examples(self):
        self.example_text()
        self.example_horizontal_bar()
        self.example_pizza()
        self.example_vertical_bar()
        self.example_function()

def help():
    print(' Examples       : e ')
    print(' Help           : h ')
    print(' Clear          : c ')
    print(' Text           : t ')
    print(' Horizontal Bar : b ')
    print(' Pizza Bar      : p ')
    print(' Vertical Bar   : v ')
    print(' Function       : f ')
    print(' Quit           : q ')

def menu():
    p = Plotter()
    print('Type "h" for help ')
    while 1:
        option = input('@-->> ')
        if option == 'e':
            p.examples()
        if option == 'h':
            help()
        if option == 'c':
            print("\033[H\033[J", end="")
        if option == 't' or option == 'b' or option == 'v' or option == 'p' or option == 'f':
            table_width = int(input('Table width (40): '))
            frame = []
            end = 'no'
            position = ''
            while position not in ('r','l','c'):
                position = input('Position (l, r, c): ')
        if option == 't':
            while end != 'y':
                frame.append(input('Text to append: '))
                end = input('End (y, n): ')
            frame = p.align(table_width, frame, position)
            p.display(table_width, frame)
        if option == 'b':
            while end != 'y':
                column = (int(input('Column Value: ')), input('Column Label: '))
                frame.append(column)
                end = input('End (y, n): ')
            bar_width = int(input('Bar width (4): '))
            frame = p.horizontal_bar(bar_width, frame)
            frame = p.align(table_width, frame, position)
            p.display(table_width, frame)
        if option == 'p':
            table_height = int(input('Table Height (10): '))
            while end != 'y':
                row = (int(input('Slice Value: ')), input('Slice Label: '))
                frame.append(row)
                end = input('End (y, n): ')
            frame = p.pizza(table_height, frame)
            frame = p.align(table_width, frame, position)
            p.display(table_width, frame)
        if option == 'v':
            while end != 'y':
                row = (int(input('Row Value: ')), input('Row Label: '))
                frame.append(row)
                end = input('End (y, n): ')
            frame = p.vertical_bar(frame)
            frame = p.align(table_width, frame, position)
            p.display(table_width, frame)
        if option == 'f':
            function = input('Function (x+x): ')
            cartesian_plane = int(input('Catersian Plane (5): '))
            frame = p.function(cartesian_plane, function)
            frame = p.align(table_width, frame, position)
            p.display(table_width, frame)
        if option == 'q':
            raise SystemExit
menu()
