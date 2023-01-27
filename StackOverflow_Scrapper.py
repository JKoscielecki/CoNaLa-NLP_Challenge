# import os
from selenium import webdriver
# os.environ['PATH'] += r"C:\SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/questions/tagged/python?tab=Votes")