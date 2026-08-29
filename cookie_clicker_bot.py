from selenium import webdriver
from selenium.webdriver.common.by import By
import time

edge_options=webdriver.EdgeOptions()
edge_options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=edge_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(5)
english=driver.find_element(By.XPATH,value='//*[@id="langSelect-EN"]')
english.click()
first_recorded_time=time.time()
last_recorded_time=time.time()
interval=5.0
while 1:
    driver.find_element(By.ID,value="bigCookie").click()

    current_time=time.time()
    if current_time-last_recorded_time>=interval:
        try:
            available_game_items=driver.find_elements(By.CSS_SELECTOR,value=".product.unlocked.enabled")
            prices=[]
            for i in range(len(available_game_items)):
                prices.append(int(driver.find_element(By.ID,value=f"productPrice{i}").text.replace(",","")))
            most_expensive_item=prices.index(max(prices))
            print(available_game_items[most_expensive_item].get_attribute("id"))
            available_game_items[most_expensive_item].click()
            prices=[]

        except Exception as e:
            print(e)
        last_recorded_time+=interval
        if current_time-first_recorded_time>=5*60:
            print(f"cookies/second : {float(driver.execute_script("return document.getElementById('cookiesPerSecond').innerText;").split(":")[1])}")
            break
