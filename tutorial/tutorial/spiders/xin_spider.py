from scrapy.spider import Spider
from scrapy.selector import Selector

class XinSpider(Spider):
      name="xin"
      allowed_domains=["xin.com"]
      start_urls=["http://www.xin.com/quanguo/s/"]
	 
      def parse(self,response):
          #filename=response.url.split("/")[-2]
          #open(filename,'wb').write(response.body)
          sel = Selector(response)
          sites = sel.xpath('//ul/li')
          for site in sites:
              title = site.xpath('a/text()').extract()
              link = site.xpath('a/@href').extract()
              desc = site.xpath('text()').extract()
              print title
