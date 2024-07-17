from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_sleeper_waivers():

    driver = webdriver.Chrome()

    #link = input('https://sleeper.com/leagues/1088591425672929280/players')
    input_id = input('Whats sleeper league id?')

    driver.get('https://www.sleepercompanion.com/league/' + str(input_id) + '/rosters')

    EC.presence_of_element_located((By.XPATH, './/div[@class="cha-70qvj9"]'))
    roster_elements = driver.find_elements(By.XPATH, './/div[@class="cha-70qvj9"]')

    rostered_players = []

    players_on_roster = driver.find_elements(By.XPATH, './/p[@class="chakra-text cha-yfehv3"]')
    for element in players_on_roster:
        players_on_rosterd = players_on_roster.text
        rostered_players.append(players_on_rosterd)

    input('breaker')

    print(rostered_players)
    #print(player_types)

    #input('breaker')
    # Close Driver
    driver.quit()


if __name__ == "__main__":
    df = scrape_sleeper_waivers()
    print(df)