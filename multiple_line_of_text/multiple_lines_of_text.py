class LifeWriter:
    def __init__(self, output_file):
        self.output_file = output_file

    def write_lines(self):
        with open(self.output_file, "w") as file:
            while True:
                line = input("Enter line: ")
                file.write(line + "\n")