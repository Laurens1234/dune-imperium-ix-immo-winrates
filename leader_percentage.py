import pandas as pd

# Load the CSV data into a DataFrame
df = pd.read_csv('dune_imperium_data.csv')

# Group the data by Leader and count the occurrences of each ending position
leader_counts = df.groupby('Leader')['Ending Position'].value_counts().unstack(fill_value=0)

# Calculate the total number of games played by each leader
leader_counts['Total Games'] = leader_counts.sum(axis=1)

# Calculate the win rate for each leader
leader_counts['Win Rate'] = (leader_counts[1] / leader_counts['Total Games']) * 100  # Convert to percentage

# Calculate the average ending position for each leader
average_ending_position = df.groupby('Leader')['Ending Position'].mean()

# Combine the win rate and total games with the average ending position
leader_stats = pd.concat([leader_counts[['Win Rate', 'Total Games']], average_ending_position.rename('Average Ending Position')], axis=1)

# Sort the results by win rate
leader_stats_sorted = leader_stats.sort_values(by='Win Rate', ascending=False)

# Calculate the total number of games played overall
total_games_overall = leader_counts['Total Games'].sum()

# Divide the total number of games by 4 to account for 4 entries per game
actual_games_played_overall = total_games_overall / 4

# Display the actual number of games played overall
print("\nActual number of games played overall: {}".format(actual_games_played_overall))

# Display the Leader Statistics
print("\nLeader Statistics:")
print(leader_stats_sorted)

# Group the data by Leader and Starting Position and count the occurrences of each ending position
leader_starting_position_counts = df.groupby(['Leader', 'Starting Position'])['Ending Position'].value_counts().unstack(fill_value=0)

# Reindex to ensure all starting positions (1 to 4) are included for each leader
leader_starting_position_counts = leader_starting_position_counts.reindex(columns=[1, 2, 3, 4], fill_value=0)

# Calculate the total number of games played by each leader and starting position combination
leader_starting_position_counts['Total Games'] = leader_starting_position_counts.sum(axis=1)

# Calculate the win rate for each leader and starting position combination
leader_starting_position_counts['Win Rate'] = (leader_starting_position_counts[1] / leader_starting_position_counts['Total Games']) * 100  # Convert to percentage

# Calculate the average ending position for each leader and starting position combination
average_ending_position_starting = df.groupby(['Leader', 'Starting Position'])['Ending Position'].mean()

# Combine the win rate and total games with the average ending position
leader_starting_position_stats = pd.concat([leader_starting_position_counts[['Win Rate', 'Total Games']], average_ending_position_starting.rename('Average Ending Position')], axis=1)

# Sort the results by win rate
leader_starting_position_stats_sorted = leader_starting_position_stats.sort_values(by='Win Rate', ascending=False)

# Display the Leader and Starting Position Statistics
print("\nLeader and Starting Position Statistics:")
print(leader_starting_position_stats_sorted)

# Print Leader Statistics based on Starting Position for each leader
print("\nLeader Statistics based on Starting Position:")
for starting_position in range(1, 5):
    print(f"\nPosition {starting_position}: Win Rate Average Ending Position Total Games")
    starting_position_data = leader_starting_position_stats_sorted.xs(starting_position, level='Starting Position')
    max_name_length = max(starting_position_data.index.map(len))  # Get the maximum length of leader names
    for leader, data in starting_position_data.iterrows():
        win_rate = data['Win Rate']
        avg_end_place = data['Average Ending Position']
        total_games = data['Total Games']
        print(f"{leader:{max_name_length}}:\t{win_rate:.2f}%\t{avg_end_place:.2f}\t{total_games}")

# Calculate the total average winrate and average ending position for each leader
total_avg_winrate = leader_stats_sorted['Win Rate'].mean()
total_avg_end_position = leader_stats_sorted['Average Ending Position'].mean()

# Display the total average winrate and average ending position for each leader
print("\nTotal Average Winrate and Average Ending Position for Each Leader:")

# Add a description of what's being printed for each leader
print("\nFor each leader, the following lines show: Win Rate / Average Ending Position / Total Games Played for each seat.")

# Iterate through each leader
for leader, data in leader_stats_sorted.iterrows():
    win_rate = data['Win Rate']
    avg_end_place = data['Average Ending Position']
    
    # Retrieve the win rate and average ending position for each seat for the current leader, sorted
    seat_stats = leader_starting_position_stats_sorted.loc[leader]
    sorted_seat_stats = seat_stats.sort_index()
    
    # Print the leader's overall statistics
    print(f"\n{leader}: Win Rate: {win_rate:.2f}%, Average Ending Position: {avg_end_place:.2f}")
    
    # Print each seat's win rate, average ending position, and games played on a separate line
    for seat, stats in sorted_seat_stats.iterrows():
        win_rate = stats['Win Rate']
        avg_end_position = stats['Average Ending Position']
        total_games = stats['Total Games']
        
        # Display win rate, average ending position, and games played
        print(f"Seat {seat}: {win_rate:.2f}% / {avg_end_position:.2f} / {total_games}")


    
    # Calculate the win rate for each starting position across all players
starting_position_counts = df.groupby('Starting Position')['Ending Position'].value_counts().unstack(fill_value=0)

# Calculate the total number of games played from each starting position
starting_position_counts['Total Games'] = starting_position_counts.sum(axis=1)

# Calculate win rates for each starting position across all players
starting_position_win_rates = (starting_position_counts[1] / starting_position_counts['Total Games']) * 100  # Convert to percentage

# Print the win rates for each starting position
print("\nWin Rates for Each Starting Position Across All Players:")
for position, win_rate in starting_position_win_rates.items():
    print(f"Starting Position {position}: {win_rate:.2f}%")

