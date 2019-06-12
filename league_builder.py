"""
league_builder.py
@Author - Kellen Rice
Taking in a text file, or plain text from stdin create a soccer league
table and print the results.
"""

from League import League


league = League()
league.get_matches()
league.fill_league()
league.print_table()

