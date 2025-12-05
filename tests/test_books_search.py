import allure
from pages.books_page import BooksPage


@allure.feature("Поиск книг")
class TestBooksSearch:

    @allure.story("Открытие страницы")
    def test_open_books(self, setup_browser):
        page = BooksPage(setup_browser)
        page.open()

        assert "books" in setup_browser.current_url.lower()

    @allure.story("Поиск по точному названию")
    def test_search_full_title(self, setup_browser):
        page = BooksPage(setup_browser).open()
        page.search("Git Pocket Guide").should_have_book("Git Pocket Guide")

    @allure.story("Поиск по части названия")
    def test_search_partial_title(self, setup_browser):
        page = BooksPage(setup_browser).open()
        page.search("Git").should_have_book("Git")

    @allure.story("Поиск по автору")
    def test_search_by_author(self, setup_browser):
        page = BooksPage(setup_browser).open()
        page.search("Richard")
        page.should_have_book("Richard E. Silverman")

    @allure.story("Поиск по несуществующему значению")
    def test_search_no_results(self, setup_browser):
        page = BooksPage(setup_browser).open()
        page.search("qwerty123!@#").should_have_no_results()
