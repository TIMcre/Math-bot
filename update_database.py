from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
# inital setup
driver = webdriver.Firefox(executable_path="C:\\Users\\Timon\\geckodriver.exe")
driver.get("https://www.realmath.de/Neues/Klasse8/binome/binomevar03.php")

# box to show the answer
sbox = driver.find_element(By.CSS_SELECTOR,".hilfButton")
# box to make a new question
gbox = driver.find_element(By.CSS_SELECTOR,".neuButton")

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

def write_data(data):
    # open the csv file
    f = open("data.csv","a",newline = "", encoding='utf-8')
    # create the writer
    writer = csv.writer(f)
    # write the data
    writer.writerow(data)
    # close the csv file
    f.close()

for i in range(500):
    write_data(get_data(driver, sbox, gbox))
    print(i)

driver.quit

f = open("data.csv","r", encoding='utf-8').readlines()
fs = set(f)

for line in fs:
    f.write(line)

