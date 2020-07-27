# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
# import pymysql

class NikePipeline(object):
    def __init__(self):
        self.fp = open("images.txt", 'w', encoding='utf-8')
        pass

    def process_item(self, item, spider):
        image_url = item['image_url']
        if image_url is not None and len(image_url) > 0:
            self.fp.write(image_url + '\n')
            pass
        return item

    def close_spider(self,spider):
        self.fp.close()
        pass