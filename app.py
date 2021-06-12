from copy import deepcopy
from constants import PLAYERS
from constants import TEAMS


players_copy = deepcopy(PLAYERS)
teams = [panthers = [], bandits = [], warriors = []]
#team_copy = TEAMS
#Teams
#panthers = []
#bandits = []
#warriors = []

print(players_copy)

# Experience: This should be saved as a boolean value (True or False)

for player in players_copy:  # loop through the copy
    if player["experience"] == "YES":  # if that player has experaince set to the string "Yes"
        player["experience"] = True    # change it to True
    elif player["experience"] == "NO":  # if that player has experaince set to the string "NO"
        player["experience"] = False    # change it to False

# Height: This should be saved as an integer.

for player in players_copy:
	player["height"] = int(player["height"][0:2])

# Create a balance_teams function:
	# Now that the player data has been cleaned, balance the players across the three teams: Panthers, Bandits and Warriors. Make sure the teams have the same number of total players on them when your team balancing function has finished.
	# HINT: To find out how many players should be on each team, divide the length of players by the number of teams. Ex: num_players_team = len(PLAYERS) / len(TEAMS)


def Balance_Teams():
	num_of_players = len(players_copy) / 3
	# Balance the players across the three teams: Panthers, Bandits and Warriors.
	for team in teams:
		for player in players_copy:
			team.append(player)


		















	
	# Console readability matters: When the menu or stats display to the console, it should display in a nice readable format. Use extra spaces or line breaks ('\n') to break up lines if needed. For example, '\nThis will start on a newline.'

	# Displaying the stats: When displaying the selected teams' stats to the screen you will want to include:
	# Team's name as a string
	# Total players on that team as an integer
	# The player names as strings separated by commas

print(players_copy)