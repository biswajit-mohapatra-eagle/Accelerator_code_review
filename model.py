import re
import time
import pandas as pd

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Put your desired URL here.
url = ""

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(url)
