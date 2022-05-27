<h1 align="center">Tournament Game Generator programme.</h1>

#### Programme for the project.

This is a simple game generator programme which I got to write as a project for the [programmingexpert.io](https://www.programmingexpert.io/).The programme is written in Python with the Object Oriented Programminge style.

#### How to run the programme?

To run the programe simple download a `generator_oop.py` file and run it in your terminal. You can do it or clone it by clicking on the green `code` button at the top right side.

#### The programme assumes...

The programme assumes that a user enters as valid data as it asks to do. For example if programe asks to enter number of teams it assums that a user enters a integer and not a string. It does not make such checks.

#### Checks made by the programme:

- A minimum number of teams.
- If the team name is made minimum of two characters.
- If team name has maximum two words length.
- Minimum number of the games.
- Maximum and minimum number of the wins teams has won.

#### Programme result.

The programme finally generates a table in which the team on the first place playes to the team on the last place, a team on the second place plays to the team on the before last place and so on.

#### Example of the programme:

```
Enter the number of teams in the tournament: 1
The minimum number of teams is 2, try again.
Enter the number of teams in the tournament: 4
Enter the name for team  # 1: AA
Enter the name for team  # 2: BB
Enter the name for team  # 3: CC
Enter the name for team  # 4: D
Team names must have at least 2 characters, try again.
Enter the name for team  # 4: D Is Great
Team names may have at most 2 words, try again.
Enter the name for team  # 4: DD
Enter the number of games played by each team: 2
Invalid number of games. Each team plays each other at least once in the regular season, try again.
Enter the number of games played by each team: 3
Enter the number of wins Team AA had: 2
Enter the number of wins Team BB had: 1
Enter the number of wins Team CC had: 0
Enter the number of wins Team DD had: -2
The minimum number of wins is 0, try again.
Enter the number of wins Team DD had: 3
Generating the games to be played in the first round of the tournament...
Home: CC VS Away: DD
Home: BB VS Away: AA
```
