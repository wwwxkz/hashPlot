from classes.examples import *
from classes.plotter import *

class Menu:
    def __init__(self):
        plotter = Plotter()
        print('Type "h" for help ')
        while 1:
            option = input('@-->> ')
            if option == 'e':
                Examples(plotter)
            if option == 'h':
                self.help()
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
                frame = plotter.align(table_width, frame, position)
                plotter.display(table_width, frame)
            if option == 'b':
                while end != 'y':
                    column = (int(input('Column Value: ')), input('Column Label: '))
                    frame.append(column)
                    end = input('End (y, n): ')
                bar_width = int(input('Bar width (4): '))
                frame = plotter.horizontal_bar(bar_width, frame)
                frame = plotter.align(table_width, frame, position)
                plotter.display(table_width, frame)
            if option == 'p':
                radius = int(input('Radius (8): '))
                while end != 'y':
                    row = (int(input('Slice Value: ')), input('Slice Label: '))
                    frame.append(row)
                    end = input('End (y, n): ')
                frame = plotter.pizza(radius, frame)
                frame = plotter.align(table_width, frame, position)
                plotter.display(table_width, frame)
            if option == 'v':
                while end != 'y':
                    row = (int(input('Row Value: ')), input('Row Label: '))
                    frame.append(row)
                    end = input('End (y, n): ')
                frame = plotter.vertical_bar(frame)
                frame = plotter.align(table_width, frame, position)
                plotter.display(table_width, frame)
            if option == 'f':
                function = input('Function (x+x): ')
                cartesian_plane = int(input('Catersian Plane (5): '))
                frame = plotter.function(cartesian_plane, function)
                frame = plotter.align(table_width, frame, position)
                plotter.display(table_width, frame)
            if option == 'q':
                raise SystemExit

    def help(self):
        print(' Examples       : e ')
        print(' Help           : h ')
        print(' Clear          : c ')
        print(' Text           : t ')
        print(' Horizontal Bar : b ')
        print(' Pizza Bar      : p ')
        print(' Vertical Bar   : v ')
        print(' Function       : f ')
        print(' Quit           : q ')