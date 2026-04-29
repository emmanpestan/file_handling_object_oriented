class LifeWriter:
    def __init__(self, output_file):
        self.output_file = output_file

    def write_lines(self):
        with open(self.output_file, "w") as file:
            while True:
                line = input("Enter line: ")
                file.write(line + "\n")

                answer = input("Are there more lines y/n? ")

                if answer.lower() == "n":
                    break

        print("Done. Text saved to mylife.txt")


life_writer = LifeWriter("mylife.txt")
life_writer.write_lines()