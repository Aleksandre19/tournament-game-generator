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
                break


GameGenerator()
