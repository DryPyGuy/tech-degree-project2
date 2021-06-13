from copy import deepcopy
from constants import PLAYERS
from constants import TEAMS


players_copy = deepcopy(PLAYERS)

panthers = []

bandits = []

warriors = []

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


# def Balance_Teams(team):
# 	# Balance the players across the three teams: Panthers, Bandits and Warriors.
# 	while times <= num_of_players:
# 		for player in players_copy:
# 			team.pop(player)
# 			times += 1

num_of_players = len(players_copy) / len(TEAMS)

for player in players_copy:
	if len(panthers) == len(bandits):
		panthers.append(players_copy)
	elif len(warriors) < len(panthers)

# def balance_teams(players):
#     #the team balancing function
#     for player in players_copy:
#         if player['experience'] == True:
#             if len(team_panthers) == len(team_bandits):
#                 team_panthers.append(player)
#             elif len(team_warriors) < len(team_panthers):
#                 team_warriors.append(player)
#             else:
#                 team_bandits.append(player)
#     for player in players:
#         if player['experience'] == False:
#             if len(team_panthers) == len(team_bandits):
#                 team_panthers.append(player)
#             elif len(team_warriors) < len(team_panthers):
#                 team_warriors.append(player)
#             else:
#                 team_bandits.append(player)



		















	
	# Console readability matters: When the menu or stats display to the console, it should display in a nice readable format. Use extra spaces or line breaks ('\n') to break up lines if needed. For example, '\nThis will start on a newline.'

	# Displaying the stats: When displaying the selected teams' stats to the screen you will want to include:
	# Team's name as a string
	# Total players on that team as an integer
	# The player names as strings separated by commas

print(players_copy)