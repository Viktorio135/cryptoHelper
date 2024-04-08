import time

from selenium import webdriver
from selenium.webdriver.common.by import By







def tw_grapth15(bir, sym):

    url = f'https://ru.tradingview.com/chart/?symbol={bir}%3A{sym}'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options) 
    
    driver.get(url=url)
    driver.implicitly_wait(10)
    #time.sleep(3)
    m = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[4]'
    )
    m.click()
    time.sleep(.1)
    m2 = driver.find_element(
        By.XPATH, '/html/body/div[8]/div/span/div[1]/div/div/div/div[12]/div/span[1]'
    )
    m2.click()
    time.sleep(.1)
    full_screen = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[16]/div/button')
    full_screen.click()
    #time.sleep(3)

    driver.save_screenshot('photo/tw.png')

def tw_grapth1h(bir, sym):

    url = f'https://ru.tradingview.com/chart/?symbol={bir}%3A{sym}'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options) 
    
    driver.get(url=url)
    driver.implicitly_wait(10)
    #time.sleep(3)
    m = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[4]'
    )
    m.click()
    time.sleep(.1)
    m2 = driver.find_element(
        By.XPATH, '/html/body/div[8]/div/span/div[1]/div/div/div/div[17]/div/span[1]'
    )
    m2.click()
    time.sleep(.1)
    full_screen = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[16]/div/button')
    full_screen.click()
    #time.sleep(3)

    driver.save_screenshot('photo/tw.png')


def tw_grapth4h(bir, sym):

    url = f'https://ru.tradingview.com/chart/?symbol={bir}%3A{sym}'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options) 
    
    driver.get(url=url)
    driver.implicitly_wait(10)
    #time.sleep(3)
    m = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[4]'
    )
    m.click()
    time.sleep(.1)
    m2 = driver.find_element(
        By.XPATH, '/html/body/div[8]/div/span/div[1]/div/div/div/div[20]/div/span[1]'
    )
    m2.click()
    time.sleep(.1)
    full_screen = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[16]/div/button')
    full_screen.click()
    #time.sleep(3)

    driver.save_screenshot('photo/tw.png')


def tw_grapth1d(bir, sym):

    url = f'https://ru.tradingview.com/chart/?symbol={bir}%3A{sym}'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options) 
    
    driver.get(url=url)
    driver.implicitly_wait(10)
    #time.sleep(3)
    m = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[4]'
    )
    m.click()
    time.sleep(.1)
    m2 = driver.find_element(
        By.XPATH, '/html/body/div[8]/div/span/div[1]/div/div/div/div[23]/div/span[1]'
    )
    m2.click()
    time.sleep(.2)
    full_screen = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[16]/div/button')
    full_screen.click()
    time.sleep(.3)

    driver.save_screenshot('photo/tw.png')





def bubbles():


    url = 'https://cryptobubbles.net/'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    
    driver.get(url=url)
    driver.implicitly_wait(10)
    time.sleep(10)
    driver.save_screenshot('photo/bubbles.png')
    driver.close()
    

    url = f'https://ru.tradingview.com/chart/?symbol=FX%3ASPX500'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options) 
    
    driver.get(url=url)
    driver.implicitly_wait(10)
    #time.sleep(3)
    m = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[4]'
    )
    m.click()
    time.sleep(.1)
    m2 = driver.find_element(
        By.XPATH, '/html/body/div[8]/div/span/div[1]/div/div/div/div[13]/div'
    )
    m2.click()
    time.sleep(.2)
    full_screen = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[16]/div/button')
    full_screen.click()
    time.sleep(.3)

    driver.save_screenshot('photo/spx.png')

    driver.close()


    time.sleep(120)

    bubbles()


    


