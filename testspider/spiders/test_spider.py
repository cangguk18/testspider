import scrapy
#import time
import requests
#import googletrans
#from googletrans import Translator


class testSpider(scrapy.Spider):
    name = 'test_spider'
    
    start_urls = ['https://www.burkett.com/used-restaurant-equipment']
    allowed_domains = ['burkett.com']
    #time.sleep(5)
    #BASE_URL = 'http://www.mhs2000.de'
    #start_urls = ['https://www.secondhand-equipment.com/collections/miscellaneous-1']
   
   
    #handle_httpstatus_list = [403]
    #USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


    #handle_httpstatus_list = [True]

 #   url = r"http://www.imdb.com/search/title?release_date=2017&page=1&ref_=adv_nxt"
#headers = {"Accept-Language": "en-US,en;q=0.5"}

    #def parse(self, response):
       # for category_url in response.xpath('//tr/td/@onclick').extract():   
          #  category_url = 'http://www.hoentsch.net' + category_url[25:][:-2]
          #  yield scrapy.Request(category_url, callback = self.parse_item)
          
    

    #def parse(self, response):
     #   category_url = response.xpath('//div[contains(@class,"new-green  hvr-sweep")]/a/@href').extract()  
      #  for url1 in category_url:
       #     url_desc = response.urljoin(url1)
        #    yield scrapy.Request(url=url_desc, callback = self.parse_cat)

  #  def parse(self, response):
    #    category_url = response.xpath('//li[contains(@class,"product-category product")]/a/@href').extract()  
     #   for url1 in category_url:
       #     url_desc = response.urljoin(url1)
       #     yield scrapy.Request(url=url_desc, callback = self.parse_cat)
            

    def parse(self, response):
        category_url = response.xpath('//div/a[@class="btn btn-sm btn-block btn-main"]/@href').extract()  
        for url1 in category_url:
            url_desc = response.urljoin(url1)
            yield scrapy.Request(url=url_desc, callback = self.parse_cat)

    def parse_cat(self, response):
        category_url = response.xpath('//h2[@class="product-name"]/a/@href').extract()  
        for url1 in category_url:
            url_desc = response.urljoin(url1)
            yield scrapy.Request(url=url_desc, callback = self.parse_item)
        category_url = response.xpath('//div[@class="pages"]/ol/li/a/@href').extract()  
        for url1 in category_url:
            url_desc = response.urljoin(url1)
            yield scrapy.Request(url=url_desc, callback = self.parse_cat)
       
         
        
            


      #  i=1
      #  url_desc = "https://www.westparkgraphic.com/machines/?search=1&stockpage=list&pg=" + str(i)
      #  while i <= 10:
      #      i = i+1
       #     page = requests.get(url_desc)
       #     if page.status_code != 200:
       #        break
       #     url_desc = "https://www.westparkgraphic.com/machines/?search=1&stockpage=list&pg=" + str(i)
        #    yield scrapy.Request(url=url_desc, callback = self.parse)

           # source = requests.get(url).text
           # soup = BeautifulSoup(source, 'lxml')
  


  #  def parse(self, response):
   #     category_url = response.xpath('//a/@href').extract()
    #    for url1 in category_url:
     #       url_desc = response.urljoin(url1)
     #       yield scrapy.Request(url=url_desc, callback = self.parse_item)

            
     
            
   # def parse_cat(self, response):
        #category_url = response.xpath('//li/a[contains(@class,"level-2 col col-md-3 section") and contains(@href,"-USED-")]/@href').extract()
      #  category_url = response.xpath('//div[@class="font-weight-bold"]/a/@href').extract()
       # category_url = response.xpath('//li/a[contains(@href,"id_mac=")]/@href').extract() 
      #  for url1 in category_url:
         #   url_desc = response.urljoin(url1)
         #   yield scrapy.Request(url=url_desc, callback = self.parse_subcat)

  
