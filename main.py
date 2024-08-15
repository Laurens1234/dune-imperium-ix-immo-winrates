import csv

import regex as re  # import the regex module


# Function to parse the input string and extract relevant information
def parse_data(input_string):
    # Use regex to extract game IDs, player names, positions, and scores
    matches = re.findall(r"(?:Game ID: (\d+)|(\d+)(?:st|nd|rd|th):(@[\w\s'|.@#🏍\[\]()/0-9\p{Emoji}-\"-]+)\s*:\s*(\w+):\s*Position:\s*(\d+)\s*([-+]?\d*\.\d+|\d+))", input_string, flags=re.UNICODE)
    game_id = None
    parsed_data = []
    ending_position = 1  # Initialize ending position
    missed_matches = []
    for match in matches:
        if match[0]:  # Game ID match
            game_id = int(match[0])
            ending_position = 1  # Reset ending position for each new game
        else:  # Player data match
            if len(match) == 6:  # Check if all groups were captured
                parsed_data.append((game_id, match[2], match[3], match[4], match[5], ending_position))
                ending_position += 1  # Increment ending position for each player data match
            else:  # If any group is missed
                missed_matches.append(match)
    if missed_matches:
        print("Warning: Some matches were not captured completely:", missed_matches)
    return parsed_data

# Function to write the parsed data to a CSV file
def write_to_csv(data, csv_filename):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Game ID', 'Player', 'Leader', 'Starting Position', 'Score', 'Ending Position']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow({'Game ID': item[0], 'Player': item[1], 'Leader': item[2], 'Starting Position': item[3], 'Score': item[4], 'Ending Position': item[5]})

# Read data from a file
def read_data_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Sample input file name
input_filename = 'dataset_full_s7.txt'

# Read the input data from the file
input_data = read_data_from_file(input_filename)

# Parse the data
parsed_data = parse_data(input_data)

# Write the parsed data to CSV
write_to_csv(parsed_data, 'dune_imperium_data_full_s7.csv')
