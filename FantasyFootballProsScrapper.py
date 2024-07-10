from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_ffpros_rankings():

    driver = webdriver.Chrome()

    driver.get('https://www.fantasypros.com/nfl/rankings/ppr-cheatsheets.php')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//tr[@class="player-row"]')))

    players_full = driver.find_elements(By.XPATH, '//tr[@class="player-row"]')

    player_names = []
    player_types = []

    for row in players_full:
        name_element = row.find_element(By.XPATH, './/div[@class="player-cell player-cell__td"]').text
        type_element = row.find_element(By.XPATH, './td[4]').text
        player_names.append(name_element)
        player_types.append(type_element)
        

    #print(player_names)
    #print(player_types)

    #input('breaker')
    # Close Driver
    driver.quit()

    totalDictionary = {}
    for key in player_names:
        for value in player_types:
            totalDictionary[key] = value
            player_types.remove(value)
            break

    return totalDictionary

if __name__ == "__main__":
    df = scrape_ffpros_rankings()
    print(df)
    




