Dune imperium code for data analysis from hidden assets.
If you find any errors contact krompl on discord.

main.py turns discord bot output into csv style data. (need to make sure regex is correct when adding new data for new player names)

leader_percentage.py analysis the data.

dataset.txt only contains data for up to game 967. This is season 7 games with sandstorm.

dataset_no_sandstorm_s7.txt only contains games from 968 until 1182 (s7 no sandsorm)

Resubmits up to this game have been manually removed from dataset.txt and ns  until 1182


How to use:
create a txt file or add to a txt file games in exactly this format:
Dune Imperium Bot
BOT
 — 04/01/2024 10:15 PM
Submit Accepted [Game ID: 10]
1st:@Freek :Ilban: Position: 4 52.4
2nd:@Yung Savage :Rhombur: Position: 3 11.6
3rd:@justinbyun :Beast: Position: 2 -20.4
4th:@M1X :Baron: Position: 1 -43.6

edit this line in main.py to the txt file name:
# Sample input file name
input_filename = 'dataset_full_s7.txt'

edit this line to the csv file name:

# Write the parsed data to CSV
write_to_csv(parsed_data, 'dune_imperium_data_full_s7.csv')

python main.py

make sure data is being read correctly and update regex if needed (this is only needed if people in the .txt have unknown symbols like emojis in their name if this is not done the code breaks)

run python leader_percentage.py

most other programs to get leader/player stats work in a similar way