from espn_api.football import League
from datetime import datetime

user_team_name = input('What is your team name?')
league_id = input('What is your league ID?')

league = League(league_id=league_id, year=datetime.now().year)

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

    user_roster = []


    print(team.roster)
    for player in team.roster:
        string_player = str(player)
        string_player[end - 7: end - 3].replace('D/ST', 'DST')
        print(string_player)
        end = len(str(player))
        user_roster.append(string_player[7: end - 1])

    return user_roster

def scrape_espn_waivers():
    free_agents = []
    for player in league.free_agents():
        string_player = str(player)
        free_agents.append(string_player[7: string_player.index(',')])
    return free_agents

if __name__ == "__main__":
    df = scrape_roster_espn()
    dg = scrape_espn_waivers()
    print(df)
    print(dg)