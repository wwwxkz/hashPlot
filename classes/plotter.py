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

    def pizza(self, radius, slices):
        # Frame can not initialize empty as using += operator
        frame = [' ']
        last_frame = 0
        rec = 2 * radius + 1
        for i in range(rec):
            for j in range(rec):
                x = i - radius
                y = j - radius
                if x * x + y * y <= radius * radius + 1:
                    frame[last_frame] += '#'
                else:
                    frame[last_frame] += ' '
            last_frame += 1
            # Append array in matrix as \n in string
            frame.append(' ')
        return frame
    
    def function(self, scale, function):
        frame = []
        # (0,0) in cartesian plane
        # if not even, round it to the next number and do not
        # nothing as it has a middle number
        zero = round(scale)
        # Get function positions (x,y) based on scale
        res_y = []
        res_y_negative = []
        # Positive and negative (exmp -> -5 left +5 right)
        # +1 to add 0 position
        for p, _ in enumerate(range((scale * 2) + 1)):
            # Replacing x by scale of the cartesian plane
            # Using y for the sake of practicality
            # as both y and x are the same there is no problem
            replace_x = str(function.replace('x', str(p)))
            res_y.append(zero - eval(replace_x))
        for p, _ in enumerate(range((scale * 2) + 1)):
            # for negative section 
            # x = -5, -4, -3, -2, -1
            replace_x = str(function.replace('x', str(-p)))
            res_y_negative.append(zero + eval(replace_x))
        print('res_y: ', res_y)
        print('res_y_n: ', res_y_negative)
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
            for index, i in enumerate(res_y): # index for using the same loop for res_y_negative
                if y == i:
                    # invert side of i
                    # if it is in 3 in a scale of 0-11 with the middle point 6
                    # i will turn 9, and if it is 9 it will turn 3
                    # in that will we can centralize the x and y at the middle point
                    # of our cartesian table
                    # that is because an array will always start in 0 from the left
                    if i > scale:
                        distance_from_zero =  i - scale
                        # i positive
                        i_p = scale - distance_from_zero
                    else:
                        distance_from_zero = scale - i
                        i_p = scale + distance_from_zero
                    frame[y] = frame[y][:i_p] + '@' + frame[y][i_p:]
                    frame[y] = frame[y].replace('@ ', '@')
                    # Are we at the center?
                    if y == zero:
                        frame[y] = frame[y].replace('@|', '@')
                if y == res_y_negative[index]:
                    print('i: ', i)
                    frame[y] = frame[y][:i] + '@' + frame[y][i:]
                    frame[y] = frame[y].replace('@ ', '@')
        return frame