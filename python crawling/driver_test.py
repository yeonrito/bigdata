from selenium import webdriver
query = input("입력 : ")

driver = webdriver.Chrome("chromedriver.exe")


driver.get("https://www.naver.com/")
driver.implicitly_wait(3)

xpath = '//*[@id="query"]'

driver.find_element_by_xpath(xpath).send_keys(query)
button_xpath = '//*[@id="search_btn"]'
driver.find_element_by_xpath(button_xpath).click()

html = driver.page_source

driver.close()
print(html)