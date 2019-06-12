import sys


class League:
    """League class holds games in a season and has ability to build and
    print league tables.

    Attributes:
        teams {(team_name: points)}: Dictionary of all teams and associated
        points for the season.

        table [(team_name, points)]: Sorted list of tuples, team name and
        points for season. Tie-breaker is alphabetical order.

        matches [string]: Raw text of matches throughout a season.

    """

    def __init__(self):
        self.teams = {}
        self.table = []
        self.matches = []

    def get_matches(self):
        """Fill matches with data from either stdin or from file passed
        from stdin

            Parameters:
                None: implicit in function is an argument passed via command line
                when program is run.

            Return:
                None: Function populates self.matches to be used later in
                calculating match results.

        """

        # Input will come from stdin or file from command line
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
            with open(input_file, 'r') as file:
                self.matches = [f.strip() for f in file]
        else:
            self.matches = [line.strip() for line in sys.stdin]
        #print('matches: ')
        #print(self.matches)

    def print_table(self):
        """Print the formatted league table from sorted table list

            Parameters:
                table [(name, points)]: Sorted list of tuples of meta team data

            Return:
                none: Function prints league data in desired format

        """
        if not self.table:
            return
        position_counter = 1
        # to test for ties in league table
        last_team_points = 0
        # keep track of ties for resuming league position
        tied_teams = 0
        first = True
        for team, score in self.table:
            if not first and last_team_points != score:
                position_counter += 1 + tied_teams
                tied_teams = 0
            elif last_team_points == score:
                tied_teams += 1
            elif not first:
                position_counter += 1
            print(str(position_counter) + '. ' + team + ', ' + str(score)+" pts")
            last_team_points = score
            first = False

    def fill_league(self):
        """ Populate teams with league meta-data, sort and assign to table

        Parameters:
            matches []: array list of individual matches with final scores

        Return:
            null: function merely populates teams and sorts into table

        function will take all matches and populate the teams dictionary
        with the correct points associated with each match outcome.
        Function currently sorts twice, to ensure alphabetical tie breaker.
        A more robust sort key could be used to make only 1 sort, but unsure
        on computational benefit.

        """
        if not self.matches:
            return

        for match in self.matches:
            teams = match.split(',')
            # Some teams have two names, split on space once from the right
            home = teams[0].strip().rsplit(' ', 1)
            away = teams[1].strip().rsplit(' ', 1)
            # Check/populate teams dict with new teams
            if home[0] not in self.teams:
                self.teams[home[0]] = 0
            if away[0] not in self.teams:
                self.teams[away[0]] = 0

            # Tie Case
            if int(home[1]) == int(away[1]):
                self.teams[home[0]] += 1
                self.teams[away[0]] += 1
            # Home Win
            if int(home[1]) > int(away[1]):
                self.teams[home[0]] += 3
            # Away Win
            if int(away[1]) > int(home[1]):
                self.teams[away[0]] += 3
        # first sort alphabetically
        self.table = sorted(self.teams.items(), key=lambda x: x[0])
        # then sort on points total
        self.table.sort(key=lambda x: x[1], reverse=True)
