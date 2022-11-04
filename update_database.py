from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from tqdm.auto import tqdm
import pandas as pd


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
    return question, answer

def add_data(data, df):
    df.loc[len(df.index)] = data    
    
print(f"[Debug] loading browser")  
# inital setup
driver = webdriver.Firefox(service=Service("geckodriver.exe"))
driver.get("https://www.realmath.de/Neues/Klasse8/binome/binomevar03.php")
df = pd.read_csv("data.csv", encoding="utf8")

# box to show the answer
sbox = driver.find_element(By.CSS_SELECTOR,".hilfButton")
# box to make a new question
gbox = driver.find_element(By.CSS_SELECTOR,".neuButton")

print(f"[Debug] finished loading browser")
print(f"[Debug] gathering data")
try:
    for _ in tqdm(range(500)):
        add_data(get_data(driver, sbox, gbox), df)    
except:
    print(f"[Error] invalid input")

driver.quit
print(f"[Debug] processing new data")
df = df.drop_duplicates()
df.to_csv("data.csv", encoding='utf8', index= False)
print(f"[Debug] finished")
