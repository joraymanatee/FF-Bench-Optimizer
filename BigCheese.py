from ImprovementSleeper import availablePlayers_sleeper, user_roster_rankings_sleeper
from ImprovementESPN import availablePlayers_ESPN, user_roster_rankings_ESPN
import os 


fantasy_platform = input('What platform do you use for Fantasy?')

if fantasy_platform == 'ESPN':
    waiver_players = availablePlayers_ESPN()
    current_roster = user_roster_rankings_ESPN()
elif fantasy_platform == 'Sleeper':
    waiver_players = availablePlayers_sleeper()
    current_roster = user_roster_rankings_sleeper()

os.system('clear')

for player in current_roster:
    if current_roster[player] < min(waiver_players.values()):
        pass
    else:
        first_key = next(iter(waiver_players))
        print('There is a better player available, get rid of ' + player + ' for ' + first_key + '.')
        del waiver_players[first_key]




                                    

