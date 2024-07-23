from Compilier import compileAll
from Scrape_City.SleeperScrape import scrape_team_roster
from Scrape_City.SleeperScrape import scrape_sleeper_players_rostered

sorted_Dictionary = compileAll()

def availablePlayers():
    non_rostered_sorted_Dictionary = {}

    already_on_a_team = scrape_sleeper_players_rostered()

    for key in sorted_Dictionary:
        if key not in already_on_a_team:
            non_rostered_sorted_Dictionary[key] = '0'

    #Temporary fix.
    non_rostered_sorted_Dictionary.pop('Travis Etienne Jr.')
    non_rostered_sorted_Dictionary.pop('Marvin Harrison Jr.')
    non_rostered_sorted_Dictionary.pop('Deebo Samuel Sr.')
    non_rostered_sorted_Dictionary.pop('Brian Thomas Jr.')

    for key in non_rostered_sorted_Dictionary:
        non_rostered_sorted_Dictionary[key] = sorted_Dictionary[key]

    return non_rostered_sorted_Dictionary

def user_roster_rankings():
    user_roster_sorted_Dictionary = {}
    on_team = scrape_team_roster()

    for key in sorted_Dictionary:
        if key in on_team:
            user_roster_sorted_Dictionary[key] = sorted_Dictionary[key]

    return user_roster_sorted_Dictionary

if __name__ == "__main__":
    df = availablePlayers()
    dg = user_roster_rankings()
    print(df)
    print(dg)

