import random

from Game.Gamestate import GameState
from schools.school import School

def simulate_game(team1, team2):
    #team1 = School(team1_name)
    #team2 = School(team2_name)
    game = GameState(team1, team2)

    while game.clock > 0:
        game.run_play()

    print("\nFinal Score:")
    print(f"{team1.name}: {game.score[0]}")
    print(f"{team2.name}: {game.score[1]}")




