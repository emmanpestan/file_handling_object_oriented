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

        with open(self.input_file, "r") as file:
            numbers = file.readlines()

        for number in numbers:
            number = number.strip()

            if number == "":
                continue

            number = int(number)

            if number % 2 == 0:
                even_squares.append(str(number ** 2))
            else:
                odd_cubes.append(str(number ** 3))