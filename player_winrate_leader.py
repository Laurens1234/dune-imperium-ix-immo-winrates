import argparse

import pandas as pd


def calculate_win_rates(file_path, player_name):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Ensure the player names are cleaned by stripping leading/trailing whitespaces
    df['Player'] = df['Player'].str.strip()
    player_name = player_name.strip()

    # Filter the DataFrame to include only the rows for the specified player
    player_data = df[df['Player'] == player_name]

    # Calculate the total games played by the player
    total_games_played = len(player_data)

    # Print the player's name and total games played
    print(player_name)
    print(f"Total games played: {total_games_played}")

    # Group data by leader
    grouped_data_by_leader = player_data.groupby('Leader')

    # Iterate over each leader group and calculate the win rate and total games played
    for leader, group in grouped_data_by_leader:
        # Calculate the number of games where the player ended in position 1 (won the game)
        wins = sum(group['Ending Position'] == 1)

        # Calculate the total number of games played with this leader
        total_games = len(group)

        # Calculate win rate as a percentage
        win_rate = (wins / total_games) * 100 if total_games > 0 else 0

        # Print the win rate and the total games played for each leader
        print(f"{leader}: {win_rate:.2f}% win rate (games played: {total_games})")


if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Calculate win rates by leader for a specified player.')

    # Add an argument for the player name
    parser.add_argument('player_name', type=str, help='The name of the player (e.g., "@BenitoMax")')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Specify the CSV file path
    file_path = 'dune_imperium_data_full_s7.csv'  # Specify the correct file path

    # Calculate win rates using the specified player name
    calculate_win_rates(file_path, args.player_name)
