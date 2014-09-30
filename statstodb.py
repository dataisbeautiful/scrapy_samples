from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy import log
import datetime
from config import settings
import MySQLdb
 
class StatsToDb(object):
 
    def __init__(self):
        dispatcher.connect(self.stats_spider_closed, signal=signals.stats_spider_closed)
        try:
            self.conn = MySQLdb.connect(user=settings['user'],passwd=settings['password'],db=settings['database'],host=settings['host'],charset=settings['charSet'],use_unicode=settings['useUnicode'])
            self.cursor = self.conn.cursor()
        except:
            print "Unable to connect to the database."
 
    def stats_spider_closed(self, spider, spider_stats):
         try:
             self.cursor.execute("INSERT INTO spider_stats (name, created_at, updated_at, start_time, finish_time, finish_reason, item_scraped_count, images_count, images_uptodate, images_downloaded, request_count, response_count, response_status_count_200, response_status_count_301, response_status_count_302, response_status_count_500) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (spider.name,
                             unicode(datetime.datetime.now().replace(microsecond=0)),
                             unicode(datetime.datetime.now().replace(microsecond=0)),
                             unicode(spider_stats['start_time'].replace(microsecond=0)),
                             unicode(spider_stats['finish_time'].replace(microsecond=0)),
                             spider_stats['finish_reason'].encode('utf-8'),
                             spider_stats['item_scraped_count'] if 'item_scraped_count' in spider_stats  else 0,
                             spider_stats['images_count'] if 'images_count' in spider_stats  else 0 ,
                             spider_stats['images_uptodate'] if 'images_uptodate' in spider_stats  else 0,
                             spider_stats['images_downloaded'] if 'images_downloaded' in spider_stats  else 0,
                             spider_stats['downloader/request_count'] if 'request_count' in spider_stats  else 0,
                             spider_stats['downloader/response_count'] if 'downloader/response_count' in spider_stats  else 0,
                             spider_stats['downloader/response_status_count/200'] if 'downloader/response_status_count/200' in spider_stats else 0,
                             spider_stats['downloader/response_status_count/301'] if 'downloader/response_status_count/301' in spider_stats else 0,
                             spider_stats['downloader/response_status_count/302'] if 'downloader/response_status_count/302' in spider_stats else 0,
                             spider_stats['downloader/response_status_count/500'] if 'downloader/response_status_count/500' in spider_stats else 0,
             ))
             self.conn.commit()
  
         except MySQLdb.DatabaseError, e:
             print 'Error %s' % e
             exit(1)
