from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_team_roster():

    driver = webdriver.Chrome()
    input_username = input('Whats your sleeper username?')
    input_id = input('Whats sleeper league id?')

    driver.get('https://www.sleepercompanion.com/league/' + str(input_id) + '/rosters')
    EC.presence_of_element_located((By.XPATH, './/div[@class="cha-vxgrp0"]'))
    potential_team_names = driver.find_elements(By.XPATH, './/h2[@class="chakra-heading cha-tmg4cn"]')
    
    team_names_number = {}

    for name in potential_team_names:
        team_names_number[name.text] = '0'
    
    j = 1
    for key in team_names_number:
        team_names_number[key] = j
        j+=1

    numbered_roster = team_names_number[input_username]

    team_roster_list = []
    team_roster = driver.find_elements(By.XPATH, './/div[@class="cha-cn82tz"][' + str(numbered_roster) + ']//div[@class="chakra-stack cha-n21gh5"]//div[@class="cha-70qvj9"]/p[@class="chakra-text cha-yfehv3"]')
    for row in team_roster:
        players_text = row.text
        team_roster_list.append(players_text)
    
    abbrev_to_name = {}

    with open('nfl_teams.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                abbrev_to_name[row[2]] = row[1]

    for part in team_roster_list:
        if part in abbrev_to_name.keys():
            team_roster_list.remove(part)
            team_roster_list.append(abbrev_to_name[part] + ' DST')
           
    driver.quit()
    
    return team_roster_list

if __name__ == "__main__":
    df = scrape_team_roster()
    print(df)