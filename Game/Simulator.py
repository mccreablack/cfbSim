import random

from game.state import GameState
from teams.team import Team

def simulate_game(team1_name, team2_name):
    team1 = Team(team1_name)
    team2 = Team(team2_name)
    game = GameState(team1, team2)

    while game.clock > 0:
        game.run_play()

    print("\nFinal Score:")
    print(f"{team1.name}: {team1.score}")
    print(f"{team2.name}: {team2.score}")




