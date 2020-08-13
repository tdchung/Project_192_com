import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.192.com"

xpath_input_name = "//input[@id='peopleBusinesses_name']"
xpath_input_location = "//input[@id='where_location']"
xpath_search_button = "//input[@id='searchBtn']"

xpath_no_results = "//h3[contains(text(), 'Sorry, your search for')]"
xpath_list_response = "//li[@class='ont-people-premium-result-item']"

# name info
xpath_info_name = ".//div[@class='test-name']"
xpath_info_age = ".//*[@class='age-guide-value']"
xpath_info_director = ".//div[contains(@class, 'director')]"
xpath_info_address = (
    ".//div[contains(@class, 'results-address')]//*[contains(@class, 'test-address')]"
)


# main
driver = webdriver.Chrome(
    "D://Project//Python//Selenium//driver//chromedriver.exe"
)  # Optional argument, if not specified will search path.


def get_info_element_text(element, element_xpath):
    info_text = ""
    try:
        info_text = element.find_element_by_xpath(element_xpath).text
    except Exception as e:
        # print(e)
        info_text = "N/A"
    return info_text


# define data to test
list_data = [
    ["Ben Davies", "E1"],
    ["Ben Davies", "E1 2JH"],
]

try:
    driver.get(url)
    for j in range(len(list_data)):
        input_name = driver.find_element_by_xpath(xpath_input_name)
        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)
        input_name.send_keys(list_data[j][0])

        input_location = driver.find_element_by_xpath(xpath_input_location)
        input_location.send_keys(Keys.CONTROL + "a")
        input_location.send_keys(Keys.DELETE)
        input_location.send_keys(list_data[j][1])

        print(driver.find_element_by_xpath(xpath_search_button).click())
        time.sleep(2)

        is_result = False
        try:
            no_results_found = driver.find_element_by_xpath(xpath_no_results)
        except Exception as e:
            # print(e)
            is_result = True

        if is_result:
            list_results = driver.find_elements_by_xpath(xpath_list_response)
            print(
                "Total result found for %s, %s: %d"
                % (list_data[j][0], list_data[j][1], len(list_results))
            )

            i = 0
            for result in list_results:
                i = i + 1
                info_name = get_info_element_text(result, xpath_info_name)
                info_age = get_info_element_text(result, xpath_info_age)
                info_director = get_info_element_text(result, xpath_info_director)
                info_address = get_info_element_text(result, xpath_info_address)

                print(
                    "INFO: %d === Name: %s  === Age: %s  === DIR: %s  === addr: %s"
                    % (i, info_name, info_age, info_director, info_address)
                )
        else:
            print("NO result found for %s, %s" % (list_data[j][0], list_data[j][1]))


except Exception as e:
    print(e)
    pass
# driver.close()

driver.quit()
