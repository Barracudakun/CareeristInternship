from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


# this Base class is serving basic attributes for every single page inherited from Page class

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def get_text(self, *locator):
        return self.find_element(*locator).text

    def open_url(self, url):
        self.driver.get(url)

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_for_form_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))
