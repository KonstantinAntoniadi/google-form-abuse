from driver import *
from settings import * 
import time

if __name__ == '__main__':
    driver = set_up_driver("./chromedriver/chromedriver")
    try:
        driver.get(URL)
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()