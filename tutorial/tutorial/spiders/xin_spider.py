from scrapy.spider import Spider

class XinSpider(Spider):
      name="xin"
      allowed_domains=["xin.com"]
      start_urls=["http://www.xin.com/quanguo/s/"]
	 
      def parse(self,response):
          filename=response.url.split("/")[-2]
          open(filename,'wb').write(response.body)
