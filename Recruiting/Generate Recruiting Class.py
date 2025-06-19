#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# recruiting.py

import csv
import random
import uuid

# === CONFIGURABLE CONSTANTS ===
NUM_RECRUITS = 3000
PLAYER_ALL_CSV = 'players_all.csv'
RECRUITS_CSV = 'recruits.csv'

REGION_DISTRIBUTION = {
    "NW": 0.0449,
    "W":  0.0897,
    "MT": 0.0449,
    "SW": 0.1859,
    "C":  0.0769,
    "MW": 0.1474,
    "SE": 0.1859,
    "E":  0.1474,
    "NE": 0.0769
}



# Star rating probabilities
STAR_PROBS = [
    (5, 0.01),
    (4, 0.09),
    (3, 0.50),
    (2, 0.30),
    (1, 0.05),
    (0, 0.05)
]

# Star to Overall ranges
STAR_TO_OVERALL = {
    5: (70, 90),
    4: (60, 70),
    3: (50, 60),
    2: (40, 50),
    1: (30, 40),
    0: (0, 30)
}

# Position weights (must sum to 100)
POSITION_WEIGHTS = {
    'QB':  [15, 20, 30, 10, 25],
    'RB':  [30, 25, 10, 20, 15],
    'WR':  [30, 15, 25, 20, 10],
    'TE':  [20, 30, 25, 10, 15],
    'OT':  [15, 55,  0, 20, 10],
    'OG':  [20, 55,  0, 15, 10],
    'C':   [15, 55,  0, 10, 20],
    'FB':  [30, 30, 15, 15, 10],
    'DL':  [15, 30, 25, 20, 10],
    'EDGE':[25, 30, 15, 20, 10],
    'LB':  [20, 20, 30, 15, 15],
    'CB':  [25, 15, 30, 20, 10],
    'S':   [25, 10, 15, 20, 30],
    'P':   [ 0, 50, 50,  0,  0],
    'K':   [ 0, 50, 50,  0,  0]
}
PosistionVectors={
'QB' : [
[-2,0,3,-1,-2, 6],
[1,-1, -2, -1, 3, 6],
[-1,3,-1,1,-1, 2],
[4, 0, -2, 0, 0, 0]
],

'RB': [
[3,-2,-2,-1,0,6],
[-1,3, -1, -1, -1,6],
[-1,-1,-1,4,-1,4],
[-2, 1, 6, -2, 1,2]
],

'WR' : [
[3,0,-2,-1,-2,6],
[-1,-1, 3, -1, -1,6],
[-1,-1,-1,4,-1,4],
[-2, 1, 1, -2, 6,2]
],

'TE' : [
[-1,3,-2,-2,0,6],
[-1,-1, 3, -1, -1,6],
[4, -1, -1, -1, -1, 4],
[-2, -2, 1, 6, 1,2]
],

'OT' : [
[-2,2,-2,-3,-2,6],
[-1,-1, -3, 4, -1,5],
[-3,1,0,1,-3,4],
[6, -2, 3, -1, 4,2]
],

'OG' : [
[-3,2,-2,-2,-2,6],
[4,-1, -3, -1, -1,5],
[1,1,0,-3,-3,4],
[-1, -2, 3, 6, 4,2]
],

'C': [
[-2,2,-2,-2,-3,6],
[-1,-1, -3, -1, 4,5],
[-3,1,0,-3,1,4],
[6, -2, 3, 4, -1,2]
],

'FB' : [
[3,-2,1,-1,-3,6],
[-2,3, -1, 1,-3,6],
[-1,-1,3,-1,3,1],
[-1, -1, -1, 3, 3,1]
],

'DL': [
[0,3,-2,-1,-2, 6],
[-1,-1, 3, -1, -1, 6],
[-1,-1,-1,4,-1, 4],
[1, -2, 1, -2, 6, 2]
],

'EDGE' : [
[-2,3,0,-1,-2,6],
[3,-1, -1, -1, -1,6],
[-1,-1,-1,4,-1,4],
[1, -2, 1, -2, 6,2]
],

'LB': [
[-2,-1,2,0,0,6],
[-1,4, -1, -1, -1,6],
[4,-1,-1,-1,-1,6],
[-1, -2, 1, 1, 1,6]
],

'CB' : [
[-2,0,3,-1,-2,6],
[3,-1, -1, -1, -1,6],
[-1,-1,-1,4,-1,4],
[1, 1, -2, -2, 6,2]
],
'S' : [
[-2,-2,0,-1,3,6],
[3,-1, -1, -1, -1,6],
[-1,-1,-1,4,-1,4],
[1, 6, 1, -2, -2,2]
],
'P' : [
[2,-1,1,2,2,6],
[-2,1, -1, -2, -2,6],
[-2,-1,1,-2,-2,4],
[-2, 1, -1, -2, -2,4]
],
'K': [
[2,-1,1,2,2,6],
[-2,1, -1, -2, -2,6],
[-2,-1,1,-2,-2,4],
[-2, 1, -1, -2, -2,4]
]

}
POSITIONS = list(POSITION_WEIGHTS.keys())



