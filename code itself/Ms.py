import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# print('Введите адрес получателя:')
# mail = input()
# print('Введите сообщение:')
# text = input()

browser = webdriver.Edge(executable_path=r'C:\проги\питон\moduls\msedgedriver.exe')
browser.get('https://account.mail.ru/')
time.sleep(5)

login = browser.find_element_by_class_name('input-1-1-72')
login.send_keys('yasha.b0lda@inbox.ru')
time.sleep(3)

submit1 = browser.find_element_by_tag_name('button')
submit1.click()
time.sleep(2)

password = browser.find_element_by_class_name('withIcon-1-1-73')
password.send_keys('ooERpoOTr/34')
time.sleep(2)

submit2 = browser.find_element_by_tag_name('button')
submit2.click()
time.sleep(20)

browser.get('https://e.mail.ru/compose/')
time.sleep(5)

who = browser.find_element_by_class_name('container--H9L5q.size_s_compressed--2c-eV')
who.send_keys('qn0n1m0us@mail.ru')
time.sleep(2)

message = browser.find_element_by_xpath('//div[@aria-label="false"]/div[1]')
message.send_keys('hello')
time.sleep(2)

sender = browser.find_element_by_xpath('//span[@title="Отправить"]')
sender.click()
time.sleep(6)

browser.quit()
