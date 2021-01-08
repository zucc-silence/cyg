import scrapy
from cyg.items import CygItem

class CygdataSpider(scrapy.Spider):
    name = 'cygdata'
    allowed_domains = ['tl.cyg.changyou.com']
    sellpage=1
    publicpage=0
    url= 'http://tl.cyg.changyou.com/goods/selling?world_id=0&have_chosen=&page_num='
    url2= 'http://tl.cyg.changyou.com/goods/public?world_id=0&have_chosen=&page_num='
    start_urls = [url + str(sellpage)]


    def parse(self, response):
        item = CygItem()
        character = response.xpath("//li[contains(@class, 'role-item')]")
        for each in character:
            s = each.xpath(".//span[@class='name']/text()").extract()[0]
            item['sect'] = str(s[1:-1]).split(" ")[0]
            item['sex'] = str(s[1:-1]).split(" ")[1]
            item['level'] = str(s[1:-1]).split(" ")[2]
            item['name'] = each.xpath(".//a/text()").extract()[1]
            item['score'] = each.xpath(".//span[@class='di' and position()=1]//b/text()").extract()[0]
            item['xiulian'] = each.xpath(".//span[@class='di' and position()=2]//b/text()").extract()[0]
            item['jinjie'] = each.xpath(".//span[@class='di' and position()=3]//b/text()").extract()[0]
            item['price'] = each.xpath(".//p[@class='price']/text()").extract()[0][1:]
            item['area'] = each.xpath(".//span[@class='server-info']/text()").extract()[0][5:]
            if 'selling' in response.url:
                item['is_tag'] = 1
            elif 'public' in response.url:
                item['is_tag'] = 0

            yield item


        if self.sellpage<1316:
            self.sellpage+=1
            yield scrapy.Request(self.url + str(self.sellpage), callback=self.parse)
        else:
            if self.publicpage<964:
                self.publicpage+=1
                yield scrapy.Request(self.url2 + str(self.publicpage), callback=self.parse)