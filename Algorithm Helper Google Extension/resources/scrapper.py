from selenium import webdriver
from selenium.webdriver.common.by import By

# Scrapes the description of the question on leetcode.com
def scrape_lc_website(website:str): 
    driver = webdriver.Chrome()
    driver.get(website)
    content = driver.find_element(By.CLASS_NAME, "elfjS")
    text = content.text
    driver.quit()
    
    return text