import scrapy
from nike.items import NikeItem
from selenium import webdriver

class NikeSpidersSpider(scrapy.Spider):
    name = 'nike_spiders'
    allowed_domains = ['www.nike.com']
    start_urls = ['https://www.nike.com/cn/']

    def __init__(self):
        # use any browser you wish
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=chromeOptions)
        self.browser.implicitly_wait(30)
        pass

    def parse(self, response):
        self.browser.get(response.url)
        results = self.browser.find_elements_by_xpath("//div[@class='ncss-row grid-row']//div[@data-qa='image-media']/img")
        for result in results:
            img_url = result.get_attribute('src')
            item = NikeItem(image_url=img_url)
            yield item
        self.browser.quit()
