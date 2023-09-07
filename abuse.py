from storage import *
from settings import *
from driver import *
import time
import random

# Create a list with keys whose value is not zero
def create_non_empty_list(count):
    return [key for key, value in count.items() if value > 0]

def get_random_key(faculties, valid_faculties):
    random_faculty = random.choice(valid_faculties)
    faculties[random_faculty] -= 1
    return random_faculty

def fill_form(driver, faculty):
    # Click faculty
    driver.find_element(By.XPATH, f"//*[contains(text(), '{faculty}')]").click()
    time.sleep(0.2)

    # Click distant format (yes)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]").click()
    time.sleep(0.2)

    # Click Saturday work (no)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]").click()
    time.sleep(0.2)

    # Click evening work (no)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]").click()
    time.sleep(0.2)

    # Click benefits for students (random - yes or no)
    driver.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[{random.choice([1, 2])}]").click()
    time.sleep(0.2)

    # Click submit
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span").click()

    print("The form is filled out")

def abuse(url):
    try:
        faculties_storage = MapStorage(MAP_PATH)
        faculties = faculties_storage.Read()
        valid_faculties = create_non_empty_list(faculties)
        while (len(valid_faculties) > 0):
            driver = set_up_driver(DRIVER_PATH)
            driver.get(URL)
            start_time = random.uniform(0, PERIOD)
            time.sleep(start_time * 60)
            random_faculty = get_random_key(faculties, valid_faculties)
            fill_form(driver, random_faculty)
            time.sleep((PERIOD - start_time) * 60)
            driver.close()


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    