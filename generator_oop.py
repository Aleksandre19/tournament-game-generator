class GameGenerator:
    def __init__(self):
        self.teams = None
        while True:
            self.teams = int(
                input("Enter the number of teams in the tournament: "))
            if self.teams < 2:
                print("The minimum number of teams is 2, try again. ")
            else:
                break


GameGenerator()
