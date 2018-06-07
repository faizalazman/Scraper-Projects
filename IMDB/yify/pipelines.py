# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
from scrapy import signals
from scrapy.exporters import CsvItemExporter

class CSVPipeline(object):

  def __init__(self):
    self.files = {}

  @classmethod
  def from_crawler(cls, crawler):
    pipeline = cls()
    crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
    crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
    return pipeline

  def spider_opened(self, spider):
    file = open('%s_items.csv' % spider.name, 'w+b')
    self.files[spider] = file
    self.exporter = CsvItemExporter(file)
    self.exporter.fields_to_export = ['movies','ratings','Actors_1','Actors_2','Actors_3','genre','Synopsis']
    self.exporter.start_exporting()

  def spider_closed(self, spider):
    self.exporter.finish_exporting()
    file = self.files.pop(spider)
    file.close()

    #given I am using Windows i need to elimate the blank lines in the csv file
    print("Starting csv blank line cleaning")
    with open('%s_items.csv' % spider.name, 'r') as f:
      reader = csv.reader(f)
      original_list = list(reader)
      cleaned_list = list(filter(None,original_list))

    with open('%s_items_cleaned.csv' % spider.name, 'w', newline='') as output_file:
        wr = csv.writer(output_file, dialect='excel')
        for data in cleaned_list:
          wr.writerow(data)

  def process_item(self, item, spider):
    self.exporter.export_item(item)
    return item

class YifyPipeline(object):
    def process_item(self, item, spider):
        return item
