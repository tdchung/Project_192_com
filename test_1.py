import time
from selenium import webdriver
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

url = "https://hshop.vn/account/register"

user_name_xpath = "//div[@id='first_name']//input"
last_name_xpath = "//div[@id='last_name']//input"
email_xpath = "//div[@id='email']//input"
password_xpath = "//div[@id='password']//input"
submit = "//div[@class='action_bottom']//input"


def proxy_list():
    req_proxy = RequestProxy()
    proxies = req_proxy.get_proxy_list()
    return proxies

req_proxy = RequestProxy()
proxies = req_proxy.get_proxy_list()

# proxies = proxy_list()
for i in range(20,30):
    print("-------------- LOOP %d ---------------" %(i+1))
    
    PROXY = proxies[i].get_address()
    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,
        "proxyType":"MANUAL"
    }
    driver = webdriver.Chrome('D://Project//Python//Selenium//driver//chromedriver.exe')  # Optional argument, if not specified will search path.

    for j in range(10):
        try:
            driver.get(url)
            # time.sleep(5) # Let the user actually see something!

            print(driver.find_element_by_xpath(user_name_xpath).send_keys('Just %d' % (i*10+j)))
            print(driver.find_element_by_xpath(last_name_xpath).send_keys('Test'))
            print(driver.find_element_by_xpath(email_xpath).send_keys('Email%d@mail.mail' % (i*10+j)))
            print(driver.find_element_by_xpath(password_xpath).send_keys('12345678'))
            print(driver.find_element_by_xpath(submit).click())

            time.sleep(5) # Let the user actually see something!
        except:
            pass
        # driver.close()

    driver.quit()