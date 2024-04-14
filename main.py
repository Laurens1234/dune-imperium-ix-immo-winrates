import csv
import re


# Function to parse the input string and extract relevant information
def parse_data(input_string):
    # Use regular expression to extract player names, positions, and scores
    matches = re.findall(r"(?:Game ID: (\d+)|@(\w+)\s*:(\w+):\s*Position:\s*(\d+)\s*([-+]?\d*\.\d+|\d+))", input_string)
    game_id = None
    parsed_data = []
    for idx, match in enumerate(matches):
        if match[0]:  # Game ID match
            game_id = int(match[0])
        else:  # Player data match
            ending_position = (idx % 4) + 1  # Calculate ending position
            parsed_data.append((game_id, match[1], match[2], match[3], match[4], ending_position))
    return parsed_data

# Function to write the parsed data to a CSV file
def write_to_csv(data, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
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
input_filename = 'dataset.txt'

# Read the input data from the file
input_data = read_data_from_file(input_filename)

# Parse the data
parsed_data = [data for data in parse_data(input_data)]

# Write the parsed data to CSV
write_to_csv(parsed_data, 'dune_imperium_data.csv')
