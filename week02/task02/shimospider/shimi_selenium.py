from selenium import webdriver
import time

def scrape_shimo():
    browser = webdriver.Chrome()
    browser.get("https://shimo.im/")
    #查找登录按钮
    loginButton = browser.find_element_by_xpath("/html/body/div[1]/div[1]/header/nav/div[3]/a[2]/button")
    time.sleep(5)
    if(loginButton):
        loginButton.click()
    else:
        print("未发现登录按钮")
        browser.close()

    #查找用户名和密码输入框，xpath目前都是采取绝对路径，在实际项目中采用相对路径
    username_xpath='/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input'
    usernameButton = browser.find_element_by_xpath(username_xpath)
    usernameButton.send_keys('xqdd2004@163.com')
    time.sleep(2)
    passwd_xpath= '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input'
    passwdButton = browser.find_element_by_xpath(passwd_xpath)
    #输入密码，密码屏蔽
    passwdButton.send_keys('password123')

    time.sleep(5)
    #立即登录按钮
    loginButton2_xpath='/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button'
    loginButton2 = browser.find_element_by_xpath(loginButton2_xpath).click()    
    #
    time.sleep(10)
    browser.close()


scrape_shimo()



