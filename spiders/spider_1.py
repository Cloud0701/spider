import scrapy
import sqlite3
from .. items import *
class QuoteSpider(scrapy.Spider):
    name = 'data'

    
    start_urls = [
        'https://www.partslink24.com/partslink24/user/login.do'
    ]
        

    def parse(self, response):
        
        items = Project1Item()  
        
        urls = response.css("a.brand-logo::attr(href)").extract()
        items['urls']= urls
        
        
        yield items
        
