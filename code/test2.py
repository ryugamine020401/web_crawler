# seleium網頁操作

from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#-------------------------selemium版本4.x-----------------
def make_webdriver() -> Chrome:
    s = Service(ChromeDriverManager().install())    #一個瀏覽器
    #driver = webdriver.Chrome(service=s, options=create_options())
                                                    #無論版本 chrome_options 都是被棄用的...
    driver = webdriver.Chrome(service=s, options=create_options())   #瀏覽器的驅動
    print(s)
    print(driver)
    return driver
#---------------------------------------------------------


def create_options() -> Options:        # 設定一些瀏覽器的參數...
    options = Options()         #一個object的物件，裡面可以有很多參數，這邊只用到add_argument...
    # 每加入一個argument會在 options.arguments <-這個陣列添加一個，類似 陣列.append()
    #options.add_argument("--headless")         #讓瀏覽器隱藏
    options.add_argument("--start-maximized")   #最大化瀏覽器
    #print(options.arguments)
    return options

if __name__ == '__main__':
    url = "https://www.facebook.com/"
    chrome = make_webdriver()   #chrome就是操作瀏覽器的基本物件
    chrome.get(url=url)     # 讓瀏覽器前往該網址
    print(chrome)

    k = chrome.find_element(By.NAME, "email")
    k.send_keys("example@gmail.com")
    k = chrome.find_element(By.NAME, "pass")
    k.send_keys("your passward...")
    k.submit()
    chrome.maximize_window()