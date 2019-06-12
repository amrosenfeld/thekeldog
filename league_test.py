"""Test file for testing League.py"""

import pytest
from League import League


def test_sample_input(monkeypatch, capsys):
    """Test sample text given in challenge prompt"""

    monkeypatch.setattr('sys.stdin', open('./input_files/sample-input.txt'))
    league = League()
    league.get_matches()
    league.fill_league()
    league.print_table()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip() == '1. Tarantulas, 6 pts\n2. Lions, 5 pts\n3. FC Awesome, 1 pts\n3. Snakes, 1 pts\n5. Grouches, 0 pts'


def test_empty_input(monkeypatch, capsys):
    """Test when receiving input from an empty file"""

    monkeypatch.setattr('sys.stdin', open('./input_files/empty.txt'))
    league = League()
    league.get_matches()
    league.fill_league()
    league.print_table()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == ''


def test_all_tied_input(monkeypatch, capsys):
    """Test output when all teams have equal points"""

    monkeypatch.setattr('sys.stdin', open('./input_files/ties.txt'))
    league = League()
    league.get_matches()
    league.fill_league()
    league.print_table()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == '1. FC Awesome, 2 pts\n1. FC Wackapodamus, 2 pts\n1. Grouches, 2 pts\n1. Lions, 2 pts\n1. Snakes, 2 pts\n1. Tarantulas, 2 pts'


def test_another_league(monkeypatch, capsys):
    """Test output from a different set of league/game data"""

    monkeypatch.setattr('sys.stdin', open('./input_files/another-test.txt'))
    league = League()
    league.get_matches()
    league.fill_league()
    league.print_table()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == '1. Man Utd, 9 pts\n2. Arsenal, 3 pts\n3. Chelsea, 1 pts\n3. Man City, 1 pts'
