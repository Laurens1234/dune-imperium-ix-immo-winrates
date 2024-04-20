import pandas as pd

# Load the CSV file into a DataFrame
file_path = "dune_imperium_data.csv"  # Specify the correct file path
df = pd.read_csv(file_path)

# Specify the player name you want to calculate the win rates for
player_name = "@Yung Savage"

# Ensure the player names are cleaned by stripping leading/trailing whitespaces
df['Player'] = df['Player'].str.strip()
player_name = player_name.strip()

# Filter the DataFrame to include only the rows for the specified player
player_data = df[df['Player'] == player_name]

# Group data by leader
grouped_data_by_leader = player_data.groupby('Leader')

# Print the player's name
print(player_name)

# Iterate over each leader group and calculate the win rate and total games played
for leader, group in grouped_data_by_leader:
    # Calculate the number of games where the player ended in position 1 (won the game)
    wins = sum(group['Ending Position'] == 1)
    
    # Calculate the total number of games played with this leader
    total_games = len(group)
    
    # Calculate win rate as a percentage
    win_rate = (wins / total_games) * 100 if total_games > 0 else 0
    
    # Print the win rate and the total games played for each leader
    print(f"Leader {leader}: {win_rate:.2f}% win rate (games played: {total_games})")
