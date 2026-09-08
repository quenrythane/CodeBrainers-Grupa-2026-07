from selenium import webdriver

driver = webdriver.Chrome()
URL = "http://127.0.0.1:8000"
driver.get(URL)

print(driver.title)
input("Wciśnij ENTER, aby zamknąć przeglądarkę")
