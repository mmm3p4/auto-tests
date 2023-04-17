from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



browser=webdriver.Chrome()
browser.get('http://www.vlsu.ru//')
def news():
        button_news = browser.find_element(By.CSS_SELECTOR, value='a[title="«Человек и война: учителя и педагоги в годы Великой Отечественной войны»"]')
        button_news.click()
        try:
         assert "«Человек и война: учителя и педагоги в годы Великой Отечественной войны»" in browser.page_source
         print('Тест прошел удачно')
        except Exception as err:
           print('Тест прошел неудачно')

def search():
    search = browser.find_element(By.NAME, value="text")
    search.send_keys("испи")
    search.send_keys(Keys. RETURN)
    time.sleep(5)
    try:
     assert "Нашёлся 1 ответ" in browser.page_source
     print('Тест прошел удачно')
    except Exception as err:
        print('Тест прошел неудачно')

def language():
   original_window = browser.current_window_handle
   button_language = browser.find_element(By.LINK_TEXT, 'EN')
   button_language.click()
   time.sleep(5)
   for window_handle in browser.window_handles:
        if window_handle != original_window:
            browser.switch_to.window(window_handle)
            break
   try:
       assert "GENERAL INFORMATION" in browser.page_source
       print('Тест прошел удачно')
   except Exception as err:
       print('Тест прошел неудачно')
news()