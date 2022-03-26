from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm.auto import tqdm
import pandas as pd
# inital setup
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.realmath.de/Neues/Klasse8/binome/binomevar03.php")
df = pd.read_csv("data.csv", encoding="utf8")

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
    return question, answer

def add_data(data, df):
    df.loc[len(df.index)] = data    

for _ in tqdm(range(500)):
    add_data(get_data(driver, sbox, gbox), df)
    

driver.quit

df = df.drop_duplicates()
df.to_csv("data.csv", encoding='utf8', index= False)