import time
import sys
from selenium import webdriver

browser = webdriver.Edge(executable_path=r'C:\проги\питон\moduls\msedgedriver.exe')
browser.get('https://account.mail.ru/')
print('Браузер успешно запустился.')
time.sleep(10)
print('Начинается авторизация...')

login = browser.find_element_by_xpath('//input[@name="username"]')
login.send_keys('yasha.b0lda@inbox.ru')
time.sleep(2)

submit1 = browser.find_element_by_tag_name('button')
submit1.click()
time.sleep(2)

password = browser.find_element_by_class_name('withIcon-1-1-73')
password.send_keys('ooERpoOTr/34')
time.sleep(2)
print('Авторизация завершена.')

submit2 = browser.find_element_by_tag_name('button')
submit2.click()
print('Заходим в аккаунт...')
time.sleep(20)

browser.get('https://e.mail.ru/compose/')
time.sleep(5)
print('Отправляем письмо...')

who = browser.find_element_by_xpath('//input[@style="width: 12px;"]')
who.send_keys(sys.argv[1])
time.sleep(2)

message = browser.find_element_by_xpath('//div[@role="textbox"]/div[1]')
message.send_keys(' '.join(sys.argv[2:]))
time.sleep(2)

sender = browser.find_element_by_xpath('//span[@title="Отправить"]')
sender.click()
print('Письмо успешно отправлено!')
time.sleep(6)

browser.quit()
