from collections import defaultdict

data = {
    "Hundro": {
        1: {"Winrate": 30.95, "Average ending place": 2.21, "Games": 42},
        2: {"Winrate": 35.38, "Average ending place": 2.29, "Games": 65},
        3: {"Winrate": 31.91, "Average ending place": 2.36, "Games": 47},
        4: {"Winrate": 22.22, "Average ending place": 2.67, "Games": 9},
    },
    "Ilban": {
        1: {"Winrate": 20.00, "Average ending place": 2.44, "Games": 25},
        2: {"Winrate": 33.33, "Average ending place": 2.52, "Games": 21},
        3: {"Winrate": 27.78, "Average ending place": 2.56, "Games": 36},
        4: {"Winrate": 29.82, "Average ending place": 2.33, "Games": 57},
    },
    "Tessia": {
        1: {"Winrate": 12.12, "Average ending place": 2.73, "Games": 33},
        2: {"Winrate": 26.09, "Average ending place": 2.48, "Games": 23},
        3: {"Winrate": 13.04, "Average ending place": 2.57, "Games": 23},
        4: {"Winrate": 20.83, "Average ending place": 2.54, "Games": 24},
    },
    "Ecaz": {
        1: {"Winrate": 32.00, "Average ending place": 2.56, "Games": 25},
        2: {"Winrate": 14.29, "Average ending place": 3.00, "Games": 21},
        3: {"Winrate": 14.71, "Average ending place": 2.79, "Games": 34},
        4: {"Winrate": 20.00, "Average ending place": 2.66, "Games": 50},
    },
    "Ariana": {
        1: {"Winrate": 13.04, "Average ending place": 2.48, "Games": 23},
        2: {"Winrate": 37.04, "Average ending place": 2.19, "Games": 27},
        3: {"Winrate": 26.09, "Average ending place": 2.35, "Games": 23},
        4: {"Winrate": 28.57, "Average ending place": 2.33, "Games": 21},
    },
    "Beast": {
        1: {"Winrate": 22.58, "Average ending place": 2.58, "Games": 31},
        2: {"Winrate": 21.95, "Average ending place": 2.61, "Games": 41},
        3: {"Winrate": 29.03, "Average ending place": 2.39, "Games": 31},
        4: {"Winrate": 14.55, "Average ending place": 2.85, "Games": 55},
    },
    "Baron": {
        1: {"Winrate": 25.00, "Average ending place": 2.50, "Games": 28},
        2: {"Winrate": 26.09, "Average ending place": 2.43, "Games": 46},
        3: {"Winrate": 24.00, "Average ending place": 2.38, "Games": 50},
        4: {"Winrate": 22.73, "Average ending place": 2.55, "Games": 44},
    },
    "Helena": {
        1: {"Winrate": 23.33, "Average ending place": 2.40, "Games": 30},
        2: {"Winrate": 21.74, "Average ending place": 2.70, "Games": 23},
        3: {"Winrate": 26.19, "Average ending place": 2.76, "Games": 42},
        4: {"Winrate": 27.08, "Average ending place": 2.44, "Games": 48},
    },
    "Leto": {
        1: {"Winrate": 32.14, "Average ending place": 2.25, "Games": 28},
        2: {"Winrate": 14.29, "Average ending place": 2.68, "Games": 28},
        3: {"Winrate": 20.00, "Average ending place": 2.64, "Games": 25},
        4: {"Winrate": 25.81, "Average ending place": 2.71, "Games": 31},
    },
    "Rhombur": {
        1: {"Winrate": 25.81, "Average ending place": 2.55, "Games": 31},
        2: {"Winrate": 30.77, "Average ending place": 2.46, "Games": 26},
        3: {"Winrate": 34.78, "Average ending place": 2.26, "Games": 23},
        4: {"Winrate": 15.00, "Average ending place": 2.55, "Games": 20},
    },
    "Paul": {
        1: {"Winrate": 18.92, "Average ending place": 2.38, "Games": 37},
        2: {"Winrate": 6.67, "Average ending place": 3.07, "Games": 15},
        3: {"Winrate": 0.00, "Average ending place": 3.17, "Games": 18},
        4: {"Winrate": 30.00, "Average ending place": 2.30, "Games": 10},
    },
    "Yuna": {
        1: {"Winrate": 22.86, "Average ending place": 2.51, "Games": 35},
        2: {"Winrate": 14.71, "Average ending place": 2.94, "Games": 34},
        3: {"Winrate": 30.77, "Average ending place": 2.62, "Games": 13},
        4: {"Winrate": 57.14, "Average ending place": 2.00, "Games": 7},
    },
    "Ilesa": {
        1: {"Winrate": 33.33, "Average ending place": 1.78, "Games": 9},
        2: {"Winrate": 25.00, "Average ending place": 2.42, "Games": 12},
        3: {"Winrate": 33.33, "Average ending place": 2.00, "Games": 9},
        4: {"Winrate": 16.67, "Average ending place": 2.83, "Games": 6},
    },
    "Memnon": {
        1: {"Winrate": 0.00, "Average ending place": 2.43, "Games": 7},
        2: {"Winrate": 0.00, "Average ending place": 3.50, "Games": 2},
        3: {"Winrate": 0.00, "Average ending place": 2.00, "Games": 2},
        4: {"Winrate": 0.00, "Average ending place": 2.67, "Games": 3},
    }
}

# Initialize a dictionary to hold lists of leaders for each position
position_lists = defaultdict(list)

# Iterate over each leader and their starting position
for leader, positions in data.items():
    for position, stats in positions.items():
        position_lists[position].append((leader, stats["Average ending place"], stats["Games"]))

# Sort the lists of leaders for each position by average ending place
for position, leaders in position_lists.items():
    position_lists[position] = sorted(leaders, key=lambda x: x[1])

# Display the sorted lists for each position
for position, leaders in position_lists.items():
    print(f"Position {position}:")
    for leader, avg_ending_place, games in leaders:
        print(f"Leader: {leader}, Average ending place: {avg_ending_place}, Games: {games}")
    print()
