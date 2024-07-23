from ImprovementSleeper import availablePlayers, user_roster_rankings
import os 


fantasy_platform = input('What platform do you use for Fantasy?')

if fantasy_platform == 'ESPN':
    waiver_players = 
    current_roster = 
elif fantasy_platform == 'Sleeper':
    waiver_players = 
    current_roster = 
    

waiver_players = availablePlayers()
current_roster = user_roster_rankings()

os.system('clear')

for player in current_roster:
    if current_roster[player] < min(waiver_players.values()):
        pass
    else:
        first_key = next(iter(waiver_players))
        print('There is a better player available, get rid of ' + player + ' for ' + first_key + '.')
        del waiver_players[first_key]




                                    

