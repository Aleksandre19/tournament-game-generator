class GameGenerator:
    def __init__(self):
        self.teams = None
        while True:
            self.teams = int(
                input("Enter the number of teams in the tournament: "))
            if self.teams < 2:
                print("The minimum number of teams is 2, try again. ")
            else:
                self.game_team_names(self.teams)
                break

    def game_team_names(self, teams):
        self.teams = teams
        self.team_names = {}
        while True:
            name = input(
                f"Enter the name for team  # {len(self.team_names) + 1}: ")

            if len(name) < 2:
                print("Team names must have at least 2 characters, try again.")
            # Chacking to find if name has max 2 characters.
            elif len(name.split(" ")) > 2:
                print("Team names may have at most 2 words, try again.")
            else:
                self.team_names[name] = 0

            # Breaking the while loop when all names
            # are edded in to the list
            if len(self.team_names) >= teams:
                self.number_games_played_by_teams(self.team_names)
                break

    def number_games_played_by_teams(self, team_names):
        self.team_names = team_names
        # Calculating a minimum number of the games for each team
        min_number = len(self.team_names) - 1
        count = 0
        finished = False

        # First loop to get the number of the games
        while True:
            games = int(
                input("Enter the number of games played by each team: "))
            if games < min_number:
                print(
                    "Invalid number of games. Each team plays each other at least once in the regular season, try again.")
            else:
                # Gettiing the wins numbers
                while True:
                    # Getting the team name from the dictionary
                    team_name = list(self.team_names.keys())[count]

                    wins = int(
                        input(f"Enter the number of wins Team {team_name} had: "))
                    if wins > games:
                        print(
                            f"The maximum number of wins is {games}, try again.")
                    elif wins < 0:
                        print("The minimum number of wins is 0, try again.")
                    else:
                        # After validation adding a wins to the teams accordingly
                        self.team_names[team_name] = wins
                        count += 1

                    # When all wins has been added breaking the loop
                    # and calling the game generator function
                    if count >= len(self.team_names):
                        count = 0
                        finished = True
                        break

            if finished:
                break


GameGenerator()
