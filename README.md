Scrapy Samples
==============

Scrapy spider examples and scripts referenced from my blog http://www.dataisbeautiful.io
These are all written and tested using scrapy 0.24.4

##metademo
Spider to collect the meta tags from a site. Note that it only collects description and keywords tags.

Call with:

`scrapy crawl example`

##ogmeta
Spider to collect the Facebook Open Graph Meta Tags from a site based on PyOpenGraph library that can be found here https://pypi.python.org/pypi/PyOpenGraph

Call with:

`scrapy crawl example`

##mysqldemo
Spider showing how to take start_urls from a database and store scrape results in mysql using a scrapy pipeline

##parameterdemo
Spider that takes multiple arguments, in this case the year and month of the archive page to scrape.

Call with:

`scrapy crawl example -a year=2014 -a month=09`

##statstodb

Save Scrapy spider stats to a mySQL database with this handy extension.
