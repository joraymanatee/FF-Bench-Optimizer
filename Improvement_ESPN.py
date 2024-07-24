from Compilier import compileAll
from Scrape_City.ESPNScrape import scrape_roster_espn, espn_on_waivers

sorted_Dictionary = compileAll()

def availablePlayersESPN():
    non_rostered_sorted_Dictionary = {}

    not_on_a_team = espn_on_waivers()

    for key in sorted_Dictionary:
        if key in not_on_a_team:
            non_rostered_sorted_Dictionary[key] = '0'

    for key in non_rostered_sorted_Dictionary:
        non_rostered_sorted_Dictionary[key] = sorted_Dictionary[key]

    return non_rostered_sorted_Dictionary

def user_roster_rankingsESPN():
    user_roster_sorted_Dictionary = {}
    on_team = scrape_roster_espn()

    for key in sorted_Dictionary:
        if key in on_team:
            user_roster_sorted_Dictionary[key] = sorted_Dictionary[key]

    return user_roster_sorted_Dictionary

if __name__ == "__main__":
    df = availablePlayersESPN()
    dg = user_roster_rankingsESPN()
    print(df)
    print(dg)

