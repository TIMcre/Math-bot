from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="C:\\Users\\Timon\\geckodriver.exe")

driver.get("https://www.realmath.de/Neues/Klasse8/binome/binomevar03.php")

# box to show the answer
sbox = driver.find_element_by_css_selector(".hilfButton")
# box to check the answer
cbox = driver.find_element_by_css_selector(".pruefeButton")
# box to make a new question
gbox = driver.find_element_by_css_selector(".neuButton")

time.sleep(2)
gbox.click()



driver.quit