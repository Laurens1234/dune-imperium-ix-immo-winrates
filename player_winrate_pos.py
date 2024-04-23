import argparse

import pandas as pd


def calculate_win_rates_by_starting_position(file_path, player_name):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Ensure the player names are cleaned by stripping leading/trailing whitespaces
    df['Player'] = df['Player'].str.strip()
    player_name = player_name.strip()

    # Filter the DataFrame to include only the rows for the specified player
    player_data = df[df['Player'] == player_name]

    # Group data by starting position
    grouped_data = player_data.groupby('Starting Position')

    # Print the player's name
    print(player_name)

    # Iterate over each starting position group and calculate the win rate and total games
    for starting_position, group in grouped_data:
        # Calculate the number of games where the player ended in position 1 (won the game)
        wins = sum(group['Ending Position'] == 1)
        
        # Calculate the total number of games played from this starting position
        total_games = len(group)
        
        # Calculate win rate as a percentage
        win_rate = (wins / total_games) * 100 if total_games > 0 else 0
        
        # Print the win rate and the total games played for the starting position
        print(f"Starting position {starting_position}: {win_rate:.2f}% win rate (games played: {total_games})")

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Calculate win rates by starting position for a specified player.')

    # Add an argument for the player name
    parser.add_argument('player_name', type=str, help='The name of the player (e.g., "@Yung Savage")')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Specify the CSV file path
    file_path = 'dune_imperium_data.csv'  # Specify the correct file path

    # Calculate win rates using the specified player name
    calculate_win_rates_by_starting_position(file_path, args.player_name)
