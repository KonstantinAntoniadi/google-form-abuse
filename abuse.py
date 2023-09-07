from storage import *
from settings import *
import time
import random

# Create a list with keys whose value is not zero
def create_non_empty_list(count):
    return [key for key, value in count.items() if value != 0]

def get_random_key(keys):
    random_key = random.choice(keys)
    # TODO: add logic for reducing the value
    return random_key

def abuse(driver, url):
    try:
        driver.get(URL)
        map_storage = MapStorage(MAP_PATH)
        count = map_storage.Read()
        valid_keys = create_non_empty_list(count)
        random_key = get_random_key(valid_keys)
        print(random_key)
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    