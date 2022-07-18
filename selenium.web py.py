from selenium import webdriver


class infow():
    def __init__(self, chromedriver=None):
        import time

        from selenium import webdriver

        from selenium.webdriver.chrome.service import Service

        service = Service('C:\chromedriver.exe')

        service.start()

        driver = webdriver.Remote(service.service_url)

        driver.get('http://www.youtube.com/');

    def get_info(self, query):
        self. query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*["id=search input"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*["id=search-form"]/fieldset/button')
        enter.click()

assist = infow()
