import allure
from selenium.webdriver.common.by import By


class BooksPage:
    URL = "https://demoqa.com/books"

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу книг")
    def open(self):
        self.driver.get(self.URL)
        return self

    @allure.step("Ввести в поиск текст: {text}")
    def search(self, text: str):
        search_input = self.driver.find_element(By.ID, "searchBox")
        search_input.clear()
        search_input.send_keys(text)
        return self

    @allure.step("Получить список найденных книг")
    def get_results(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        return [row.text for row in rows if row.text.strip()]

    @allure.step("Проверить, что книга '{title}' присутствует в результатах")
    def should_have_book(self, title: str):
        results = self.get_results()
        assert any(title in r for r in results), f"Книга '{title}' не найдена"
        return self

    @allure.step("Проверить, что результатов нет")
    def should_have_no_results(self):
        results = self.get_results()
        assert len(results) == 0, f"Ожидалось 0 результатов, найдено: {len(results)}"
        return self
