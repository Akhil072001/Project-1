import time
from selenium import webdriver

print("start")
driver = webdriver.Firefox("./geckodriver")  # Optional argument, if not specified will search path.
print("webdriver")
driver.get('http://www.google.com/')
print("url")
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
print("search_box")
search_box.send_keys('ChromeDriver')
print("send_keys")
search_box.submit()
print("submit")
time.sleep(5) # Let the user actually see something!
driver.quit()
print("end")