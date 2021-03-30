from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome() # Terminal 에서 폴더 경로 맞춰줘야 함
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&authuser=0&ogbl") # 구글 이미지 검색으로 접속
elem = driver.find_element_by_name("q")


keyword = "김세정" # 검색어 입력


elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 3 

# Get scroll height 
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgurl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
        urllib.request.urlretrieve(imgurl, keyword + str(count) + ".jpg")
        print(keyword + str(count) + " 저장")
        count += 1
    
    except:
        pass
print("다운로드 끝")
# driver.close()
