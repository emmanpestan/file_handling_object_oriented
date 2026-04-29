class NumberSplitter:
    def __init__(self, input_file, even_file, odd_file):
        self.input_file = input_file
        self.even_file = even_file
        self.odd_file = odd_file

    def split_numbers(self):
        with open(self.input_file, "r") as file:
            numbers = file.readlines()