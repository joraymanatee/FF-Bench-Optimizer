from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_footballguys_rankings():

    driver = webdriver.Chrome()
    driver.get('https://www.footballguys.com/rankings')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="component-body"]/table/tbody')))

    rows = driver.find_elements(By.XPATH, '//div[@class="component-body"]/table/tbody/tr')

    player_names = []
    player_types = []

    for row in rows:
        try:
            name_element = row.find_element(By.XPATH, './/td[@class="name player-col sticky-col"]/a').text
            type_element = row.find_element(By.XPATH, './/td[4]').text
            player_names.append(name_element)
            player_types.append(type_element)
        except Exception as e:
            pass

    driver.quit()

    totalDictionary = {}
    for i in range(len(player_names)):
        totalDictionary[player_names[i]] = player_types[i]

    totalDictionaryReal = {}
    for key, value in totalDictionary.items():
        clean_key = key.replace(" Jr.", "").replace("Jr", "").replace(" Sr.", "").replace("Sr", "").replace("III", "").replace(" II", "")
        totalDictionaryReal[clean_key] = value
    return totalDictionaryReal


if __name__ == "__main__":
    df = scrape_footballguys_rankings()
    print(df)