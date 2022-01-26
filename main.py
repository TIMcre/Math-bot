from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# inital setup
driver = webdriver.Firefox(executable_path="C:\\Users\\Timon\\geckodriver.exe")
driver.get("https://www.realmath.de/Neues/Klasse8/binome/binomevar03.php")

def get_answer(question):
    f = csv.reader(open("data.csv", encoding='utf-8'))
    for row in f:
        if question == row[0]:
            return row[1]




print(get_answer("(x + 5)⋅(x - 5)"))


print("done")



# box to check the answer
cbox = driver.find_element(By.CSS_SELECTOR,".pruefeButton")
# input field for answer
ibox = driver.find_element(By.CSS_SELECTOR,"#idxt1")
# checkbox for alowing input
abox = driver.find_element(By.XPATH,"/html/body/form/div[2]/div/div/div/div[3]/center/table/tbody/tr/td[1]/input")
