from Scrape_City.FootballGuys import scrape_footballguys_rankings
from Scrape_City.PFFScrapper import scrape_pff_rankings
from Scrape_City.FantasyFootballProsScrapper import scrape_ffpros_rankings
from tabulate import tabulate
import pandas as pd

def compileAll():
    ffprosDict = scrape_ffpros_rankings()

    i = 0
    for key in ffprosDict:
        ffprosDict[key] = i
        i+=1

    footballguysDict = scrape_footballguys_rankings()
    
    j = 0
    for key in footballguysDict:
        footballguysDict[key] = j
        j+=1

    pffDict = scrape_pff_rankings()

    k = 0
    for key in pffDict:
        pffDict[key] = k
        k+=1

    CummulationDict = {}
    for key in ffprosDict:
        try:
            CummulationDict[key] = (int(ffprosDict[key]) + int(footballguysDict[key]) + int(pffDict[key]))/3
        except:
            pass

    sorted_dict = dict(sorted(CummulationDict.items(), key=lambda x: x[1]))
 
    l = 0
    for key in sorted_dict:
        sorted_dict[key] = l
        l+=1
    
    return sorted_dict

if __name__ == "__main__":
    cData = compileAll()
    df_players = pd.DataFrame(cData.keys(), columns=['Player'])
    print(tabulate(df_players, headers="firstrow", tablefmt='fancy_grid'))
