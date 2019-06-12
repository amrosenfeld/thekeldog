## League Builder

A Python Program to take input from text files of soccer match outcomes and
transform them into league tables given the following rules.

### The rules

In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A
loss is worth 0 points. If two or more teams have the same number of points,
they should have the same rank and be printed in alphabetical order (as in the
tie for 3rd place in the sample data).

### How to run

There is currently a `run_all_leagues.sh` file in the directory. When run,
this file will run `league_builder.py` on all the current input files in the directory
as `stdin` redirects AND as command line arguments.

#### Testing
`run_all_leagues.sh` will then install the required unit testing package `pytest` via
`pip install` and then run `pytest`. 

#### Note:
If at first `run_all_leagues.sh` does not run correctly, please check the filepath at the top
of the file following the `#!` to ensure bash is being referenced correctly.
Permissions may also need to be granted via command `chmod 7xx run_all_leagues.sh`

`league_builder.py` can of course be run on it's own with an input file provided
either as `stdin` with file redirect operator i.e. `python3 league_builder.py < sample-input.txt`
or as a command line argument i.e. `python3 league_builder.py sample-input.txt`

### Platform support
This program should run on all Linux/Unix compatible systems.
Tested on both Windows bash and Mac/OS
