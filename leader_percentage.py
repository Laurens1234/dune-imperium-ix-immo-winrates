import pandas as pd

# Load the CSV data into a DataFrame
df = pd.read_csv('dune_imperium_data.csv')

# Group the data by Leader and Starting Position and count the occurrences of each ending position
leader_starting_position_counts = df.groupby(['Leader', 'Starting Position'])['Ending Position'].value_counts().unstack(fill_value=0)

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

# Leader Statistics
leader_stats = leader_starting_position_stats_sorted.groupby('Leader')[['Win Rate', 'Total Games', 'Average Ending Position']].mean()
print("\nLeader Statistics:")
print(leader_stats)

# Game Balance Assessment - Example of analyzing win rates for each starting position
starting_position_win_rates = df.groupby('Starting Position')['Ending Position'].apply(lambda x: (x == 1).sum() / len(x) * 100)
print("\nGame Balance Assessment - Win Rates by Starting Position:")
print(starting_position_win_rates)

# Average Ending Position by Starting Position
average_ending_position_starting = df.groupby('Starting Position')['Ending Position'].mean()
print("\nAverage Ending Position by Starting Position:")
print(average_ending_position_starting)

# Leader Popularity Analysis
leader_popularity = df['Leader'].value_counts()
print("\nLeader Popularity Analysis:")
print(leader_popularity)
