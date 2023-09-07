from storage import *
from settings import *
import time

def abuse(driver, url):
    try:
        driver.get(URL)
        map_storage = MapStorage(MAP_PATH)
        count = map_storage.Read()
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    