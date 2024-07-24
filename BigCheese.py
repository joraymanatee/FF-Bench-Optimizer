import os  

fantasy_platform = input('What platform do you use for Fantasy?')

if fantasy_platform == 'Sleeper':
    from Improvement_Sleeper import availablePlayers_Sleeper, user_roster_rankings_Sleeper
    waiver_players = availablePlayers_Sleeper()
    current_roster = user_roster_rankings_Sleeper()
elif fantasy_platform == 'ESPN':
    from Improvement_ESPN import availablePlayersESPN, user_roster_rankingsESPN
    waiver_players = availablePlayersESPN()
    current_roster = user_roster_rankingsESPN()
    

os.system('clear')

for player in current_roster:
    if current_roster[player] < min(waiver_players.values()):
        pass
    else:
        first_key = next(iter(waiver_players))
        print('There is a better player available, get rid of ' + player + ' for ' + first_key + '.')
        del waiver_players[first_key]




                                    

