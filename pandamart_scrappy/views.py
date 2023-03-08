import time
import random
from rest_framework import viewsets, status
from rest_framework.response import Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent


# Create your views here.

# API SUMMARY
# /////////////////////////////////////////////////////////////////////////////
# @DESC            GET DATA LIST FROM PANDAMART URLS
# @ROUTE           POST: http://{server_ip:port}/pandamart/pandamart_scrappy/
# @ACCESS          Authentication NOT REQUIRED
# @PAYLOAD         { "keyword": "Dettol" }
# /////////////////////////////////////////////////////////////////////////////

class PandamartScrapperView(viewsets.ModelViewSet):
    # serializer_class = PandamartScrapperSerializer

    def create(self, request, *args, **kwargs):
        try:
            urls = ["https://www.foodpanda.com.bd/darkstore/w2lx/pandamart-gulshan-w2lx",
                    "https://www.foodpanda.com.bd/darkstore/h9jp/pandamart-mirpur"]

            # Initializing Fake User agent & Setting a random user agent
            ua = UserAgent()
            user_agent = ua.random

            options = webdriver.ChromeOptions()

            # setting options to start the browser maximized so that all the products are loaded
            options.add_argument("start-maximized")

            # Exclude the collection of enable-automation switches and Turn-off userAutomationExtension as a part of preventing antibot detection
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            # Adding argument to disable the AutomationControlled flag as a part of preventing antibot detection
            options.add_argument("--disable-blink-features=AutomationControlled")

            # Adding the generated random user agent to browser
            options.add_argument(f'user-agent={user_agent}')

            # Setting the driver with options and setting custom window size of the browser
            driver = webdriver.Chrome(options=options)
            driver.set_window_size(1915, 1070)

            def kill_popup(element):
                """ method to close the pop up modal about address
                :arg
                    element (str): The popup module element.

                :functions
                    The method then finds the close button element withing the pop up element
                    Then the button is clicked

                :returns None"""

                pop_up = element
                pop_up_close_btn = pop_up[0].find_element(By.CLASS_NAME, "groceries-modal-close-button")
                pop_up_close_btn.click()

            all_item_details = []  # list initiated for storing all item and their details

            random_number = random.randint(1, 3)
            random_number2 = random.randint(2, 3)

            for url_count, url in enumerate(urls):
                driver.get(url)  # requesting a url

                time.sleep(random_number)  # pausing the program to mimic a human activity

                # checking for existence of address pop up modal & calling the kill_popup method to close it
                if len(driver.find_elements(By.CLASS_NAME, 'no-address-modal')) > 0:
                    kill_popup(driver.find_elements(By.CLASS_NAME, 'no-address-modal'))

                search_field = driver.find_element(By.XPATH,
                                                   '//div[@class="darkstore-container"]//input[@data-testid="search-input"]')  # finding the search field
                search_field.send_keys(request.data["keyword"])  # entering the keyword in the search field
                time.sleep(0.75)  # pausing the program to mimic a human activity
                search_field.send_keys(Keys.RETURN)  # pressing enter to search

                time.sleep(random_number)  # pausing the program to mimic a human activity

                if len(driver.find_elements(By.CLASS_NAME, 'no-address-modal')) > 0:  # checking for existence of address pop up modal
                    kill_popup(driver.find_elements(By.CLASS_NAME, 'no-address-modal'))  # calling the kill_popup method to close it

                try:
                    all_items = wait(driver, 2).until(EC.visibility_of_all_elements_located(
                        (By.XPATH,
                         '//div[@class="darkstore-container"]/ul/li')))  # if 0 items are found, throws exception
                except:
                    continue  # continue to the next url or end the loop if 0 items are found

                for item in all_items:
                    count = len(item.find_elements(By.CLASS_NAME, 'product-card-price-before-discount'))  # checking if product has a discounted price
                    price_count = len(item.find_elements(By.CLASS_NAME, 'product-card-price'))  # checking if product has a price to state its availability

                    if count == 0:
                        price = item.find_element(By.CLASS_NAME, 'product-card-price').text  # if the discount price is not available, set the price from the price element
                    else:
                        price = item.find_element(By.CLASS_NAME, 'product-card-price-before-discount').text  # if the discount price is available, set the price from the discounted price element

                    # setting the response data for each item in a dict
                    item_details = {
                        'title': item.find_element(By.CLASS_NAME, 'product-card-name').text,
                        'url': item.find_element(By.CLASS_NAME, 'product-card-nav-wrapper').get_attribute('href'),
                        'darkStore':
                            item.find_element(By.CLASS_NAME, 'product-card-nav-wrapper').get_attribute('href').split(
                                '/')[5].split(
                                '-')[
                                1].capitalize(),
                        'price': price,
                        'priceAfterDiscount': item.find_element(By.CLASS_NAME, 'product-card-price').text,
                        'stockStatus ': 'IN STOCK' if price_count > 0 else 'OUT OF STOCK'
                    }

                    all_item_details.append(item_details)

                time.sleep(2.5)  # pausing the program to mimic a human activity
                if url_count != len(urls)-1:
                    time.sleep(random_number2)  # pausing the program to mimic a human activity

            driver.quit()  # quitting the driver

            response = {
                "statusCode": status.HTTP_200_OK,
                "data": all_item_details,
                "totalCount": len(all_item_details)

            }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {
                "message": "Error! Couldn't Fetch Data!",
                "statusCode": status.HTTP_400_BAD_REQUEST,
                "error": str(e)
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


