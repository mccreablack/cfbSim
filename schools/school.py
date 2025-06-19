# school/school.py

from .coach import Coach, AthleticDirector
from .player import Player

class School:
    def __init__(self, name, head_coach, off_coord, def_coord, ad, fanbase_size, money,prestiege, roster,region, sub_region):
        self.name = name
        self.head_coach = head_coach
        self.off_coord = off_coord
        self.def_coord = def_coord
        self.athletic_director = ad
        self.fanbase_size = fanbase_size
        self.money = money
        self.prestiege = prestiege
        self.roster = roster
        self.region = region
        self.sub_region = sub_region
