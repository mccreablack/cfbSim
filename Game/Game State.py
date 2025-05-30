#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

class GameState:
    def __init__(self, team1, team2):
        self.offense = team1
        self.defense = team2
        self.down = 1
        self.distance = 10
        self.yardline = 25  # offense starts on own 25
        self.clock = 3600  # seconds remaining (60:00)
        self.possession = team1
        self.other_team = team2

    def switch_possession(self):
        self.offense, self.defense = self.defense, self.offense
        self.possession, self.other_team = self.other_team, self.possession
        self.down = 1
        self.distance = 10
        self.yardline = 75 - self.yardline  # flip field

    def is_touchdown(self):
        return self.yardline >= 100

    def is_turnover_on_downs(self):
        return self.down > 4

    def run_play(self):
        yards_gained = random.randint(-5, 15)
        print(f"{self.possession.name} ran a play for {yards_gained} yards.")
        self.yardline += yards_gained
        self.clock -= random.randint(5, 20)  # subtract 5-20 seconds

        if self.is_touchdown():
            print(f"TOUCHDOWN {self.possession.name}!")
            self.possession.score += 7
            self.switch_possession()
        elif yards_gained >= self.distance:
            print(f"{self.possession.name} got a first down!")
            self.down = 1
            self.distance = 10
        else:
            self.down += 1
            self.distance -= yards_gained
            if self.is_turnover_on_downs():
                print(f"{self.possession.name} turned it over on downs.")
                self.switch_possession()

