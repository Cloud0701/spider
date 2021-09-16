# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class Project1Pipeline:
    def __init__(self):
        self.create_conn()
        self.create_table()
    
    def create_conn(self):
        self.conn = sqlite3.connect("mydb.db")
        self.c = self.conn.cursor()
    def create_table(self):
        
        self.c.execute("""CREATE TABLE IF NOT EXISTS URLS_DB(
            url text
                )""")

    def process_item(self, item, spider):
       
        self.store_db(item)  
        self.conn.commit()
        return item
    def store_db(self,item):
        for i in item['urls']:
            self.c.execute("""INSERT INTO URLS_DB VALUES (?)""",(
                i,
            )) 
            self.conn.commit()
    
        
        