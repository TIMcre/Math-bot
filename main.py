from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
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

abox.click()
gbox.click()
sbox.click()

# output box
obox = driver.find_element(By.CSS_SELECTOR,"#MathOutput > font:nth-child(1)")
# question field
qbox = driver.find_element(By.CSS_SELECTOR,"#idz1")




time.sleep(1)


print(obox.text)


print(qbox.get_attribute("value"))

values = []

values.append((obox.text,qbox.get_attribute("value")))




driver.quit