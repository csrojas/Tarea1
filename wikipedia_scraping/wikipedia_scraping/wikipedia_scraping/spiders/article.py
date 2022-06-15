from attr import attrib
import scrapy
from wikipedia_scraping.items import articles

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']
    counter =0
    counter2 =0
    bd_ =""


    def parse(self, response):
    
        host = self.allowed_domains[0]
        
        for link  in response.css(".featured_article_metadata > a"):
            if self.counter > 24:
                 return
            else:
                self.counter += 1
                a= f"https://{host}{link.attrib.get('href')}"
                yield scrapy.Request(a,callback=self.parse_page2 )
            
    def parse_page2(self, response):
        titulo = response.css('.firstHeading::text').extract_first()
        vec=[]
        cont=0
        while (response.css('div.mw-parser-output p::text')[cont].extract() != '.\n' ):
            vec.append(response.css('div.mw-parser-output p::text')[cont].extract())
            if cont == 20:
                break
            cont+=1
        parrafo = str(vec)
        aux = {'titulo':titulo,'parrafo': parrafo}
        self.log('eeeeeeeeeeeeeeeeeeeeeeeeeee' +str(aux))
        yield(aux)

        

