from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_sleeper_waivers():

    driver = webdriver.Chrome()
    input_id = input('Whats sleeper league id?')

    driver.get('https://www.sleepercompanion.com/league/' + str(input_id) + '/rosters')
    EC.presence_of_element_located((By.XPATH, './/div[@class="cha-vxgrp0"]'))
    roster_elements = driver.find_elements(By.XPATH, './/div[@class="cha-70qvj9"]')

    rostered_players = []

    for row in roster_elements:
        name_element = row.find_element(By.XPATH, './/p[@class="chakra-text cha-yfehv3"]').text
        rostered_players.append(name_element)

    abbrev_to_name = {}

    with open('nfl_teams.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            abbrev_to_name[row[2]] = row[1]

    for part in rostered_players:
        if part in abbrev_to_name.keys():
            rostered_players.remove(part)
            rostered_players.append(abbrev_to_name[part] + ' DST')
           
    driver.quit()
    return rostered_players

if __name__ == "__main__":
    df = scrape_sleeper_waivers()
    print(df)