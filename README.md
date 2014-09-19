Scrapy Samples
==============

Scrapy spider examples and scripts referenced from my blog http://www.dataisbeautiful.io
These are all written and tested using scrapy 0.24.4

##metademo
Spider to collect the meta tags from a site. Note that it only collects deccription and keywords tags.

Call with:

`scrapy crawl example`

##mysqldemo
Spider showing how to take start_urls from database and store resutls in mysql

##parameterdemo
Spider that takes multiple arguments, in this case the year and month of the archive page to scrape.

Call with:

`scrapy crawl example -a year=2014 -a month=09`
