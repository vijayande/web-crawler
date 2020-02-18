import scrapy
from scrapy.linkextractors import LinkExtractor
#from ..items import DebenhamsLinksSpiderItem # class to store the fields

class Debenhams_Links_Spider(scrapy.Spider):
    '''
    crawl the url "https://www.debenhams.com" and get all the links from this website
    '''
    name = "Debenhams_Links_Spider"
    #in this list if you keep adding url's the scrapy would crawl all those url's
    start_urls = ['https://www.debenhams.com']

    def parse(self, response):
        #items = DebenhamsLinksSpiderItem() we can use this to store specific fields that we fetch for the crawled url's
        try:
            link_extractor = LinkExtractor()
            links = link_extractor.extract_links(response)
            data = ''
            if len(links) > 0:
                for link in links:
                    data+=link.url+'\n'
            with open("output.txt", 'w') as f:
                f.write(data)
        except:
            return False
