import csv
import random
from collections import defaultdict

MAX_OFFERS = 20  # Only consider top 20 schools per player

# Dummy function to simulate interest score for a player-school pair
def get_interest_score(player, school):
    base = int(player['Victory']) + int(player['Playtime']) + int(player['Money'])
    if player['Hometown'] in school_regions.get(school, ''):
        base += int(player['Local'])  # hometown boost
    return base + random.randint(-10, 10)

# Example mapping: school -> region
school_regions = {
    'Alabama': 'SE',
    'Ohio State': 'MW',
    'Air Force': 'MT',
    'USC': 'W',
    # ... all 136 schools
}

# === Load players ===
with open('players_active.csv', newline='') as f:
    reader = csv.DictReader(f)
    all_players = list(reader)

# === Filter uncommitted players ===
portal_players = [p for p in all_players if p['Current School'] == 'Portal']

# === Build set of schools ===
all_schools = sorted(set(p['Current School'] for p in all_players if p['Current School'] != 'Portal'))

# === Assign recruits ===
for player in portal_players:
    # Get top schools by interest
    school_scores = [(school, get_interest_score(player, school)) for school in all_schools]
    school_scores.sort(key=lambda x: x[1], reverse=True)
    top_choices = school_scores[:MAX_OFFERS]

    # Choose school based on weighted random (or always choose top for now)
    chosen_school = top_choices[0][0]  # TODO: smarter choice logic

    # Assign player
    player['Current School'] = chosen_school

# === Save updated roster ===
fieldnames = list(all_players[0].keys())
with open('players_active.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_players)
