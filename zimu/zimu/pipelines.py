# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZimuPipeline(object):
    def __init__(self):
        pass
    def process_item(self, item, spider):
        url = item['url']
        file_name = url.replace('/','_').replace(':','_')
        print("========")
        print(file_name)
        fp = open('result/'+file_name, 'w')
        fp.write(item['body'])
        fp.close()
        return item
