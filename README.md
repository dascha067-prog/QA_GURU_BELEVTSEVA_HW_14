<h1> Проект по тестированию сервиса "Book Store Application" (ToolsQA) </h1>

> <a target="_blank" href="https://demoqa.com/books">Ссылка на сайт</a>


![site_testing.png](media/image/site_testing.png)

---
<h3> Список проверок, реализованных в автотестах:</h3>


### UI-тесты

✅ Открытие страницы Book Store  
✅ Поиск книги по точному названию  
✅ Поиск книги по части названия  
✅ Поиск книги по автору  
✅ Поиск книги по несуществующему значению

### Проект реализован с использованием:

<p>
<img src="media/icons/python-original.svg" width="55">
<img src="media/icons/pytest.png" width="55">
<img src="media/icons/selene.png" width="55">
<img src="media/icons/selenoid.png" width="55">
<img src="media/icons/jenkins.png" width="55">
<img src="media/icons/allure_report.png" width="55">
<img src="media/icons/allure_testops.png" width="55">
<img src="media/icons/intellij_pycharm.png" width="55">
<img src="media/icons/jira.png" width="55">
<img src="media/icons/tg.png" width="55">
<p>

---

### <img width="30" title="Jenkins" src="media/icons/jenkins.png"> Запуск проекта в Jenkins

### [Задача в jenkins](https://jenkins.autotests.cloud/job/Qa_guru_hw_14_daria_belevtseva/)

#### Для запуска автотестов в Jenkins

1. Открыть [Проект в Jenkins](https://jenkins.autotests.cloud/job/qa_guru_hw_14_daria_belevtseva/)
2. Выбрать пункт `Build with Parameters`
3. Выбрать тип запускаемых тестов в выпадающем списке Type_of_tests(ui, api, mobile)
4. Выбрать контекст запускаемых тестов в выпадающем списке context(remote_web, bstack, api)
5. Указать версию браузера, по умолчанию стоит 122
6. Нажать кнопку `Build`
7. Результат запуска сборки можно посмотреть в отчёте Allure
   ![Запуск проекта в Jenkins.png](media/image/%D0%97%D0%B0%D0%BF%D1%83%D1%81%D0%BA%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0%20%D0%B2%20Jenkins.png)

---

### <img src="media/icons/allure_report.png" width="30">  Allure отчет

#### Общие результаты

![Общие результаты Allure.png](media/image/%D0%9E%D0%B1%D1%89%D0%B8%D0%B5%20%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B%20Allure.png)

#### Список тест кейсов

![Список тест кейсов Allure.png](media/image/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%20%D1%82%D0%B5%D1%81%D1%82%20%D0%BA%D0%B5%D0%B9%D1%81%D0%BE%D0%B2%20Allure.png)

#### Пример отчета о прохождении ui-теста

![Пример отчета о прохождении ui-тестов.png](media/image/%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%B0%20%D0%BE%20%D0%BF%D1%80%D0%BE%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B8%20ui-%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2.png)

Отчет позволяет получить детальную информацию по все шагам тестов, включая скриншоты, log - файлы и видео о прохождение
теста(набор атач файлов зависит от типа тестов), а так же позволяет оперативно понять причину падения теста.

---

### <img src="media/icons/allure_testops.png" width="30 "> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/5041/dashboards)

![Dashboard с результатами о прохождении тестов в AllureTesOps.png](media/image/Dashboard%20%D1%81%20%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%B0%D0%BC%D0%B8%20%D0%BE%20%D0%BF%D1%80%D0%BE%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B8%20%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%20%D0%B2%20AllureTesOps.png)
Дашборд с результатами о прохождении тестов.

#### Общий список всех кейсов, имеющихся в системе

![Общий список всех тест кейсов в Allure TestOpe.png](media/image/%D0%9E%D0%B1%D1%89%D0%B8%D0%B9%20%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%20%D0%B2%D1%81%D0%B5%D1%85%20%D1%82%D0%B5%D1%81%D1%82%20%D0%BA%D0%B5%D0%B9%D1%81%D0%BE%D0%B2%20%D0%B2%20Allure%20TestOpe.png)

#### Пример отчёта выполнения одного из автотестов

![Пример отчета выполнения одного из автотестов.png](media/image/%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%B0%20%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B8%D0%B7%20%D0%B0%D0%B2%D1%82%D0%BE%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2.png)

#### История запуска тестовых наборов

![История запуска тестовых наборов.png](media/image/%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F%20%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA%D0%B0%20%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D1%85%20%D0%BD%D0%B0%D0%B1%D0%BE%D1%80%D0%BE%D0%B2.png)

---

### <img src="media/icons/jira.png" width="30"> Интеграция с Jira

[Ссылка на проект в Jira](https://jira.autotests.cloud/browse/HOMEWORK-1558)
![Интеграция с Jira.png](media/image/%D0%98%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D1%81%20Jira.png)
---

### <img src="media/icons/tg.png" width="30"> Оповещение о результатах прогона тестов в Telegram

![test telegram.png](media/image/test%20telegram.png)

---

### <img src="media/icons/selenoid.png" width="30"> Пример видео прохождения ui-автотеста

![test_run.gif.gif](media/image/test_run.gif.gif)