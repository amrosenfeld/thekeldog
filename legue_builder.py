
input_file = "sample-input.txt"

with open(input_file, 'r') as file:
    all_matches = file.readlines()
    [print (match.strip()) for match in all_matches]


class League:
    def __init__(self):
        self.teams = {}
        self.table = []

    def print_table(self):

