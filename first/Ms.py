import time
from selenium import webdriver

print('Введите адрес получателя:')
mail = input()
print('Введите сообщение:')
text = input()

browser = webdriver.Edge(executable_path=r'C:\проги\питон\moduls\msedgedriver.exe')
browser.get('https://account.mail.ru/')
time.sleep(35)
browser.quit()
