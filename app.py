
if __name__ == "__main__":

	import constants.py

	clean_data(PLAYERS)

	players_new_collection = []

	def clean_data(name, guardians, experience, height):
		# clean the player data without changing the original data
		# Data to be cleaned: Height: This should be saved as an integer. Experience: This should be saved as a boolean value (True or False)
		
		# save it to a new collection - build a new collection with what you have learned up to this point.
		
	# Create a balance_teams function:
		# Now that the player data has been cleaned, balance the players across the three teams: Panthers, Bandits and Warriors. Make sure the teams have the same number of total players on them when your team balancing function has finished.
		# HINT: To find out how many players should be on each team, divide the length of players by the number of teams. Ex: num_players_team = len(PLAYERS) / len(TEAMS)

	# Console readability matters: When the menu or stats display to the console, it should display in a nice readable format. Use extra spaces or line breaks ('\n') to break up lines if needed. For example, '\nThis will start on a newline.'

	# Displaying the stats: When displaying the selected teams' stats to the screen you will want to include:
	# Team's name as a string
	# Total players on that team as an integer
	# The player names as strings separated by commas