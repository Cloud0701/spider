
import sqlite3
import scrapy

from sqlite3.dbapi2 import Cursor
conn = sqlite3.connect("mydb.db")
c = conn.cursor()
c.execute("SELECT * FROM URLS_DB")
a=c.fetchall()
for i in range(0,len(a)-1):
    
    
    
    class QuoteSpider(scrapy.Spider):
        name = 'data2'

    
        start_urls = [
            str(a[i][0])
        ]
        

    def parse(self, response):
        items =  Project1Item()
        model_overview = response.css("td.caption tc-lcell tc-rcell").extract()
        items['model_overview'] = model_overview
        yield items

        
        
        
        pass