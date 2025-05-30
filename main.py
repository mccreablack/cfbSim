# main.py

from schools import Coach, AthleticDirector, Player, School

hc = Coach("John Smith", 55, "CEO", 80, 60, 70, 65, 75, 60, 120, 40)
oc = Coach("Mike Lane", 42, "Spread", 85, 50, 72, 60, 80, 55, 30, 10)
dc = Coach("Rick Stone", 50, "Blitz", 60, 90, 65, 75, 50, 70, 40, 20)
ad = AthleticDirector("Nancy Sharp", 60, 85, 90)

#players = [
#    Player("Drew Adams", "QB", 2, 90, 70, 80, 85, 88, 89),
#    Player("Isaiah Jones", "RB", 3, 92, 78, 75, 88, 80, 87),
#]

school = School("State University", hc, oc, dc, ad, 80000, 2000000, players)

print(school.name)  # State University
print(school.head_coach.name)  # John Smith
print(school.roster[0].name)   # Drew Adams

from game.simulator import simulate_game

simulate_game("Texas", "Alabama")
