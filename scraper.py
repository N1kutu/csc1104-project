from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import Select
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get('https://www.cpubenchmark.net/CPU_mega_page.html')
driver.find_element(By.CLASS_NAME, 'css-47sehv').click()
select = Select(driver.find_element(By.NAME, 'cputable_length'))
select.select_by_visible_text('All')
time.sleep(1)

driver.find_element(By.XPATH, ".//*[contains(text(), 'Columns')]").click()
driver.find_element(By.XPATH, ".//*[contains(text(), 'Auto')]").click()
driver.find_element(By.XPATH, ".//*[contains(text(), 'Num. Sockets')]").click()
driver.find_element(By.XPATH, ".//*[contains(text(), 'Cores')]").click()
driver.find_element(By.XPATH, ".//*[contains(text(), 'Price')]").click()
driver.find_element(By.XPATH, ".//*[contains(text(), 'CPU Value')]").click()
driver.find_element(By.XPATH, ".//*[contains(text(), 'Thread Value')]").click()
driver.find_element(By.XPATH, ".//*[contains(text(), 'Power Perf.')]").click()
driver.find_element(By.XPATH, ".//*[contains(text(), 'Test Date')]").click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

names = soup.find_all('td', class_='sorting_1')
scores = soup.find_all('td', attrs={'class':None})
scores = scores[2:]
cpu_name = []
n_sockets = []
cores = []
price = []
cpu_mark = []
cpu_value = []
thread_mark = []
thread_value = []
tdp_w = []
power_perf = []
test_date = []
socket = []
category = []
num_scores_per_cpu = 12

for i, link in enumerate(names):
    cpu_name.append(link.text.strip())
    score_values = scores[i * num_scores_per_cpu:(i + 1) * num_scores_per_cpu]

    if len(score_values) == num_scores_per_cpu:
        n_sockets.append(score_values[0].get_text(strip=True))
        cores.append(score_values[1].get_text(strip=True))
        price.append(score_values[2].get_text(strip=True))
        cpu_mark.append(score_values[3].get_text(strip=True))
        cpu_value.append(score_values[4].get_text(strip=True))
        thread_mark.append(score_values[5].get_text(strip=True))
        thread_value.append(score_values[6].get_text(strip=True))
        tdp_w.append(score_values[7].get_text(strip=True))
        power_perf.append(score_values[8].get_text(strip=True))
        test_date.append(score_values[9].get_text(strip=True))
        socket.append(score_values[10].get_text(strip=True))
        category.append(score_values[11].get_text(strip=True))

df = pd.DataFrame({
    'CPU Name': cpu_name,
    'No. Sockets': n_sockets,
    'Cores': cores,
    'Price': price,
    'CPU Mark': cpu_mark,
    'CPU Value': cpu_value,
    'Thread Mark': thread_mark,
    'Thread Value': thread_value,
    'TDP (W)': tdp_w,
    'Power Performance': power_perf,
    'Test Date': test_date,
    'Socket': socket,
    'Category': category,
})
df.index += 1

df.to_csv('Project.csv')
driver.quit()