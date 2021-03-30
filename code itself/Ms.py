import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print('Введите адрес получателя:')
mail = input()
print('Введите сообщение:')
text = input()

option = Options()
option.headless = True

browser = webdriver.Chrome(executable_path=r'C:\проги\питон\moduls\chromedriver.exe', options=option)
browser.get('https://account.mail.ru/')
print('Браузер успешно запустился.')
time.sleep(5)
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
time.sleep(17)

browser.get('https://e.mail.ru/compose/')
time.sleep(5)
print('Отправляем письмо...')

who = browser.find_element_by_xpath('//input[@style="width: 12px;"]')
who.send_keys(mail)
time.sleep(2)

message = browser.find_element_by_xpath('//div[@aria-label="false"]/div[1]')
message.send_keys(text)
time.sleep(2)

sender = browser.find_element_by_xpath('//span[@title="Отправить"]')
sender.click()
print('Письмо успешно отправлено!')
time.sleep(6)

browser.quit()
