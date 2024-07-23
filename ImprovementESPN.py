from Compilier import compileAll
from Scrape_City.ESPNScrape import scrape_roster_espn
from Scrape_City.ESPNScrape import scrape_espn_waivers

sorted_Dictionary = compileAll()

def availablePlayers_ESPN():

    non_rostered_sorted_Array = scrape_espn_waivers()
    fixed_DST = []

    for player in non_rostered_sorted_Array:
        fixed_player = player.replace('D/ST', 'DST')
        fixed_DST.append(fixed_player)


    non_rostered_sorted_Dictionary = {}

    for name in fixed_DST:
        non_rostered_sorted_Dictionary[name] = '0'

    for key in non_rostered_sorted_Dictionary:
        non_rostered_sorted_Dictionary[key] = sorted_Dictionary[key]

    return non_rostered_sorted_Dictionary

def user_roster_rankings_ESPN():
    user_roster_sorted_Dictionary = {}
    on_team = scrape_roster_espn()

    on_team_fixed_DST = []
    for player in on_team:
        string_player = str(player)
        if string_player[:string_player.index]
        fixed_player = player.replace('D/ST', 'DST')
        
        on_team_fixed_DST.append(fixed_player)

    for name in on_team_fixed_DST:
        user_roster_sorted_Dictionary[name] = '0'

    for key in sorted_Dictionary:
        if key in on_team:
            user_roster_sorted_Dictionary[key] = sorted_Dictionary[key]

    return user_roster_sorted_Dictionary

if __name__ == "__main__":
    df = availablePlayers_ESPN()
    dg = user_roster_rankings_ESPN()
    print(df)
    print(dg)

