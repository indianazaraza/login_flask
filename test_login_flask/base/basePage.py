class BasePage:
    """Class that initializes the pages classes"""
    def __init__(self, driver) -> None:
        self.driver = driver

    def send_to(self, locator: tuple, word: str) -> None:
        """Send a given word to a given locator """
        self.driver.find_element(*locator).send_keys(word)

    def click(self, locator: tuple) -> None:
        """Clicks on a given locator"""
        self.driver.find_element(*locator).click()

    def is_displayed(self, locator: tuple) -> bool:
        """Returns if an element is displayed given a locator"""
        return self.driver.find_element(*locator).is_displayed()

    def title_web_page(self) -> str:
        """Returns the title of the current web page"""
        return self.driver.title
