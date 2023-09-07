from driver import *
from settings import * 
from abuse import *

if __name__ == '__main__':
    driver = set_up_driver("./chromedriver/chromedriver")
    abuse(driver, URL)