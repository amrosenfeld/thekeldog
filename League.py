class League:
    def __init__(self):
        self.teams = {}
        self.table = []

    def print_table(self):
        position_counter = 1
        last_team_points = 0
        tied_teams = 0
        first = True
        for team,score in self.table:
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

    def fill_league(self, matches):
        """
        matches [] - array list of individual matches with final scores
        function will take all matches and populate the teams dictionary
        with the correct points associated with each match outcome
        """
        for match in matches:
            teams = match.split(',')
            # Some teams have two names, split on space once from the right
            home = teams[0].strip().rsplit(' ', maxsplit=1)
            away = teams[1].strip().rsplit(' ', maxsplit=1)
            # Check/populate teams table with new teams
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
