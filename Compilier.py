from Scrape_City.FootballGuys import scrape_footballguys_rankings
from Scrape_City.PFFScrapper import scrape_pff_rankings
from Scrape_City.FantasyFootballProsScrapper import scrape_ffpros_rankings
import pandas as pd
from tabulate import tabulate

ffprosDict = scrape_ffpros_rankings()
#print(ffprosDict)
ffprosDictTiny = {
 'Christian McCaffrey': 'RB1', 
 'CeeDee Lamb': 'WR1', 
 'Tyreek Hill': 'WR2', 
 'Amon-Ra St. Brown': 'WR3',
 'Justin Jefferson': 'WR4', 
 "Ja'Marr Chase": 'WR5'
}

i = 0
for key in ffprosDict:
    ffprosDict[key] = i
    i+=1
#print(ffprosDict)


###################
footballguysDict = scrape_footballguys_rankings()
footballguysDictTiny = {
 'Christian McCaffrey': 'RB1', 
 'CeeDee Lamb': 'WR1', 
 'Tyreek Hill': 'WR2', 
 'Justin Jefferson': 'WR3', 
 "Ja'Marr Chase": 'WR4', 
 'Amon-Ra St. Brown': 'WR5',
}

j = 0
for key in footballguysDict:
    footballguysDict[key] = j
    j+=1
#print(footballguysDict)

###################
pffDict = scrape_pff_rankings()
pffDictTiny = {
    'Christian McCaffrey': 'RB1', 
    'CeeDee Lamb': 'WR1', 
    'Tyreek Hill': 'WR2', 
    "Ja'Marr Chase": 'WR3', 
    'Justin Jefferson': 'WR4', 
    'Amon-Ra St. Brown': 'WR5',
}

k = 0
for key in pffDict:
    pffDict[key] = k
    k+=1
#print(pffDict)




CummulationDict = {}
for key in ffprosDict:
    try:
        CummulationDict[key] = (int(ffprosDict[key]) + int(footballguysDict[key]) + int(pffDict[key]))/3
    except:
        print("Error")

#print(CummulationDict)

sorted_dict = dict(sorted(CummulationDict.items(), key=lambda x: x[1]))

l = 0
for key in sorted_dict:
    sorted_dict[key] = l
    l+=1
#print(sorted_dict)

df_players = pd.DataFrame(sorted_dict.keys(), columns=['Player'])

print(tabulate(df_players, headers="firstrow", tablefmt='fancy_grid'))
