from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage:
    class BasePage:
        def __init__(self, driver):
            self.driver = driver

        def find_element(self, *locator):
            return self.driver.find_element(*locator)

        def click(self, *locator):
            self.driver.find_element(*locator).click()

        def input_text(self, text, *locator):
            e = self.driver.find_element(*locator)
            e.clear()
            e.send_keys(text)

        def open(self, url):
            self.driver.get(url)

        def get_title(self):
            return self.driver.title

        def get_url(self):
            return self.driver.current_url

        def hover(self, *locator):
            element = self.find_element(*locator)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()

        def wait_element(self, *locator):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            except TimeoutException:
                print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
                self.driver.quit()
