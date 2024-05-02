import re
from typing import Final

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

EMAIL_REGEX: Final = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

class Browser:
    def __init__(self, driver) :
        print("Staritng up borwser...")
        self.edge_options = Options
        self.edge_options.add_argument("--headless")
        self.edge_options.add_argument("--disable-extensions")
        self.edge_options.add_argument("--disable-gpu")

        self.service = Service(driver)
        self.browser = webdriver.Edge(service=self.service, options=self.edge_options)

    def scrape_emails(self, url):
        print(f'Scraping {url} for emails..')
        self.browser.get(url)
        page_scource = self.browser.page_source

        list_emails = set()
        for re_match in re.finditer(EMAIL_REGEX, page_scource):
            list_emails.add(re_match.group())
        return list_emails
    
    def close_browser(self):
        print("Closing browser...")
        self.browser.close()



def main():
    driver = webdriver.Edge()
    browser  = Browser(driver=driver)
    
    emails = browser.scrape_emails('https://www.randomlists.com/email-addresses?qty=50')

    for i, email in enumerate(emails, start=1):
        print(i, email, sep=': ')

    
if __name__ == '__main__':
    main()