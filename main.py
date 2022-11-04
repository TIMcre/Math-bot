from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from tqdm.auto import tqdm
import pandas as pd


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

print(f"[Debug] loading browser")
# inital setup
driver = webdriver.Firefox(service=Service("geckodriver.exe"))
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

print(f"[Debug] finished loading browser")
times = int(input(f"[Input] iterations: "))
try:
    for _ in tqdm(range(times)):
        task(driver, gbox, qbox, ibox, cbox)
except:
    print(f"[Error] invalid input")
print(f"[Debug] finished")