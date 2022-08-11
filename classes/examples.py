class Examples:
    def __init__(self, plotter):
        self.example_text(plotter)
        self.example_horizontal_bar(plotter)
        self.example_pizza(plotter)
        self.example_vertical_bar(plotter)
        self.example_function(plotter)

    def example_text(self, plotter):
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
        frame = plotter.align(table_width, frame, 'r')
        # Pass desired frame and table (display) size
        plotter.display(table_width, frame)

    def example_horizontal_bar(self, plotter):
        # Set bar graph columns as tuple matrixes
        table_width = 40
        columns = [
            (4, 'Russia'),
            (7, 'Ukraine'),
            (4, 'Argentina'),
            (2, 'Japan'),
            (9, 'Canada')
        ]
        frame = plotter.horizontal_bar(4, columns)
        frame = plotter.align(table_width, frame, 'l')
        plotter.display(table_width, frame)

    def example_pizza(self, plotter):
        table_width = 40
        slices = [
            (20, 'New Zeland'),
            (50, 'Australia'),
            (10, 'China'),
            (80, 'Mongolia'),
            (60, 'Germany'),
            (50, 'Poland')
        ]
        frame = plotter.pizza(8, slices)
        frame = plotter.align(table_width, frame, 'c')
        plotter.display(table_width, frame)

    def example_vertical_bar(self, plotter):
        table_width = 40
        rows = [
            (4, 'Russia'),
            (7, 'Ukraine'),
            (4, 'Argentina'),
            (2, 'Japan'),
            (9, 'Canada')
        ]
        frame = plotter.vertical_bar(rows)
        frame = plotter.align(table_width, frame, 'l')
        plotter.display(table_width, frame)

    def example_function(self, plotter):
        table_width = 40
        function = 'x+x'
        # 5 to left, right, top, bottom from 0
        cartesian_plane = 5
        frame = plotter.function(cartesian_plane, function)
        frame = plotter.align(table_width, frame, 'c')
        plotter.display(table_width, frame)
        # Another function
        function = 'x+1'
        frame = plotter.function(cartesian_plane, function)
        frame = plotter.align(table_width, frame, 'c')
        plotter.display(table_width, frame)
        # One more
        function = '2'
        frame = plotter.function(cartesian_plane, function)
        frame = plotter.align(table_width, frame, 'c')
        plotter.display(table_width, frame)
        # Last one I promise
        function = 'x - x * 2'
        frame = plotter.function(cartesian_plane, function)
        frame = plotter.align(table_width, frame, 'c')
        plotter.display(table_width, frame)