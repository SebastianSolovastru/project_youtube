
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait




driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=fpUpVznI4Yc%22")

wait = WebDriverWait(driver, 20)

accept = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div.body.style-scope.ytd-consent-bump-v2-lightbox > div.eom-buttons.style-scope.ytd-consent-bump-v2-lightbox > div:nth-child(1) > ytd-button-renderer:nth-child(2) > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill")))
accept.click()
time.sleep(20)

users = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#owner-sub-count")))
for user in users:
    print(user.text)

users = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#dismissible")))
for user in users:
    print(user.text)

users = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#info > span:nth-child(1)")))
for user in users:
    print(user.text)
