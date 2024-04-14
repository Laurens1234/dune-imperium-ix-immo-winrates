# leader_percentage.py

# Function to calculate the percentage of times each leader ends in each ending position
def calculate_leader_percentage(data):
    leader_count = {}
    leader_total_games = {}
    leader_total_wins = {}
    leader_winrate_from_starting_position = {}

    for item in data:
        leader = item[2]
        starting_position = item[3]
        ending_position = item[5]

        leader_count.setdefault(leader, {}).setdefault(ending_position, 0)
        leader_count[leader][ending_position] += 1

        leader_total_games.setdefault(leader, 0)
        leader_total_games[leader] += 1

        if ending_position == 1:
            leader_total_wins.setdefault(leader, 0)
            leader_total_wins[leader] += 1

        leader_winrate_from_starting_position.setdefault(leader, {}).setdefault(starting_position, [0, 0])
        leader_winrate_from_starting_position[leader][starting_position][0] += 1
        if ending_position == 1:
            leader_winrate_from_starting_position[leader][starting_position][1] += 1

    leader_percentage = {}
    leader_average_ending_place = {}
    leader_average_winrate = {}
    for leader, counts in leader_count.items():
        leader_percentage[leader] = {}
        leader_average_ending_place[leader] = sum([pos * count for pos, count in counts.items()]) / leader_total_games[leader] if leader_total_games[leader] > 0 else 0
        leader_average_winrate[leader] = (leader_total_wins.get(leader, 0) / leader_total_games[leader]) * 100 if leader_total_games[leader] > 0 else 0
        for position, count in counts.items():
            leader_percentage[leader][position] = (count / leader_total_games[leader]) * 100 if leader_total_games[leader] > 0 else 0

    # Sort leaders by average ending place (lowest to highest)
    sorted_leaders_ending_place = sorted(leader_average_ending_place.items(), key=lambda x: x[1])

    # Sort leaders by average winrate (highest to lowest)
    sorted_leaders_winrate = sorted(leader_average_winrate.items(), key=lambda x: x[1], reverse=True)

    # Sort leaders by total games (highest to lowest)
    sorted_total_games = sorted(leader_total_games.items(), key=lambda x: x[1], reverse=True)

    return leader_percentage, sorted_leaders_ending_place, sorted_leaders_winrate, leader_average_ending_place, leader_total_games, sorted_total_games, leader_winrate_from_starting_position

if __name__ == "__main__":
    import csv
    import sys

    # Read data from CSV file
    def read_data_from_csv(csv_filename):
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [(int(row['Game ID']), row['Player'], row['Leader'], int(row['Starting Position']), float(row['Score']), int(row['Ending Position'])) for row in reader]

    # Check if the CSV filename is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python leader_percentage.py <csv_filename>")
        sys.exit(1)

    csv_filename = sys.argv[1]

    # Read data from the CSV file
    parsed_data = read_data_from_csv(csv_filename)

    # Calculate leader percentage for each ending position, average ending place, average winrate, total games, and winrate from starting position
    leader_percentage, sorted_leaders_ending_place, sorted_leaders_winrate, leader_average_ending_place, leader_total_games, sorted_total_games, leader_winrate_from_starting_position = calculate_leader_percentage(parsed_data)

    # Print leader percentage for each ending position
    print("Percentage of times each leader ends in each ending position:")
    for leader, average_ending_place in sorted_leaders_ending_place:
        print(f"{leader}:")
        print(f"  Average ending place: {average_ending_place:.2f}")
        print(f"  Average winrate: {dict(sorted_leaders_winrate)[leader]:.2f}%")
        for position, percentage in sorted(leader_percentage[leader].items()):
            print(f"  {position}st place: {percentage:.2f}%")
        print(f"  Total games: {leader_total_games[leader]}")

    # Print list of average ending place at the end
    print("\nAverage ending place for each leader:")
    for leader, average_ending_place in sorted(leader_average_ending_place.items(), key=lambda x: x[1]):
        print(f"{leader}: {average_ending_place:.2f}")

    # Print list of total games (highest to lowest)
    print("\nTotal number of games for each leader (sorted from highest to lowest):")
    for leader, total_games in sorted_total_games:
        print(f"{leader}: {total_games}")

    # Print winrate for each leader from each starting position
    print("\nWinrate for each leader from each starting position:")
    for leader, starting_positions in leader_winrate_from_starting_position.items():
        print(f"{leader}:")
        for starting_position, winrate_data in sorted(starting_positions.items()):
            total_games = winrate_data[0]
            total_wins = winrate_data[1]
            winrate = (total_wins / total_games) * 100 if total_games > 0 else 0
            average_ending_place = sum([item[5] for item in parsed_data if item[2] == leader and item[3] == starting_position]) / total_games if total_games > 0 else 0
            print(f"  Starting position {starting_position}:")
            print(f"    Winrate: {winrate:.2f}% ({total_games} games)")
            print(f"    Average ending place: {average_ending_place:.2f}")

    # Print list of leaders sorted by winrate (highest to lowest)
    print("\nList of leaders sorted by winrate (highest to lowest):")
    for leader, winrate in sorted_leaders_winrate:
        print(f"{leader}: {winrate:.2f}%")