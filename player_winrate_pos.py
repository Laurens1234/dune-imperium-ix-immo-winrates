import pandas as pd

# Load the CSV file into a DataFrame
file_path = "dune_imperium_data.csv"  # Specify the correct file path
df = pd.read_csv(file_path)

# Specify the player name you want to calculate the win rate for
player_name = "@Yung Savage"

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
    print(f"starting position {starting_position}: {win_rate:.2f}% win rate (games played: {total_games})")
