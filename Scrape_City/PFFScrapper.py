from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_pff_rankings():

    driver = webdriver.Chrome()

    driver.get('https://www.pff.com/news/fantasy-football-rankings-2024-ppr-top-400')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, './/div[@class="g-table-wrapper"]/table/tbody/tr')))

    players_full = driver.find_elements(By.XPATH, './/div[@class="g-table-wrapper"]/table/tbody/tr')

    player_names = []
    player_types = []

    for row in players_full:
        name_element = row.find_element(By.XPATH, './td[3]').text
        type_element = row.find_element(By.XPATH, './td[5]').text
        player_names.append(name_element)
        player_types.append(type_element)
        
    driver.quit()  # Driver closer.

    totalDictionary = {}
    for key in player_names:
        for value in player_types:
            totalDictionary[key] = value
            player_types.remove(value)
            break

    totalDictionary.pop('Name')

    totalDictionaryReal = {}
    for key, value in totalDictionary.items():
        clean_key = key.replace(" Jr.", "").replace("Jr", "").replace(" Sr.", "").replace("Sr", "").replace("III", "").replace(" II", "")
        totalDictionaryReal[clean_key] = value
    return totalDictionaryReal

if __name__ == "__main__":
    df = scrape_pff_rankings()
    print(df)


    