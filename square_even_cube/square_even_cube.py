import os


class IntegerProcessor:
    def __init__(self, input_file, double_file, triple_file):
        folder = os.path.dirname(__file__)
        self.input_file = os.path.join(folder, input_file)
        self.double_file = os.path.join(folder, double_file)
        self.triple_file = os.path.join(folder, triple_file)

    def create_double_and_triple_files(self):
        even_squares = []
        odd_cubes = []