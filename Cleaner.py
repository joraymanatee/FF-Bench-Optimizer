from Scrape_City.FootballGuys import scrape_footballguys_rankings
from Scrape_City.PFFScrapper import scrape_pff_rankings
from Scrape_City.FantasyFootballProsScrapper import scrape_ffpros_rankings
import pandas as pd

ffprosDict = scrape_ffpros_rankings()
#print(ffprosDict)

numbers = list(range(1, len(ffprosDict) + 1))

    
df_ffpros = pd.DataFrame(list(ffprosDict.keys()), columns=['Player'])
df_ffpros['Value'] = numbers

###################
footballguysDict = scrape_footballguys_rankings()


numbers2 = list(range(1, len(footballguysDict) + 1))

    
df_footballguys = pd.DataFrame(list(footballguysDict.keys()), columns=['Player'])
df_footballguys['Value'] = numbers2

###################
pffDict = scrape_pff_rankings()


numbers3 = list(range(1, len(pffDict) + 1))

    
df_pff = pd.DataFrame(list(pffDict.keys()), columns=['Player'])
df_pff['Value'] = numbers3

print(df_ffpros)
print(df_footballguys)
print(df_pff)



