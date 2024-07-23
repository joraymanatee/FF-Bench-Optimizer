from Scrape_City.SleeperScrape import availablePlayers, user_roster_rankings
import os 


fantasy_platform = input('What platform do you use for Fantasy?')
    

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




                                    

