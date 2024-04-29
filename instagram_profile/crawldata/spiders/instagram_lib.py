import scrapy,json,re,os,platform,instaloader,time
from crawldata.functions import *
from datetime import datetime

class CrawlerSpider(scrapy.Spider):
    name = 'instagram_lib'
    DATE_CRAWL=datetime.now().strftime('%Y-%m-%d')
    #custom_settings={'LOG_FILE':'./log/'+name+'_'+DATE_CRAWL+'.log'}
    if platform.system()=='Linux':
        URL='file:////' + os.getcwd()+'/scrapy.cfg'
    else:
        URL='file:///' + os.getcwd()+'/scrapy.cfg'
    KEYWORDS=[]
    if os.path.exists('keywords.txt'):
        KEYWORDS=re.split('\r\n|\n',open('keywords.txt').read())
    def start_requests(self):
        yield scrapy.Request(self.URL,callback=self.parse,dont_filter=True)
    def parse(self, response):
        bot = instaloader.Instaloader()
        for keyword in self.KEYWORDS:
            if not str(keyword).startswith('#'):
                search_results = instaloader.TopSearchResults(bot.context, keyword)
                for profile in search_results.get_profiles():
                    time.sleep(3)
                    item={}
                    item['search key']=keyword
                    item['username']=profile.username
                    item['Full name']=profile.full_name
                    item['Number of posts']=profile.mediacount
                    item['Folowers count']=profile.followers
                    item['Folowing count']=profile.followees
                    item['url']='https://www.instagram.com/'+item['username']+'/'
                    email=re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
                    emails=[]
                    for em in email:
                        if not em in emails:
                            emails.append(em)
                    item['Email']=', '.join(emails)
                    item['Boi']=profile.biography
                    item['External url']=profile.external_url
                    yield(item)