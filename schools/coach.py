# school/coach.py

class Coach:
    def __init__(self, name, age, archetype, off, deff, off_dev, def_dev, off_rec, def_rec, wins, losses):
        self.name = name
        self.age = age
        self.archetype = archetype
        self.off = off
        self.deff = deff
        self.off_dev = off_dev
        self.def_dev = def_dev
        self.off_rec = off_rec
        self.def_rec = def_rec
        self.wins = wins
        self.losses = losses

class AthleticDirector:
    def __init__(self, name, age, tact, patience):
        self.name = name
        self.age = age
        self.tact = tact
        self.patience = patience
