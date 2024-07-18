from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_team_names():

    driver = webdriver.Chrome()
    #input_username = input('Whats your sleeper username?')
    input_username = 'jackbernie'
    #input_id = input('Whats sleeper league id?')
    input_id = 1088591425672929280

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

    team_roster = driver.find_elements(By.XPATH, './/div[@class="chakra-stack cha-1htld2l"][' + str(numbered_roster) + ']')

           
    driver.quit()
    return team_roster

if __name__ == "__main__":
    df = scrape_team_names()
    print(df)