#scrapy.Request(url=url, cookies= {'googletrans': '/es/en'}, callback=self.parse_details)          

        #for category_url in response.xpath('//h2[@data-role="delta-hit-link"]/a/@href').extract():   
            #category_url = 'https://www.blythmachinery.co.uk' + category_url[0:]
            #yield scrapy.Request(category_url, callback = self.parse_subcat)
     
           #for category_url in response.xpath('//h2[@itemprop="stock"]/a/@href').extract():   
            #category_url = 'https://www.blythmachinery.co.uk' + category_url[0:]
            #yield scrapy.Request(category_url, callback = self.parse_item)
            
  #  def parse_cat(self, response):
     #   category_url = response.xpath('//div[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]/a/@href').extract()
      #                                '//div[@class="block"]/a[contains(@href,"/mobileinventory/")]/@href').extract()
    #    for url1 in category_url:
       #     url_desc = response.urljoin(url1)
       #     yield scrapy.Request(url=url_desc, callback = self.parse_item)
       
   
    #def parse_cat(self, response):
       # for category_url in response.xpath('//tr/td/@onclick').extract():   
           # category_url = 'http://www.nuovalombarmet.it' + category_url[24:]
           # yield scrapy.Request(category_url, callback = self.parse_item)

           
            #yield scrapy.Request(url=url_desc, callback = self.parse_cat, dont_filter = True)

   # def parse(self, response):
        #for category_url in response.xpath('//ul[@id="wpb_wrapper"]/li/a/@href').extract():   
           # category_url = 'https://www.maszyny-drukarskie.pl/' + category_url[3:]
            #category_url = 'https://www.maszyny-drukarskie.pl/' + category_url[0:]
            #yield scrapy.Request(category_url, callback = self.parse_item)

       # for category_url in response.xpath('//tr/@onclick').extract():   
        #    category_url = 'http://www.heinz-inter-trade.com' + category_url[24:][:-2]
        #    yield scrapy.Request(url=category_url, callback = self.parse_item)
 
            #yield scrapy.Request(url=url_desc, callback = self.parse_cat, dont_filter = True)
     
         # a[not (contains(@href,"sold"))]
  #a[contains(@href,"category=")]
         #ul[contains(@class,"product-category product")]
         # a[contains(text(),"btn btn-bordered btn")]
         #  //h2[.='Name' and not(ancestor::div/@class = 'abc')]
       

       # for item in response.xpath('//a[contains(text(),"/nlist/")]/@href').extract():
          #  item_url = 'https://www.arkmachinery.com' + item
          #  yield scrapy.Request(item_url, callback=self.parse_item)

    
    def parse_item(self, response):
        Url = response.url
        #belink = Urls.find("&")
        #Url = Urls[:belink]






        #test = tes.replace('annonces','listings')
        #Url = test.replace('d-occasion','used')
        #UR = response.meta['URL']
        #Description = response.xpath('//div[@class="show-info__title default-listing-title d-none d-md-block"]/h2/text()|'
                                     #'//div[@class="woocommerce-product-details__short-description"]/p[2]/text()|'
                                     #'//div[@class="woocommerce-product-details__short-description"]/p[3]/text()|'
                                     #'//div[@class="product-title"]/p[4]/text()|'
                                     #'//div[@class="post-content"]/p[5]/text()|'
                                     #'//div[@class="post_entry blog"]/h4/text()').extract()
        #Description = response.xpath('//div[@class="elementor-widget-container"]/p[string-length(text()) > 0]/text()').extract()                     
        #Description = response.xpath('//html/body/div[6]/div[2]/div/table/tbody/tr[1]/td/table/tbody/tr/td[3]/strong/text()').extract()
        Description = response.xpath('//h1[@itemprop="name"]/text()').extract()
        Reference = Description[Description.find('No.'):]
        #Reference = response.xpath('//font[contains(text(),"Art.Nr")]/following::font[1]/text()').extract()
        Reference = response.xpath('//td[text()="Storage ID"]/following-sibling::td/text()').extract()
        Year = response.xpath('//td[text()="New in"]/following-sibling::td/text()').extract()
        #Reference = response.xpath('//a[contains(@href,"c_lot")]/ancestor::li/a/text()').extract()
        #Description = response.xpath('//a[contains(@href,"c_lot")]/ancestor::li/text()').extract()
        #Price = response.xpath('//div[@class="summary entry-summary"]/p/span/bdi/text()').extract()
        #Img = response.xpath('//div/img/@src').extract_first()
        #Reference = response.xpath('//div[text()="Year of manufacture"]/following-sibling::div/text()').extract()
        #Description = response.css('#vmMainPage > table > tbody > tr > td:nth-child(1) > div > table:nth-child(2) > tbody > tr > td > h2 ::text').extract()

      

        yield {'description': Description,
               #'model': Model,
               'reference': Reference,
               #'year': Year,
               'price': Price,
               #'image': Img,
               #'URL': response.url,
               'url': Url}
             #yield scrapy.Request(item_url, callback=self.parse_cat)
