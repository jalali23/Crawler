import scrapy
from ..items import LimoonadItem
from scrapy.http import Request
import json
class my_class(scrapy.Spider):
    name="Individual-development"
    def start_requests(self):
           urls= []
           for i in range(1,4):
              urls.append('https://www.limoonad.com/courses/%d8%aa%d9%88%d8%b3%d8%b9%d9%87-%d9%81%d8%b1%d8%af%db%8c?rank=5&p='+str(i)+'&')
           for url in urls:
              yield scrapy.Request(url=url, callback=self.parse)

      
    def parse(self, response):
            
            for i in range(0,21):     
                for course in response.xpath('//*[@id="search-results"]/section/article['+ str(i+1) +']/div'):
                    items=LimoonadItem()
                    img=course.xpath('//*[@id="search-results"]/section/article['+ str(i+1) +']/div/header/a/img/@src').get(),
                    time=course.xpath('//*[@id="search-results"]/section/article['+ str(i+1) +']/div/header/time/text()').get(),  
                    title=course.xpath('//*[@id="search-results"]/section/article['+ str(i+1) +']/div/div[1]/a/h3/text()').get(),
                    teacher=course.xpath('//*[@id="search-results"]/section/article['+ str(i+1) +']/div/div[1]/small/a/text()').get(),
                    price=course.xpath('//*[@id="search-results"]/section/article['+ str(i+1) +']/div/div[3]/div[1]/div[1]/span[1]/text()').get(),
                    url=course.xpath('//*[@id="search-results"]/section/article['+ str(i+1) +']/div/div[1]/a/@href').get(),


                    items['img']=img
                    items['title']=title
                    items['price']=time
                    items['teacher']=teacher
                    items['time']=price
                    items['url']= url
                    yield items
   
           