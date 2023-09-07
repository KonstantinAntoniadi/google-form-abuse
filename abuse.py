from storage import *
from settings import *
from driver import *
import time
import random

# Create a list with keys whose value is not zero
def create_non_empty_list(count):
    return [key for key, value in count.items() if value != 0]

def get_random_key(keys):
    random_key = random.choice(keys)
    # TODO: add logic for reducing the value
    return random_key

def fill_form(driver, faculty):
    # Click faculty
    driver.find_element(By.XPATH, f"//*[contains(text(), '{faculty}')]").click()

    # Click distant format (yes)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]").click()

    # Click Saturday work (no)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]").click()

    # Click evening work (no)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]").click()

    # Click benefits for students (random - yes or no)
    driver.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[{random.choice([1, 2])}]").click()


def abuse(driver, url):
    try:
        driver.get(URL)
        map_storage = MapStorage(MAP_PATH)
        count = map_storage.Read()
        valid_keys = create_non_empty_list(count)
        random_key = get_random_key(valid_keys)
        print(random_key)
        fill_form(driver, random_key)
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    