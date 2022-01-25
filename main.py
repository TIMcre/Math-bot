from selenium import webdriver
import time
# inital setup
driver = webdriver.Firefox(executable_path="C:\\Users\\Timon\\geckodriver.exe")
driver.get("https://www.realmath.de/Neues/Klasse8/binome/binomevar03.php")


# box to show the answer
sbox = driver.find_element_by_css_selector(".hilfButton")
# box to check the answer
cbox = driver.find_element_by_css_selector(".pruefeButton")
# box to make a new question
gbox = driver.find_element_by_css_selector(".neuButton")
# input field for answer
ibox = driver.find_element_by_css_selector("#idxt1")
# checkbox for alowing input
abox = driver.find_element_by_xpath("/html/body/form/div[2]/div/div/div/div[3]/center/table/tbody/tr/td[1]/input")

abox.click()
gbox.click()
ibox.send_keys("1111")
cbox.click()

driver.quit