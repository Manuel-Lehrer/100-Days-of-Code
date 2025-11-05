from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

#price = f"Price: {price_dollar}.{price_cents}"
#print(price)

# search_bar = driver.find_element(By.NAME, value="q").get_attribute("placeholder") # or .tagname to get html element
# print(search_bar)
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# docs = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a").text
# print(docs)
# another_link = driver.find_element(By.XPATH, value='//*[@id="container"]/li[4]/ul/li[13]/a')
# print(another_link.text)


#Creating a nested dict with the next 5 upcoming events

event_times = driver.find_elements(By.CSS_SELECTOR, value=" .event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=" .event-widget li a")

events = {i: {'time': event_times[i].text, 'name': event_names[i].text} for i in range(0, len(event_times))}


print(events)

driver.quit()