def choose_star():
    r = random.random()
    cumulative = 0
    for star, prob in STAR_PROBS:
        cumulative += prob
        if r < cumulative:
            return star
    return 0  # fallback


def generate_stats(overall,vector):
    stats = [overall,overall,overall,overall,overall]
    for k in vector:
        r= random.randint(-2,2)
        for i in range(len(stats)):
            stats[i] += k[i]*(k[5]+r)

    return stats




def get_next_player_id():
    try:
        with open(PLAYER_ALL_CSV, newline='') as f:
            reader = csv.DictReader(f)
            ids = [int(row["ID No."]) for row in reader if row["ID No."].isdigit()]
            return max(ids) + 1 if ids else 0
    except FileNotFoundError:
        return 0

def generate_name():
    first = random.choice(["Jalen", "Trey", "DeShawn", "Bryce", "Ethan", "Caleb", "Zion", "Tyler"])
    last = random.choice(["Smith", "Williams", "Brown", "Taylor", "Johnson", "White", "Scott", "Walker"])
    return f"{first} {last}"

def generate_recruit(region,next_id,stars,overall,posistion,stats,weights):
    return {
        "id" : next_id,
        "name": generate_name(),
        "position": posistion,
        "stars": stars,
        "region": region,
        "overall": overall,
        "speed":stats[0],
        "strength":stats[1],
        "tech":stats[2],
        "agi":stats[3],
        "int":stats[4],
        "victory": random.randint(0, 100),
        "local": random.randint(0, 100),
        "playtime": random.randint(0, 100),
        "money": random.randint(0, 100),
        "Actual Overall": (stats[0]*weights[0]+stats[1]*weights[1]+stats[2]*weights[2]+stats[3]*weights[3]+stats[4]*weights[4])/100
    }

def generate_recruiting_class(total=3000, output_file="Recruits.csv", existing_file="Players_All.csv"):
    recruits = []
    next_id = get_next_player_id()
    
    
    for region, percent in REGION_DISTRIBUTION.items():
        count = round(total * percent)
        for _ in range(count):
            stars = choose_star()
            overall =random.randint(*STAR_TO_OVERALL[stars])
            posistion = random.choice(POSITIONS)
            weights = POSITION_WEIGHTS[posistion]
            vector = PosistionVectors[posistion]
            stats = generate_stats(overall,vector)
            recruit = generate_recruit(region,next_id,stars,overall,posistion,stats,weights)
            recruits.append(recruit)
            next_id += 1

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=recruits[0].keys())
        writer.writeheader()
        writer.writerows(recruits)

    print(f"Generated {len(recruits)} recruits in {output_file}")


if __name__ == "__main__":
    generate_recruiting_class()

