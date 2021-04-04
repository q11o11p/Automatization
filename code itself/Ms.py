import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

browser = webdriver.Chrome(executable_path=r'C:\проги\питон\moduls\chromedriver.exe', chrome_options=options)
browser.get('https://account.mail.ru/')
for i in range(36, 0, -1):
    print(f'\rБраузер запускается...{float(i)}', end='', flush=True)
    time.sleep(1)
print('\nБраузер успешно запустился. Начинается авторизация...')

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
for i in range(36, 0, -1):
    print(f'\rЗаходим в аккаунт...{float(i)}', end='', flush=True)
    time.sleep(1)

browser.get('https://e.mail.ru/compose/')
for i in range(16, 0, -1):
    print(f'\rЗагружаем форму для отправки письма...{float(i)}', end='', flush=True)
    time.sleep(1)
print('\nОтправляем письмо...')

who = browser.find_element_by_xpath('//input[@style="width: 12px;"]')
who.send_keys(sys.argv[1])
print('Вводим имя...')
time.sleep(5)

message = browser.find_element_by_xpath('//div[@role="textbox"]/div[1]')
message.send_keys(' '.join(sys.argv[2:]))
print('И сообщение...')
time.sleep(2)

sender = browser.find_element_by_xpath('//span[@title="Отправить"]')
sender.click()
print('Всё! Письмо успешно отправлено!')
time.sleep(4)

browser.quit()
