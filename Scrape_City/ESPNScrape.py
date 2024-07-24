from espn_api.football import League
from datetime import datetime
import csv

user_team_name = input('What is your team name?')
league_id = input('What is your league ID?')

league = League(league_id=league_id, year=datetime.now().year)


def create_defense_Dictionary():
    defenseDictionary = {}
    with open('nfl_teams.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            team_column = row[1]
            team_name = row[1].split(' ')
            defenseDictionary[team_name[-1] + ' D/ST'] = row[1] + ' DST'
    return defenseDictionary

def scrape_roster_espn():

    team_names = [] 
    for team in league.teams:
        end = len(str(team))
        string_team = str(team)
        team_names.append(string_team[5: end - 1])

    #print(team_names)
    idx = 0
    for idx_r,team_name in enumerate(team_names):
        if user_team_name==team_name:
            idx = idx_r
    team = league.teams[idx]

    players = team.roster

    players_on_roster = []
    for name in players:
        players_on_roster.append(str(name)[7:len(str(name))-1])
    
    defenseDictionary = create_defense_Dictionary()

    for name in players_on_roster:
        if name in defenseDictionary.keys():
            players_on_roster.remove(name)
            players_on_roster.append(defenseDictionary[name])
    
    return players_on_roster

def espn_on_waivers():

    defense_Dictionary_Two = create_defense_Dictionary()

    free_agents = []
    for player in league.free_agents():
        string_player = str(player)
        if string_player[7: string_player.index(',')] not in defense_Dictionary_Two.keys():
                free_agents.append(string_player[7: string_player.index(',')])
        else:
                free_agents.append(defense_Dictionary_Two[string_player[7: string_player.index(',')]])

    return free_agents

  


    

if __name__ == "__main__":
    df = scrape_roster_espn()
    dg = espn_on_waivers()
    print(df)
    print(dg)