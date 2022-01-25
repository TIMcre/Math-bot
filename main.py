from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
# inital setup
driver = webdriver.Firefox(executable_path="C:\\Users\\Timon\\geckodriver.exe")
driver.wait = WebDriverWait(driver, 5)


driver.get("https://www.realmath.de/Neues/Klasse8/binome/binomevar03.php")


# box to show the answer
sbox = driver.find_element(By.CSS_SELECTOR,".hilfButton")
# box to check the answer
cbox = driver.find_element(By.CSS_SELECTOR,".pruefeButton")
# box to make a new question
gbox = driver.find_element(By.CSS_SELECTOR,".neuButton")
# input field for answer
ibox = driver.find_element(By.CSS_SELECTOR,"#idxt1")
# checkbox for alowing input
abox = driver.find_element(By.XPATH,"/html/body/form/div[2]/div/div/div/div[3]/center/table/tbody/tr/td[1]/input")


def get_data(driver, sbox, gbox):
    # generate new question and answer
    gbox.click()
    sbox.click()
    # question field
    qbox = driver.find_element(By.CSS_SELECTOR,"#idz1")
    # output box
    obox = driver.find_element(By.CSS_SELECTOR,"#MathOutput > font:nth-child(1)")    
    # get the data
    question = qbox.get_attribute("value")
    answer = obox.text
    # return the data
    return (question, answer)

print(get_data(driver, sbox, gbox))

driver.quit
