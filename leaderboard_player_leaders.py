import pandas as pd

# Description of what the script does
print("This script calculates win rates for each leader based on the games played by each player.")
print("It creates a leaderboard for each leader, showing the top 5 players ranked by win rate.")
print("Only players who have played at least 5 games with a leader are included in the leaderboard.")
print("\n")

# Load the CSV file into a DataFrame
file_path = "dune_imperium_data.csv"  # Specify the correct file path
df = pd.read_csv(file_path)

# Group data by leader and player
grouped_data = df.groupby(['Leader', 'Player'])

# Calculate win rates for each leader-player combination
# Calculate win rates and total games played
def calculate_win_rate(group):
    total_games = len(group)
    wins = sum(group['Ending Position'] == 1)
    win_rate = (wins / total_games) * 100 if total_games > 0 else 0
    return pd.Series({'Win Rate': win_rate, 'Total Games': total_games})

# Apply the function to calculate win rates
win_rates = grouped_data.apply(calculate_win_rate)

# Reshape the result to a DataFrame
win_rates_df = win_rates.reset_index()

# Group the win rates by leader
grouped_by_leader = win_rates_df.groupby('Leader')

# Print the top 5 players for each leader
for leader, data in grouped_by_leader:
    # Filter data to include only players who have played at least 5 games with the leader
    filtered_data = data[data['Total Games'] >= 5]
    
    # Sort data by win rate in descending order and get the top 5 players
    top_players = filtered_data.sort_values(by='Win Rate', ascending=False).head(5)
    
    # Print the leader's name
    print(f"Leaderboard for Leader: {leader}")
    
    # Print the top 5 players for the leader
    for rank, (_, row) in enumerate(top_players.iterrows(), start=1):
        player_name = row['Player']
        win_rate = row['Win Rate']
        total_games = row['Total Games']
        print(f"{rank}. {player_name} {win_rate:.2f}% ({total_games})")
    print("\n")  # Add a newline for better readability between each leaderboard
