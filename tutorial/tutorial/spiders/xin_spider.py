from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import XinItem  


class XinSpider(Spider):
      name="xin"
      allowed_domains=["xin.com"]
      start_urls=["http://www.xin.com/quanguo/s/"]
	 
      def parse(self,response):
          #filename=response.url.split("/")[-2]
          #open(filename,'wb').write(response.body)
          sel = Selector(response)
          sites = sel.xpath('//ul[@class="vtc-info"]/li')
          items=[]
          for site in sites:
              item = XinItem() 
              item['Title'] = site.xpath('a/text()').extract()
              #Location = site.xpath('a/@href').extract()
              #desc = site.xpath('text()').extract()
              items.append(item)
          return items
