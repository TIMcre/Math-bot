from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
times = int(input("how often "))

# inital setup
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.realmath.de/Neues/Klasse8/binome/binomevar03.php")
# checkbox for alowing input
abox = driver.find_element(By.XPATH,"/html/body/form/div[2]/div/div/div/div[3]/center/table/tbody/tr/td[1]/input")
abox.click()
# input field for answer
ibox = driver.find_element(By.CSS_SELECTOR,"#idxt1")
# box to check the answer
cbox = driver.find_element(By.CSS_SELECTOR,".pruefeButton")
# box to make a new question
gbox = driver.find_element(By.CSS_SELECTOR,".neuButton")
# question field
qbox = driver.find_element(By.CSS_SELECTOR,"#idz1")

def get_answer(question):
    df = pd.read_csv("data.csv", encoding='utf8')
    ans = df[df["question"] == question]
    ans = ans.squeeze()
    ans = ans["answer"]
    return ans
    
def get_question(driver, gbox, qbox):
    gbox.click()
    # question field
    qbox = driver.find_element(By.CSS_SELECTOR,"#idz1")
    question = qbox.get_attribute("value")
    return question

def task(driver, gbox, qbox, ibox, cbox):
    q = get_question(driver, gbox, qbox)
    a = get_answer(q)
    ibox.send_keys(a)
    cbox.click()

for _ in range(times):
    task(driver, gbox, qbox, ibox, cbox)

driver.quit()
