from Compilier import compileAll
from Scrape_City.SleeperWaiversScraper import scrape_sleeper_waivers

sorted_Dictionary = compileAll()
#sorted_Dictionary = {'Christian McCaffrey': 0, 'CeeDee Lamb': 1}
non_rostered_sorted_Dictionary = {}

already_on_a_team = scrape_sleeper_waivers()

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

print(non_rostered_sorted_Dictionary)


