from Compilier import compileAll
from Scrape_City.SleeperScrape import scrape_team_roster, scrape_sleeper_players_rostered

sorted_Dictionary = compileAll()

def availablePlayers_Sleeper():
    non_rostered_sorted_Dictionary = {}

    already_on_a_team = scrape_sleeper_players_rostered()

    for key in sorted_Dictionary:
        if key not in already_on_a_team:
            non_rostered_sorted_Dictionary[key] = '0'

    for key in non_rostered_sorted_Dictionary:
        non_rostered_sorted_Dictionary[key] = sorted_Dictionary[key]

    return non_rostered_sorted_Dictionary

def user_roster_rankings_Sleeper():
    user_roster_sorted_Dictionary = {}
    on_team = scrape_team_roster()

    for key in sorted_Dictionary:
        if key in on_team:
            user_roster_sorted_Dictionary[key] = sorted_Dictionary[key]

    return user_roster_sorted_Dictionary

if __name__ == "__main__":
    df = availablePlayers_Sleeper()
    dg = user_roster_rankings_Sleeper()
    print(df)
    print(dg)

