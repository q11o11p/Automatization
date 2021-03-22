import time
from selenium import webdriver

# print('Введите адрес получателя:')
# mail = input()
# print('Введите сообщение:')
# text = input()

browser = webdriver.Edge(executable_path=r'C:\проги\питон\moduls\msedgedriver.exe')
browser.get('https://account.mail.ru/')
time.sleep(10)

login = browser.find_element_by_class_name('input-1-1-72')
login.send_keys('yasha.b0lda@inbox.ru')
time.sleep(5)

submit1 = browser.find_element_by_tag_name('button')
submit1.click()
time.sleep(10)

password = browser.find_element_by_class_name('withIcon-1-1-73')
password.send_keys('ooERpoOTr/34')
time.sleep(5)

submit2 = browser.find_element_by_tag_name('button')
submit2.click()
time.sleep(20)

browser.quit()
