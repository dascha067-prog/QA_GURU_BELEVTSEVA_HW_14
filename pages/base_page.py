from selene import browser


class BasePage:
    def __init__(self):
        self.browser = browser

    def open(self, relative_url: str):
        self.browser.open(relative_url)
        return self
