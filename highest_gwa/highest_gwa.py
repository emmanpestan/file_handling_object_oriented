class StudentGWA:
    def __init__(self, input_file):
        self.input_file = input_file

    def find_highest_gwa(self):
        with open(self.input_file, "r") as file:
            students = file.readlines()