"""
league_builder.py
@Author - Kellen Rice
Taking in a text file, or plain text from stdin create a soccer league
table and print the results.
"""

import sys
from League import League

# To be filled once input source is determined
all_matches = []

# Input will come from stdin
if len(sys.argv) > 1:
    print('file provided in argument: ' + sys.argv[1])
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        all_matches = [f.strip() for f in file]
else:
    print('stdin case!')
    all_matches = [line.strip() for line in sys.stdin]

league = League()
league.fill_league(all_matches)
league.print_table()

