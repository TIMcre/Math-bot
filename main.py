from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from tqdm.auto import tqdm
import pandas as pd
import re

times = 50

# inital setup
options = Options()
options.binary_location= "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
driver = webdriver.Firefox(executable_path="geckodriver", options=options)

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

    if re.match(".*\+.*\+.*", q):
        print(f" | {q} | 1. Binomische Formel | 1. Type |")
    if re.match(".*-.*\+.*", q):
        print(f" | {q} | 2. Binomische Formel | 1. Type |")
    if re.match("^x.*-[^x]* ",q):
        print(f" | {q} | 3. Binomische Formel | 1. Type |")

    a = get_answer(q)
    ibox.send_keys(a)
    cbox.click()


for _ in tqdm(range(times)):
    task(driver, gbox, qbox, ibox, cbox)
